---
title: 如何在docker中运行Aspose.Cells.GridJs
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: 本文介绍如何在docker中运行GridJs，以构建在线Excel编辑器或查看器应用程序。
aliases:
  - /python-net/aspose-cells-gridjs/docker/
  - /python-net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Docker指南

## 先决条件

确保你的机器已安装Docker。你可以从[官方Docker网站](https://www.docker.com/get-started)下载并安装Docker。

## 第1步：创建Dockerfile

在你的项目[目录](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs)中创建一个名为 `Dockerfile` 的文件。`Dockerfile` 应包含关于如何构建你的 Docker 镜像的指令。

## 第2步：为GridJs编写Dockerfile

这是一个示例 [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile)，用于 GridJs 演示和 Python 应用程序：

```dockerfile
# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
	fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  

# copy all to  /app  
COPY . /app  


RUN pip install --no-cache-dir -r requirements.txt  
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/



# start cmd
CMD [ "python", "./main.py" ]
```

## 步骤3：构建 Docker 镜像
在终端中执行以下命令以构建您的 Docker 镜像：
```bash
docker build -t gridjs-demo-python .
```
你可以用你想为你的 Docker 镜像命名的名称替换 gridjs-demo-python。

## 步骤4：运行 Docker 容器
镜像构建完成后，可以用以下命令运行一个容器：

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

或者直接以试用模式运行演示：


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Docker 运行命令选项说明
-d：在后台运行容器（分离模式）。
-p 2022:2022：将容器中的端口 2022 映射到主机上的端口 2022。
-v C:/path/to/license.txt:/app/license：将主机上的许可证文件路径映射到容器中的文件路径。
--name gridjs-demo-container：为容器指定一个名称。

## 步骤5：确认容器正在运行
使用以下命令检查您的容器是否在运行：

```bash
docker ps
```
这将列出所有正在运行的容器。您应该能看到您的容器，以及它的名称和状态。

## 步骤6：访问网页应用程序

用网页浏览器打开 `http://localhost:2022`。你应该会看到你的应用在运行。

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
docker rmi gridjs-demo-python
```




