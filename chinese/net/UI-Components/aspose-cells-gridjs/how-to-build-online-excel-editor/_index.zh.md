---
title: 如何在docker中运行Aspose.Cells.GridJs
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: 本文介绍如何在docker中运行GridJs，以构建在线Excel编辑器或查看器应用程序。
aliases:
  - /net/aspose-cells-gridjs/docker/
  - /net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Docker指南

## 先决条件

确保你的机器已安装Docker。你可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 第1步：创建Dockerfile

在你的项目目录中创建一个名为 `Dockerfile` 的文件。`Dockerfile`中应包含构建你的Docker镜像的指令。

## 第2步：为GridJs编写Dockerfile

以下是用于GridJs演示的ASP.NET Core应用的示例 [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Dockerfile)：

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["gridjs-demo-.net6.csproj", "."]
RUN dotnet restore "./gridjs-demo-.net6.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "gridjs-demo-.net6.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "gridjs-demo-.net6.csproj" -c Release -o /app/publish

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
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## 步骤3：构建 Docker 镜像
在终端中执行以下命令以构建您的 Docker 镜像：
```bash
docker build -t gridjs-demo-net6 .
```
你可以用你想要赋予 Docker 镜像的名称替换 gridjs-demo-net6。

## 步骤4：运行 Docker 容器
镜像构建完成后，可以用以下命令运行一个容器：

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

或者直接以试用模式运行演示：


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Docker 运行命令选项说明
-d：在后台运行容器（分离模式）。
-p 24262:80：将容器中的端口 80 映射到主机的 24262 端口。
-v C:/path/to/license.txt:/app/license：将主机上的许可证文件路径映射到容器中的文件路径。
--name gridjs-demo-container：为容器指定一个名称。

## 步骤5：确认容器正在运行
使用以下命令检查您的容器是否在运行：

```bash
docker ps
```
这将列出所有正在运行的容器。您应该能看到您的容器，以及它的名称和状态。

## 步骤6：访问网页应用程序

打开网页浏览器，访问 `http://localhost:24262/GridJs2/List`。你应该会看到你的应用程序在运行。

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
docker rmi gridjs-demo-net6
```




