---
title: Aspose.Cells.GridWebをDockerで実行する方法
type: docs
weight: 250
url: /ja/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb、Docker
description: この記事では、Docker内でGridWebを実行し、オンラインExcelエディタまたはビューアアプリケーションを構築する方法を紹介します。
aliases:
  - /net/aspose-cells-gridweb/docker/
  - /net/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /net/aspose-cells-gridweb/run-gridweb-in-docker/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Dockerガイド

## 前提条件

お使いのマシンにDockerをインストールしていることを確認してください。Dockerは[公式Dockerウェブサイト](https://www.docker.com/get-started)からダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成

プロジェクトの[ディレクトリ](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/)に`Dockerfile`という名前のファイルを作成します。`Dockerfile`にはDockerイメージのビルド方法に関する指示を記述します。

## ステップ 2: GridWeb用のDockerfileを作成

ASP.NET Coreアプリケーションを使ったGridWebデモ用のサンプル[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/Dockerfile)です：

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["GridWeb.Demo.NET6.0.csproj", "."]
RUN dotnet restore "./GridWeb.Demo.NET6.0.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/publish

# Final stage/image
FROM base AS final
WORKDIR /app
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridWeb
RUN mkdir -p /app/filecache
# the cache picture path for GridWeb
RUN mkdir -p /app/piccache
COPY wwwroot/wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "GridWeb.Demo.NET6.0.dll"]
```

## ステップ 3: Dockerイメージのビルド
Dockerイメージのビルド：ターミナルから次のコマンドを実行してDockerイメージを作成します：
```bash
docker build -t gridweb-demo-net6 .
```
`gridweb-demo-net6`をあなたのDockerイメージ名に置き換えてください。

## ステップ 4: Dockerコンテナの実行
イメージが作成されたら、次のコマンドを使用してコンテナを実行できます：

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Docker実行コマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 24262:80: コンテナ内のポート80をホストのポート24262にマッピングします。
--name gridweb-demo-container: コンテナに名前を付けます。

## ステップ 5: コンテナが実行中か確認する
コンテナが稼働しているかどうかを確認するには、次のコマンドを使用してください：

```bash
docker ps
```
これにより、すべての実行中のコンテナがリストされます。あなたのコンテナが名前とステータスとともに表示されるはずです。

## ステップ 6: Webアプリケーションへアクセスする

ウェブブラウザを開き、`http://localhost:24262/`にアクセスしてください。アプリケーションが動作しているのが見えます。

GridWebの一般的な開発ガイドを見ることができます。 

ページ内の [デモ](http://localhost:24262/grid/index1 "デモ")をクリックすると、スプレッドシートファイルの編集操作が可能です。

## 追加コマンド

### コンテナの停止

実行中のコンテナを停止するには、次のコマンドを使用します：

```bash
docker stop gridweb-demo-container
```

### コンテナの削除
停止したコンテナを削除するには、次のコマンドを使用します：

```bash
docker rm  gridweb-demo-container
```

### イメージの削除
イメージを削除するには、次のコマンドを使用します：

```bash
docker rmi gridweb-demo-net6
```




