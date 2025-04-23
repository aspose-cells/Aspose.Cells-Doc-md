---
title: So führen Sie Aspose.Cells.GridWeb aus, um einen Online Tabellenkalkulations Editor oder Viewer in Docker zu erstellen
type: docs
weight: 250
url: /de/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, Docker
description: Dieser Artikel führt ein, wie man GridWeb in Docker ausführt, um eine Online Excel Editor oder Viewer Anwendung zu erstellen.
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

# Docker Anleitung

## Voraussetzungen

Stellen Sie sicher, dass Docker auf Ihrem Rechner installiert ist. Sie können Docker vom [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie eine Dockerfile

Erstellen Sie eine Datei namens `Dockerfile` in Ihrem Projekt [Verzeichnis](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). Das `Dockerfile` sollte Anweisungen enthalten, wie Ihr Docker-Image gebaut wird.

Schritt 2: Schreiben Sie eine Dockerfile für GridWeb

Hier ist ein Beispiel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) für GridWeb-Demo mit Java-Anwendung:

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

## Schritt 3: Das Docker-Image erstellen
Builden Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridweb-demo-java .
```
Sie können `gridweb-demo-java` durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Einen Docker-Container ausführen
Sobald das Image erstellt ist, können Sie einen Container mit dem folgenden Befehl starten:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Erläuterung der Docker-Run-Befehlsoptionen
-d: Den Container im Detached-Modus (im Hintergrund) starten.
-p 8080:8080: Karte Port 8080 im Container an Port 8080 auf der Hostmaschine.
--name gridweb-demo-container: Weisen Sie dem Container einen Namen zu.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container läuft, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Dies listet alle laufenden Container auf. Sie sollten Ihren Container mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:8080/gridwebdemo/index`. Sie sollten Ihre Anwendung laufen sehen.



## Zusätzliche Befehle

### Container stoppen

Um einen laufenden Container zu stoppen, verwenden Sie den folgenden Befehl:

```bash
docker stop gridweb-demo-container
```

### Einen Container entfernen
Um einen gestoppten Container zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rm  gridweb-demo-container
```

### Ein Image entfernen
Um ein Image zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rmi gridweb-demo-java
```




