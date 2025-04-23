---
title: DockerでAspose.Cells.GridJsを実行する方法
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs、docker
description: この記事は、オンラインExcelエディタまたはビューアアプリケーションを構築するために、Docker内でGridJsを実行する方法を紹介します。
aliases:
  - /net/aspose-cells-gridjs/docker/
  - /net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Dockerガイド

## 前提条件

お使いのマシンにDockerをインストールしていることを確認してください。Dockerは[公式Dockerウェブサイト](https://www.docker.com/get-started)からダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成

プロジェクトの[ディレクトリ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/)に`Dockerfile`というファイルを作成してください。`Dockerfile`には、Dockerイメージをビルドするための命令を記述します。

## ステップ2: GridJs用のDockerfileを書く

ASP.NET Coreアプリケーションを使用したGridJsデモのサンプル [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Dockerfile) です。

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["gridjs-demo-.net6.csproj", "."]
RUN dotnet restore "./gridjs-demo-.net6.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "gridjs-demo-.net6.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "gridjs-demo-.net6.csproj" -c Release -o /app/publish

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
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## ステップ 3: Dockerイメージのビルド
Dockerイメージのビルド：ターミナルから次のコマンドを実行してDockerイメージを作成します：
```bash
docker build -t gridjs-demo-net6 .
```
`gridjs-demo-net6`を、お好みのDockerイメージ名に置き換えることができます。

## ステップ 4: Dockerコンテナの実行
イメージが作成されたら、次のコマンドを使用してコンテナを実行できます：

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

または、デモをトライアルモードで実行するだけです：


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Docker実行コマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 24262:80: コンテナ内のポート80をホストのポート24262にマッピングします。
-v C:/path/to/license.txt:/app/license: ホストマシンのライセンスファイルのパスをコンテナ内のファイルパスにマッピングします。
--name gridjs-demo-container: コンテナに名前を割り当てます。

## ステップ 5: コンテナが実行中か確認する
コンテナが稼働しているかどうかを確認するには、次のコマンドを使用してください：

```bash
docker ps
```
これにより、すべての実行中のコンテナがリストされます。あなたのコンテナが名前とステータスとともに表示されるはずです。

## ステップ 6: Webアプリケーションへアクセスする

Webブラウザを開き、`http://localhost:24262/GridJs2/List`にアクセスしてください。アプリケーションが動作しているのが確認できます。

## 追加コマンド

### コンテナの停止

実行中のコンテナを停止するには、次のコマンドを使用します：

```bash
docker stop gridjs-demo-container
```

### コンテナの削除
停止したコンテナを削除するには、次のコマンドを使用します：

```bash
docker rm  gridjs-demo-container
```

### イメージの削除
イメージを削除するには、次のコマンドを使用します：

```bash
docker rmi gridjs-demo-net6
```




