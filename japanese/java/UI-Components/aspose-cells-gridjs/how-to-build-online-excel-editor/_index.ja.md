---
title: DockerでAspose.Cells.GridJsを実行する方法
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs、docker
description: この記事では、オンラインのExcelエディタまたはビューアアプリケーションを構築するためにDockerでGridJsを実行する方法について紹介します。
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

マシンにDockerがインストールされていることを確認してください。 公式Dockerウェブサイト（https://www.docker.com/get-started）からDockerをダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成する

プロジェクトディレクトリ（https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs）に`Dockerfile`という名前のファイルを作成します。`Dockerfile`には、Dockerイメージをビルドする方法に関する指示が含まれている必要があります。

## ステップ2: GridJs用のDockerfileを作成する

以下は、Javaアプリケーションを使用したGridJsデモ用のサンプル[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile)です。

```dockerfile
# Use the jdk8 image
FROM eclipse/ubuntu_jdk8
WORKDIR /usr/src/app


# copy local Maven files to container
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN ./mvnw package -DskipTests

# Set the user
USER root

#RUN ls -l *

# copy the build output jar to container
COPY  target/*.jar /app/app.jar

# delete build source to reduce storage usage
RUN rm -rf target && rm -rf .mvn && rm -rf src
# web port
EXPOSE 8080
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## ステップ3: Dockerイメージのビルド
Dockerイメージをビルドします。ターミナルから、以下のコマンドを実行してDockerイメージをビルドします。
```bash
docker build -t gridjs-demo-java .
```
gridjs-demo-javaをお好みのDockerイメージの名前で置き換えることができます。

## ステップ4: Dockerコンテナの実行
イメージが作成されたら、以下のコマンドを使用してコンテナを実行できます。

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Docker Runコマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 8080:80: コンテナ内のポート80をホストマシンのポート8080にマッピングします。
--name gridjs-demo-container: コンテナに名前を割り当てます。

## ステップ5: コンテナが実行されているか確認する
コンテナが実行されているかどうかを確認するには、次のコマンドを使用します。

```bash
docker ps
```
これにはすべての実行中のコンテナがリストされます。 コンテナがその名前とステータスと共にリストされているはずです。

## ステップ6：Webアプリケーションにアクセス

`http://localhost:8080/gridjsdemo/index`に移動してWebブラウザを開きます。アプリケーションが実行されているのを確認できます。

## その他のコマンド

### コンテナの停止

実行中のコンテナを停止するには、次のコマンドを使用します:

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




