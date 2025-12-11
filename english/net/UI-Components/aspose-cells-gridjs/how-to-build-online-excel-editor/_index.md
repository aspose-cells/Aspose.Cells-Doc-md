---
title: how to run Aspose.Cells.GridJs in Docker
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: This article introduces how to run GridJs in Docker to build an online Excel editor or viewer application.
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
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Docker Guide

## Prerequisites

Ensure you have Docker installed on your machine. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Step 1: Create a Dockerfile

Create a file named `Dockerfile` in your project [directory](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/). The `Dockerfile` should contain instructions on how to build your Docker image.

## Step 2: Write Dockerfile for GridJs

Here is a sample [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Dockerfile) for GridJs demo with ASP.NET Core application:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build environment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
# We shall use .NET 6.0 project
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
# If you want a better display like in Windows, you need to install a variety of fonts in /usr/share/fonts/
# Then the application can parse and render the fonts that are used in the spreadsheet file.
# Here we don't provide extra fonts resource.
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to Docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# The basic file path that contains the spreadsheet files
RUN mkdir -p /app/wb
# The file path to store the uploaded files
RUN mkdir -p /app/uploads
# The cache file path for GridJs
RUN mkdir -p /app/grid_cache
# We provide some sample spreadsheet files in the demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# Set the start command for the Docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Step 3: Building the Docker Image
Build the Docker Image: From the terminal, execute the following command to build your Docker image:
```bash
docker build -t gridjs-demo-net6 .
```
You can replace `gridjs-demo-net6` with the name you want to give your Docker image.

## Step 4: Running a Docker Container
Once the image is built, you can run a container using the following command:

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

or just run the demo in trial mode:

```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```

**Explanation of Docker Run Command Options**  
- `-d`: Run the container in detached mode (in the background).  
- `-p 24262:80`: Map port 80 in the container to port 24262 on the host machine.  
- `-v C:/path/to/license.txt:/app/license`: Map the license file path on the host machine to the file path in the container.  
- `--name gridjs-demo-container`: Assign a name to the container.

## Step 5: Verify the Container is Running
To check if your container is running, use the following command:

```bash
docker ps
```
This will list all running containers. You should see your container listed along with its name and status.

## Step 6: Access the Web Application

Open a web browser and go to `http://localhost:24262/GridJs2/List`. You should see your application running.

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

### Removing an Image
To remove an image, use the following command:

```bash
docker rmi gridjs-demo-net6
```
