---
title: DockerでAspose.Cells.GridJsを実行する方法
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs、docker
description: この記事は、オンラインExcelエディタまたはビューアアプリケーションを構築するために、Docker内でGridJsを実行する方法を紹介します。
aliases:
  - /java/aspose-cells-gridjs/docker/
  - /java/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /java/aspose-cells-gridjs/run-gridjs-in-docker/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Dockerガイド

## 前提条件

お使いのマシンにDockerをインストールしていることを確認してください。Dockerは[公式Dockerウェブサイト](https://www.docker.com/get-started)からダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成

あなたのプロジェクト[ディレクトリ](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs)に `Dockerfile` という名前のファイルを作成してください。`Dockerfile` には、Dockerイメージのビルド方法に関する指示を記述します。

## ステップ2: GridJs用のDockerfileを書く

次の例は、Javaアプリケーションを使用したGridJsデモ用の [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) 例です：

```dockerfile
# Use the maven image to build jar file
FROM maven:3.8.6-amazoncorretto-17 AS build
WORKDIR /usr/src/app


# copy local Maven files to container
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN mvn  package -DskipTests


# Use the jdk8 image as the basic docker image
FROM eclipse/ubuntu_jdk8
WORKDIR /app
# copy build jar file to target container 
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
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
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## ステップ 3: Dockerイメージのビルド
Dockerイメージのビルド：ターミナルから次のコマンドを実行してDockerイメージを作成します：
```bash
docker build -t gridjs-demo-java .
```
`gridjs-demo-java` をあなたが付けたい任意の名前に置き換えることができます。

## ステップ 4: Dockerコンテナの実行
イメージが作成されたら、次のコマンドを使用してコンテナを実行できます：

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

または、デモをトライアルモードで実行するだけです：


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Docker実行コマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 8080:80: コンテナの80番ポートをホストマシンの8080番ポートにマッピングします。
-v C:/path/to/license.txt:/app/license: ホストマシンのライセンスファイルのパスをコンテナ内のファイルパスにマッピングします。
--name gridjs-demo-container: コンテナに名前を割り当てます。

## ステップ 5: コンテナが実行中か確認する
コンテナが稼働しているかどうかを確認するには、次のコマンドを使用してください：

```bash
docker ps
```
これにより、すべての実行中のコンテナがリストされます。あなたのコンテナが名前とステータスとともに表示されるはずです。

## ステップ 6: Webアプリケーションへアクセスする

Webブラウザを開き、` http://localhost:8080/gridjsdemo/index` にアクセスしてください。アプリケーションが動作しているはずです。

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
docker rmi gridjs-demo-java
```




