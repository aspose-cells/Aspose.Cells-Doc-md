---
title: hur man kör Aspose.Cells.GridJs i docker
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Den här artikeln introducerar hur man kör GridJs i docker för att bygga en online Excel redigerare eller visningsapplikation.
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

# Docker Guide

## Förutsättningar

Se till att du har Docker installerat på din maskin. Du kan ladda ner och installera Docker från [officiella Docker-webbplatsen](https://www.docker.com/get-started).

## Steg 1: Skapa en Dockerfile

Skapa en fil som heter `Dockerfile` i din projekt [katalog](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). Dockerfilen bör innehålla instruktioner för hur man bygger din Docker-image.

## Steg 2: Skriv Dockerfile för GridJs

Här är ett exempel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) för GridJs-demo med Java-applikation:

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

## Steg 3: Bygga Docker-bilden
Bygg Docker-bilden: Från terminalen, kör följande kommando för att bygga din Docker-bild:
```bash
docker build -t gridjs-demo-java .
```
du kan ersätta gridjs-demo-java med det namn du vill ge din Docker-image.

## Steg 4: Kör en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

eller bara köra demonstrationen i provläget:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Förklaring av Docker Run-kommandots alternativ
-d: Kör containern i bakgrunden (avskilt läge).
-p 8080:80: Kartlägg port 80 i containern till port 8080 på värddatorn.
-v C:/path/till/license.txt:/app/license:  Mappar licensfilens sökväg på värddatorn till filens sökväg i containern.
--name gridjs-demo-container: Tilldela ett namn till containern.

## Steg 5: Kontrollera att containern körs
För att kontrollera att din container är igång, använd följande kommando:

```bash
docker ps
```
Detta listas alla aktiva containrar. Du bör se din container listad med namn och status.

## Steg 6: Åtkomst till webbapplikationen

Öppna en webbläsare och gå till `http://localhost:8080/gridjsdemo/index`. Du bör se din applikation köras.

## Ytterligare Kommandon

### Stanna containern

För att stoppa en körande containter, använd följande kommando:

```bash
docker stop gridjs-demo-container
```

### Ta bort en container
För att ta bort en stoppad container, använd följande kommando:

```bash
docker rm  gridjs-demo-container
```

### Ta bort en bild
För att ta bort en bild, använd följande kommando:

```bash
docker rmi gridjs-demo-java
```




