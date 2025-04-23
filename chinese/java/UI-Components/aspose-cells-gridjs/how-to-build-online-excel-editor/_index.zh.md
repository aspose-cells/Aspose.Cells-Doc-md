---
title: 如何在docker中运行Aspose.Cells.GridJs
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: 本文介绍如何在docker中运行GridJs，以构建在线Excel编辑器或查看器应用程序。
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

# Docker指南

## 先决条件

确保你的机器已安装Docker。你可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 第1步：创建Dockerfile

在你的项目[目录](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs)中创建一个名为`Dockerfile`的文件。`Dockerfile`应包含构建你的Docker镜像的指令。

## 第2步：为GridJs编写Dockerfile

这里是一个用于GridJs演示的 [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) 示例，包含Java应用：

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

## 步骤3：构建 Docker 镜像
在终端中执行以下命令以构建您的 Docker 镜像：
```bash
docker build -t gridjs-demo-java .
```
你可以用你想要的名字替换 `gridjs-demo-java`，作为你的Docker镜像名称。

## 步骤4：运行 Docker 容器
镜像构建完成后，可以用以下命令运行一个容器：

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

或者直接以试用模式运行演示：


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Docker 运行命令选项说明
-d：在后台运行容器（分离模式）。
-p 8080:80：将容器内的80端口映射到主机的8080端口。
-v C:/path/to/license.txt:/app/license：将主机上的许可证文件路径映射到容器中的文件路径。
--name gridjs-demo-container：为容器指定一个名称。

## 步骤5：确认容器正在运行
使用以下命令检查您的容器是否在运行：

```bash
docker ps
```
这将列出所有正在运行的容器。您应该能看到您的容器，以及它的名称和状态。

## 步骤6：访问网页应用程序

打开网页浏览器，访问 `http://localhost:8080/gridjsdemo/index`。你应该能看到你的应用正在运行。

## 其他命令

### 停止容器

使用以下命令停止正在运行的容器：

```bash
docker stop gridjs-demo-container
```

### 删除容器
要删除已停止的容器，使用以下命令：

```bash
docker rm  gridjs-demo-container
```

### 删除镜像
要删除某个镜像，使用以下命令：

```bash
docker rmi gridjs-demo-java
```




