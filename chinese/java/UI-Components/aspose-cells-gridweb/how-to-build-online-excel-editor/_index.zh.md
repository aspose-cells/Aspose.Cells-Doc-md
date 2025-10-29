---
title: 如何在 Docker 中运行 Aspose.Cells.GridWeb 构建在线电子表格编辑器或查看器应用程序
type: docs
weight: 250
url: /zh/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb，Docker
description: 本文介绍如何在 Docker 中运行 GridWeb，以构建在线 Excel 编辑器或查看器应用程序。
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

确保你的机器已安装Docker。你可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 第1步：创建Dockerfile

在您的项目 [目录](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/) 创建一个名为 `Dockerfile` 的文件。`Dockerfile` 中应包含如何构建您的 Docker 镜像的指令。

## 第二步：为 GridWeb 编写 Dockerfile

以下是带有 Java 应用程序的 GridWeb 演示的 [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) 示例：

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

## 步骤3：构建 Docker 镜像
在终端中执行以下命令以构建您的 Docker 镜像：
```bash
docker build -t gridweb-demo-java .
```
你可以将 `gridweb-demo-java` 替换为你想要的 Docker 镜像名称。

## 步骤4：运行 Docker 容器
镜像构建完成后，可以用以下命令运行一个容器：

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Docker 运行命令选项说明
-d：在后台运行容器（分离模式）。
-p 8080:8080：将容器中的端口 8080 映射到主机的端口 8080。
--name gridweb-demo-container：为容器指定一个名称。

## 步骤5：确认容器正在运行
使用以下命令检查您的容器是否在运行：

```bash
docker ps
```
这将列出所有正在运行的容器。您应该能看到您的容器，以及它的名称和状态。

## 步骤6：访问网页应用程序

打开网页浏览器，访问 `http://localhost:8080/gridwebdemo/index`。你应该会看到你的应用在运行。



## 其他命令

### 停止容器

使用以下命令停止正在运行的容器：

```bash
docker stop gridweb-demo-container
```

### 删除容器
要删除已停止的容器，使用以下命令：

```bash
docker rm  gridweb-demo-container
```

### 删除镜像
要删除某个镜像，使用以下命令：

```bash
docker rmi gridweb-demo-java
```




