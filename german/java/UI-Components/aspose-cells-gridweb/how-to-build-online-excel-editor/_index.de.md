---
title: wie man Aspose.Cells.GridWeb ausführt, um eine Online Tabellenkalkulationseditor oder Viewer Anwendung in Docker zu erstellen
type: docs
weight: 250
url: /de/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Dieser Artikel zeigt, wie man GridWeb in Docker ausführt, um einen Online Excel Editor oder Viewer zu erstellen.
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

# Docker-Leitfaden

## Voraussetzungen

Stellen Sie sicher, dass Sie Docker auf Ihrem Rechner installiert haben. Sie können Docker von der [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie ein Dockerfile

Erstellen Sie eine Datei mit dem Namen `Dockerfile` in Ihrem Projektverzeichnis (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). Der `Dockerfile` sollte Anweisungen enthalten, wie Ihr Docker-Image erstellt werden soll.

## Schritt 2: Schreiben des Dockerfiles für GridWeb

Hier ist ein Beispiel für eine [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) für das GridWeb-Demo mit einer Java-Anwendung:

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

## Schritt 3: Erstellen des Docker-Images
Bauen Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridweb-demo-java .
```
Sie können `gridweb-demo-java` durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Ausführen eines Docker-Containers
Nachdem das Image erstellt wurde, können Sie einen Container mit dem folgenden Befehl ausführen:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Erklärung der Optionen des Docker Run-Befehls
-d: Führen Sie den Container im Hintergrundmodus (getrennt) aus.
-p 8080:8080: Port 8080 im Container auf Port 8080 des Hostrechners mappen.
--name gridweb-demo-container: Einen Namen für den Container zuweisen.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container ausgeführt wird, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Hier werden alle laufenden Container aufgelistet. Sie sollten Ihren Container zusammen mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:8080/gridwebdemo/index`. Sie sollten Ihre Anwendung in Betrieb sehen.



## Weitere Befehle

### Stoppen des Containers

Um einen laufenden Container zu stoppen, verwenden Sie den folgenden Befehl:

```bash
docker stop gridweb-demo-container
```

### Entfernen eines Containers
Um einen gestoppten Container zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rm  gridweb-demo-container
```

### Entfernen eines Bildes
Um ein Bild zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rmi gridweb-demo-java
```




