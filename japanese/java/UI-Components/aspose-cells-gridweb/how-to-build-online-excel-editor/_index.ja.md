---
title: Aspose.Cells.GridWebをDockerで起動し、オンラインスプレッドシートエディタまたはビューアアプリケーションを構築する方法
type: docs
weight: 250
url: /ja/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb、Docker
description: この記事では、Docker内でGridWebを実行し、オンラインExcelエディタまたはビューアアプリケーションを構築する方法を紹介します。
aliases:
  - /java/aspose-cells-gridweb/docker/
  - /java/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /java/aspose-cells-gridweb/run-gridweb-in-docker/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Dockerガイド

## 前提条件

お使いのマシンにDockerをインストールしていることを確認してください。Dockerは[公式Dockerウェブサイト](https://www.docker.com/get-started)からダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成

プロジェクトの[ディレクトリ](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/)に`Dockerfile`という名前のファイルを作成します。`Dockerfile`には、Dockerイメージのビルド方法に関する指示を記載してください。

## ステップ 2: GridWeb用のDockerfileを作成

GridWebデモとJavaアプリケーション用のサンプル`Dockerfile`（[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile)）はこちら：

```dockerfile
#spring boot3.3 shall use jdk17 above 
FROM openjdk:17-jdk-slim  AS build

# set work dir
WORKDIR /usr/src/app

# copy with maven
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

RUN chmod +x mvnw
# build with maven
RUN ./mvnw package -DskipTests


RUN ls -l target

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built JAR file from the build stage
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/

# Install necessary dependencies for font management,because we use jdk-slim ,we need to install it
RUN apt-get update && apt-get install -y fontconfig libfreetype6 && rm -rf /var/lib/apt/lists/*

# Set the environment variable for headless mode,no need to use display
ENV JAVA_OPTS="-Djava.awt.headless=true"
# create [log dir](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## ステップ 3: Dockerイメージのビルド
Dockerイメージのビルド：ターミナルから次のコマンドを実行してDockerイメージを作成します：
```bash
docker build -t gridweb-demo-java .
```
`gridweb-demo-java`は、あなたが希望するDockerイメージの名前に置き換えることができます。

## ステップ 4: Dockerコンテナの実行
イメージが作成されたら、次のコマンドを使用してコンテナを実行できます：

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Docker実行コマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 8080:8080: コンテナ内のポート8080をホストマシンのポート8080にマッピングします。
--name gridweb-demo-container: コンテナに名前を付けます。

## ステップ 5: コンテナが実行中か確認する
コンテナが稼働しているかどうかを確認するには、次のコマンドを使用してください：

```bash
docker ps
```
これにより、すべての実行中のコンテナがリストされます。あなたのコンテナが名前とステータスとともに表示されるはずです。

## ステップ 6: Webアプリケーションへアクセスする

Webブラウザを開き、`http://localhost:8080/gridwebdemo/index`にアクセスしてください。アプリケーションが稼働しているはずです。



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
docker rmi gridweb-demo-java
```




