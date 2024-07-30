---
title: hur man kör Aspose.Cells.GridWeb för att bygga en online kalkylbladsredigerare eller tittarapplikation i docker
type: docs
weight: 250
url: /sv/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb,docker
description: Den här artikeln introducerar hur man kör GridWeb i docker för att bygga en onlineexcelredigerare eller tittarapplikation.
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
---

# Docker Guide

## Förutsättningar

Se till att du har Docker installerat på din maskin. Du kan ladda ner och installera Docker från [officiella Docker-webbplatsen](https://www.docker.com/get-started).

## Steg 1: Skapa en Dockerfil

Skapa en fil med namnet `Dockerfile` i ditt projekt [mapp](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). `Dockerfile` ska innehålla instruktioner om hur du bygger din Docker-image.

## Steg 2: Skriv Dockerfile för GridWeb

Här är ett exempel på [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) för GridWeb-demo med javapplikation:

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
# create [log dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## Steg 3: Bygga Docker-image
Bygg Docker-image: Från terminalen, kör följande kommando för att bygga din Docker-image:
```bash
docker build -t gridweb-demo-java .
```
du kan byta ut gridweb-demo-java med det namn du vill ge din Docker-image.

## Steg 4: Köra en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Förklaring av Docker Run-kommandoalternativ
-d: Kör containern i detach-läge (i bakgrunden).
-p 8080:8080: Kartlägg port 8080 i containern till port 8080 på värdmaskinen.
--name gridweb-demo-container: Tilldela ett namn till containern.

## Steg 5: Verifiera att containern körs
För att kontrollera om din container körs, använd följande kommando:

```bash
docker ps
```
Detta kommer att lista alla körande containrar. Du bör se din container listad tillsammans med dess namn och status.

## Steg 6: Kom åt webbapplikationen

Öppna en webbläsare och gå till `http://localhost:8080/gridwebdemo/index`. Du bör se din applikation köra.



## Ytterligare kommandon

### Stoppa containern

För att stoppa en körande container, använd följande kommando:

```bash
docker stop gridweb-demo-container
```

### Ta bort en behållare
För att ta bort en stoppad behållare, använd följande kommando:

```bash
docker rm  gridweb-demo-container
```

### Ta bort en bild
För att ta bort en bild, använd följande kommando:

```bash
docker rmi gridweb-demo-java
```




