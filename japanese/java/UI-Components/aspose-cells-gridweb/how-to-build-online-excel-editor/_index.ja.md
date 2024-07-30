---
title: Dockerでオンラインスプレッドシートエディタまたはビューアーアプリケーションをビルドする方法
type: docs
weight: 250
url: /ja/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb、docker
description: この記事では、dockerでGridWebを実行してオンラインエクセルエディタまたはビューアーアプリケーションを構築する方法を紹介します。
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

マシンにDockerがインストールされていることを確認してください。 公式Dockerウェブサイト（https://www.docker.com/get-started）からDockerをダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成する

プロジェクト[ディレクトリ](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/)に`Dockerfile`という名前のファイルを作成します。`Dockerfile`には、Dockerイメージをビルドする方法に関する命令を含めます。

## ステップ2：GridWebのDockerfileを書く

こちらはJavaアプリケーションを使用したGridWebデモのための[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile)のサンプルです：

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
# create [log dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## ステップ3: Dockerイメージのビルド
Dockerイメージをビルドします。ターミナルから、以下のコマンドを実行してDockerイメージをビルドします。
```bash
docker build -t gridweb-demo-java .
```
ユーザーが名前をつけたいDockerイメージの名前でgridweb-demo-javaを置き換えることができます。

## ステップ4: Dockerコンテナの実行
イメージが作成されたら、以下のコマンドを使用してコンテナを実行できます。

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Docker Runコマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 8080:8080：コンテナ内のポート8080をホストマシンのポート8080にマップします。
--name gridweb-demo-container：コンテナに名前を割り当てます。

## ステップ5: コンテナが実行されているか確認する
コンテナが実行されているかどうかを確認するには、次のコマンドを使用します。

```bash
docker ps
```
これにはすべての実行中のコンテナがリストされます。 コンテナがその名前とステータスと共にリストされているはずです。

## ステップ6：Webアプリケーションにアクセス

`http://localhost:8080/gridwebdemo/index`に移動してWebブラウザを開きます。アプリケーションが実行されているのを確認できます。



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
docker rmi gridweb-demo-java
```




