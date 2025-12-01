---
title: how to run Aspose.Cells.GridJs in docker
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: This article introduce how to run GridJs in docker to build an online excel editor or viewer application.
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
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Docker Guide

## Prerequisites

Ensure you have Docker installed on your machine. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Step 1: Create a Dockerfile

Create a file named `Dockerfile` in your project [directory](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs). The `Dockerfile` should contain instructions on how to build your Docker image.

## Step 2:Write Dockerfile for GridJs

Here is a sample [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) for GridJs demo with python application:

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

## Step 3: Building the Docker Image
Build the Docker Image: From the terminal, execute the following command to build your Docker image:
```bash
docker build -t gridjs-demo-python .
```
you can replace gridjs-demo-python with the name you want to give your Docker image.

## Step 4: Running a Docker Container
Once the image is built, you can run a container using the following command:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

or just run the demo in trial mode:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Explanation of Docker Run Command Options
-d: Run the container in detached mode (in the background).
-p 2022:2022: Map port 2022 in the container to port 2022 on the host machine.
-v C:/path/to/license.txt:/app/license:  Map license file path on the host machine to the file path in container.
--name gridjs-demo-container: Assign a name to the container.

## Step 5: Verify the Container is Running
To check if your container is running, use the following command:

```bash
docker ps
```
This will list all running containers. You should see your container listed along with its name and status.

## Step 6: Access The Web Application

Open a web browser and go to `http://localhost:2022`. You should see your application running.

## Additional Commands

### Stopping the Container

To stop a running container, use the following command:

```bash
docker stop gridjs-demo-container
```

### Removing a Container
To remove a stopped container, use the following command:

```bash
docker rm  gridjs-demo-container
```

### Removing a Image
To remove an image, use the following command:

```bash
docker rmi gridjs-demo-python
```




