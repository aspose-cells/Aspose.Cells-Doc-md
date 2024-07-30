---
title: Docker で Aspose.Cells.GridWeb を実行する方法
type: docs
weight: 250
url: /ja/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb、Docker
description: この記事では、GridWeb を Docker で実行し、オンラインの Excel エディタまたはビューアー アプリケーションを構築する方法を紹介します。
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

マシンにDockerがインストールされていることを確認してください。 公式Dockerウェブサイト（https://www.docker.com/get-started）からDockerをダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成する

プロジェクト [ディレクトリ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/)に `Dockerfile` という名前のファイルを作成します。 `Dockerfile` には、Docker イメージをビルドする手順が含まれている必要があります。

## ステップ 2: GridWeb 用の Dockerfile を作成する

ASP.NET CoreアプリケーションのGridWebデモ用の[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile)のサンプルです。

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

## ステップ3: Dockerイメージのビルド
Dockerイメージをビルドします。ターミナルから、以下のコマンドを実行してDockerイメージをビルドします。
```bash
docker build -t gridweb-demo-net6 .
```
gridweb-demo-net6を、Dockerイメージに付けたい名前で置き換えることができます。

## ステップ4: Dockerコンテナの実行
イメージが作成されたら、以下のコマンドを使用してコンテナを実行できます。

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Docker Runコマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 24262:80: コンテナのポート80をホストマシンのポート24262にマッピングします。
--name gridweb-demo-container: コンテナに名前を割り当てます。

## ステップ5: コンテナが実行されているか確認する
コンテナが実行されているかどうかを確認するには、次のコマンドを使用します。

```bash
docker ps
```
これにはすべての実行中のコンテナがリストされます。 コンテナがその名前とステータスと共にリストされているはずです。

## ステップ6：Webアプリケーションにアクセス

Webブラウザを開き、`http://localhost:24262/`に移動します。アプリケーションが実行されているのが確認できるはずです。

GridWebの一般的な開発ガイドが表示されます 

ページ内で[demo](http://localhost:24262/grid/index1 "demo")をクリックすると、スプレッドシートファイルの編集操作を行うことができます。

## その他のコマンド

### コンテナの停止

実行中のコンテナを停止するには、次のコマンドを使用します:

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




