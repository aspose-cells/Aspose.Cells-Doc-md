---
title: 如何在docker中运行Aspose.Cells.GridWeb来构建在线电子表格编辑器或查看器应用程序
type: docs
weight: 250
url: /zh/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb，docker
description: 本文介绍了如何在Docker中运行GridWeb，以构建在线Excel编辑器或查看器应用程序。
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

# Docker指南

## 先决条件

确保您的计算机上已安装Docker。您可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 步骤1：创建一个Dockerfile

在您的项目[目录](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/)中创建名为`Dockerfile`的文件。 `Dockerfile` 应包含构建Docker镜像的指令。

## 步骤2：为GridWeb编写Dockerfile

以下是包含Java应用程序的GridWeb演示的样本[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile):

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

## 步骤3：构建Docker镜像
构建Docker镜像：从终端执行以下命令来构建Docker镜像：
```bash
docker build -t gridweb-demo-java .
```
您可以将 gridweb-demo-java 替换为您要为Docker镜像命名的名称。

## 步骤4：运行Docker容器
构建镜像后，您可以使用以下命令来运行一个容器：

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Docker运行命令选项的说明
-d：在分离模式下运行容器（在后台）。
-p 8080:8080: 将容器中的端口8080映射到主机上的端口8080。
--name gridweb-demo-container: 为容器指定一个名称。

## 步骤5：验证容器是否正在运行
要检查容器是否正在运行，请使用以下命令：

```bash
docker ps
```
这将列出所有正在运行的容器。你应该能看到你的容器以及它的名称和状态。

## 步骤 6: 访问Web应用程序

在Web浏览器中打开 `http://localhost:8080/gridwebdemo/index`。您应该能够看到您的应用程序正在运行。



## 额外命令

### 停止容器

要停止运行的容器，使用以下命令:

```bash
docker stop gridweb-demo-container
```

### 删除容器
要删除一个停止的容器，使用以下命令:

```bash
docker rm  gridweb-demo-container
```

### 删除图像
要删除图像，请使用以下命令：

```bash
docker rmi gridweb-demo-java
```




