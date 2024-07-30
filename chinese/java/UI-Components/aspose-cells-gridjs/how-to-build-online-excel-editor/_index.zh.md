---
title: 如何在docker中运行Aspose.Cells.GridJs
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs，docker
description: 本文介绍了如何在docker中运行GridJs以构建在线Excel编辑器或查看器应用程序。
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

确保您的计算机上已安装Docker。您可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 步骤1：创建一个Dockerfile

在您的项目[目录](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs)中创建名为`Dockerfile`的文件。`Dockerfile`应该包含构建Docker镜像的说明。

## 步骤2：为GridJs编写Dockerfile

这是一个GridJs演示与Java应用程序的样本[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile)：

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

## 步骤3：构建Docker镜像
构建Docker镜像：从终端执行以下命令来构建Docker镜像：
```bash
docker build -t gridjs-demo-java .
```
您可以用您想要给Docker镜像的名称替换gridjs-demo-java。

## 步骤4：运行Docker容器
构建镜像后，您可以使用以下命令来运行一个容器：

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Docker运行命令选项的说明
-d：在分离模式下运行容器（在后台）。
-p 8080:80：将容器中端口80映射到主机上的端口8080。
--name gridjs-demo-container：为容器指定一个名称。

## 步骤5：验证容器是否正在运行
要检查容器是否正在运行，请使用以下命令：

```bash
docker ps
```
这将列出所有正在运行的容器。你应该能看到你的容器以及它的名称和状态。

## 步骤 6: 访问Web应用程序

打开浏览器，转到 ` http://localhost:8080/gridjsdemo/index`。您应该看到您的应用程序正在运行。

## 额外命令

### 停止容器

要停止运行的容器，使用以下命令:

```bash
docker stop gridjs-demo-container
```

### 删除容器
要删除一个停止的容器，使用以下命令:

```bash
docker rm  gridjs-demo-container
```

### 删除图像
要删除图像，请使用以下命令：

```bash
docker rmi gridjs-demo-java
```




