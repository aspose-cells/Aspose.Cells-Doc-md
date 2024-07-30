---
title: 如何在docker中运行Aspose.Cells.GridWeb
type: docs
weight: 250
url: /zh/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb，docker
description: 本文介绍了如何在docker中运行GridWeb以构建在线Excel编辑器或查看器应用程序。
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

# Docker指南

## 先决条件

确保您的计算机上已安装Docker。您可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 步骤1：创建一个Dockerfile

在项目[目录](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/)中创建名为`Dockerfile`的文件。 `Dockerfile`应包含有关如何构建Docker镜像的说明。

## 步骤2：为GridWeb编写Dockerfile

这是一个带有ASP.NET Core应用程序的GridWeb演示的样本[`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile)：

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

## 步骤3：构建Docker镜像
构建Docker镜像：从终端执行以下命令来构建Docker镜像：
```bash
docker build -t gridweb-demo-net6 .
```
您可以将gridweb-demo-net6替换为您想要给Docker镜像命名的名称。

## 步骤4：运行Docker容器
构建镜像后，您可以使用以下命令来运行一个容器：

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Docker运行命令选项的说明
-d：在分离模式下运行容器（在后台）。
-p 24262:80: 将容器中的端口 80 映射到主机上的端口 24262。
--name gridweb-demo-container: 为容器分配一个名称。

## 步骤5：验证容器是否正在运行
要检查容器是否正在运行，请使用以下命令：

```bash
docker ps
```
这将列出所有正在运行的容器。你应该能看到你的容器以及它的名称和状态。

## 步骤 6: 访问Web应用程序

打开网页浏览器，输入 `http://localhost:24262/`。您应该可以看到您的应用程序正在运行。

您将看到GridWeb的通用开发指南。 

在页面中点击[demo](http://localhost:24262/grid/index1 "demo")，您可以对电子表格文件进行编辑操作。

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
docker rmi gridweb-demo-net6
```




