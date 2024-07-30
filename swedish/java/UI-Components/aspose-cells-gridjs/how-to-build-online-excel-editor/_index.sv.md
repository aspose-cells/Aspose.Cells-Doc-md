---
title: Hur man kör Aspose.Cells.GridJs i docker
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Den här artikeln introducerar hur man kör GridJs i docker för att bygga en online Excel editor eller visningsapplikation.
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

## Steg 1: Skapa en Dockerfil

Skapa en fil med namnet `Dockerfile` i din projektmapp [directory](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). `Dockerfilen` ska innehålla instruktioner om hur man bygger din Dockerbild.

## Steg 2: Skriv Dockerfile för GridJs

Här är en exempel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) för GridJs-demo med javaapplikation:

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

## Steg 3: Bygga Docker-image
Bygg Docker-image: Från terminalen, kör följande kommando för att bygga din Docker-image:
```bash
docker build -t gridjs-demo-java .
```
du kan byta ut gridjs-demo-java med namnet du vill ge din Dockerbild.

## Steg 4: Köra en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Förklaring av Docker Run-kommandoalternativ
-d: Kör containern i detach-läge (i bakgrunden).
-p 8080:80: Kartlägg port 80 i containern till port 8080 på värdmaskinen.
--name gridjs-demo-container: Tilldela ett namn till containern.

## Steg 5: Verifiera att containern körs
För att kontrollera om din container körs, använd följande kommando:

```bash
docker ps
```
Detta kommer att lista alla körande containrar. Du bör se din container listad tillsammans med dess namn och status.

## Steg 6: Kom åt webbapplikationen

Öppna en webbläsare och gå till `http://localhost:8080/gridjsdemo/index`. Du bör se din applikation köra.

## Ytterligare kommandon

### Stoppa containern

För att stoppa en körande container, använd följande kommando:

```bash
docker stop gridjs-demo-container
```

### Ta bort en behållare
För att ta bort en stoppad behållare, använd följande kommando:

```bash
docker rm  gridjs-demo-container
```

### Ta bort en bild
För att ta bort en bild, använd följande kommando:

```bash
docker rmi gridjs-demo-java
```




