---
title: 在Docker中运行Aspose.Cells.GridWeb的方法
type: docs
weight: 250
url: /zh/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb，Docker
description: 本文介绍如何在 Docker 中运行 GridWeb，以构建在线 Excel 编辑器或查看器应用程序。
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

确保你的机器已安装Docker。你可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 第1步：创建Dockerfile

在你的项目 [目录](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/) 中创建一个名为 `Dockerfile` 的文件。`Dockerfile` 应包含构建 Docker 镜像的指令。

## 第二步：为 GridWeb 编写 Dockerfile

以下是 GridWeb 演示的 [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/Dockerfile)，用于 ASP.NET Core 应用程序：

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

## 步骤3：构建 Docker 镜像
在终端中执行以下命令以构建您的 Docker 镜像：
```bash
docker build -t gridweb-demo-net6 .
```
你可以将gridweb-demo-net6替换为你想给你的Docker镜像命名的名称。

## 步骤4：运行 Docker 容器
镜像构建完成后，可以用以下命令运行一个容器：

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Docker 运行命令选项说明
-d：在后台运行容器（分离模式）。
-p 24262:80：将容器中的端口 80 映射到主机的 24262 端口。
--name gridweb-demo-container：为容器指定一个名称。

## 步骤5：确认容器正在运行
使用以下命令检查您的容器是否在运行：

```bash
docker ps
```
这将列出所有正在运行的容器。您应该能看到您的容器，以及它的名称和状态。

## 步骤6：访问网页应用程序

打开网页浏览器，访问`http://localhost:24262/`。你应该会看到你的应用程序在运行。

你将看到GridWeb的通用开发指南 

点击页面中的[演示](http://localhost:24262/grid/index1 "demo")，你可以对电子表格文件进行编辑操作。

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
docker rmi gridweb-demo-net6
```




