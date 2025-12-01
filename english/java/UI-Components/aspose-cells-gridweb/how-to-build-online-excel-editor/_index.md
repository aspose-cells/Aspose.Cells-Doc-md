---
title: how to run Aspose.Cells.GridWeb to build online spreadsheet editor or viewer application in docker
type: docs
weight: 250
url: /java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb,docker
description: This article introduce how to run GridWeb in docker to build an online excel editor or viewer application.
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
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Docker Guide

## Prerequisites

Ensure you have Docker installed on your machine. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Step 1: Create a Dockerfile

Create a file named `Dockerfile` in your project [directory](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). The `Dockerfile` should contain instructions on how to build your Docker image.

## Step 2:Write Dockerfile for GridWeb

Here is a sample [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) for GridWeb demo with java application:

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

## Step 3: Building the Docker Image
Build the Docker Image: From the terminal, execute the following command to build your Docker image:
```bash
docker build -t gridweb-demo-java .
```
you can replace gridweb-demo-java with the name you want to give your Docker image.

## Step 4: Running a Docker Container
Once the image is built, you can run a container using the following command:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Explanation of Docker Run Command Options
-d: Run the container in detached mode (in the background).
-p 8080:8080: Map port 8080 in the container to port 8080 on the host machine.
--name gridweb-demo-container: Assign a name to the container.

## Step 5: Verify the Container is Running
To check if your container is running, use the following command:

```bash
docker ps
```
This will list all running containers. You should see your container listed along with its name and status.

## Step 6: Access The Web Application

Open a web browser and go to `http://localhost:8080/gridwebdemo/index`. You should see your application running.

 

## Additional Commands

### Stopping the Container

To stop a running container, use the following command:

```bash
docker stop gridweb-demo-container
```

### Removing a Container
To remove a stopped container, use the following command:

```bash
docker rm  gridweb-demo-container
```

### Removing a Image
To remove an image, use the following command:

```bash
docker rmi gridweb-demo-java
```




