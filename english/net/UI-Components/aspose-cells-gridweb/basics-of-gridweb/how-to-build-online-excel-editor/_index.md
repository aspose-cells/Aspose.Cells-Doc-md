---
title: how to run Aspose.Cells.GridWeb in docker
type: docs
weight: 250
url: /net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb,docker
description: This article introduces how to run GridWeb in Docker to build an online Excel editor or viewer application.
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
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Docker Guide

## Prerequisites

Ensure you have Docker installed on your machine. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Step 1: Create a Dockerfile

Create a file named `Dockerfile` in your project [directory](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/). The `Dockerfile` should contain instructions on how to build your Docker image.

## Step 2: Write Dockerfile for GridWeb

Here is a sample [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/Dockerfile) for a GridWeb demo with an ASP.NET Core application:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 

# Use the official .NET6.0 SDK as build environment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
# we shall use .NET 6.0 project
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
# If you want better display like in Windows, you need to install fonts in /usr/share/fonts/
# Then the application can parse and render the fonts used in the spreadsheet file.
# Here we don't provide extra font resources.
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to the Docker image.
# Make sure you have a local “fonts” directory that contains all the fonts you need to install.
# In this example, the local “fonts” directory is placed in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# The basic file path which contains the spreadsheet files
RUN mkdir -p /app/wb
# The cache file path for GridWeb
RUN mkdir -p /app/filecache
# The cache picture path for GridWeb
RUN mkdir -p /app/piccache
COPY wwwroot/wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# Set the start command for the Docker image 
ENTRYPOINT ["dotnet", "GridWeb.Demo.NET6.0.dll"]
```

## Step 3: Building the Docker Image

Build the Docker image: from the terminal, execute the following command:

```bash
docker build -t gridweb-demo-net6 .
```

You can replace `gridweb-demo-net6` with the name you want to give your Docker image.

## Step 4: Running a Docker Container

Once the image is built, you can run a container using the following command:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container gridweb-demo-net6
```

### Explanation of Docker Run Command Options
- `-d`: Run the container in detached mode (in the background).
- `-p 24262:80`: Map port 80 in the container to port 24262 on the host machine.
- `--name gridweb-demo-container`: Assign a name to the container.

## Step 5: Verify the Container is Running

To check if your container is running, use the following command:

```bash
docker ps
```

This will list all running containers. You should see your container listed along with its name and status.

## Step 6: Access the Web Application

Open a web browser and go to `http://localhost:24262/`. You should see your application running.

You will see the general development guide for GridWeb.

Click the [demo](http://localhost:24262/grid/index1 "demo") on the page; you can edit the spreadsheet file.

## Additional Commands

### Stopping the Container

To stop a running container, use the following command:

```bash
docker stop gridweb-demo-container
```

### Removing a Container

To remove a stopped container, use the following command:

```bash
docker rm gridweb-demo-container
```

### Removing an Image

To remove an image, use the following command:

```bash
docker rmi gridweb-demo-net6
```
