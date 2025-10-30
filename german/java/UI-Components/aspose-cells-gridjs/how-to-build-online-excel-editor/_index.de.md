---
title: So läuft Aspose.Cells.GridJs in Docker
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: Dieser Artikel beschreibt, wie man GridJs in Docker ausführt, um einen Online Excel Editor oder Viewer zu erstellen.
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

# Docker Anleitung

## Voraussetzungen

Stellen Sie sicher, dass Docker auf Ihrem Rechner installiert ist. Sie können Docker vom [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie eine Dockerfile

Erstellen Sie eine Datei namens `Dockerfile` in Ihrem Projekt [Verzeichnis](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs). Das `Dockerfile` sollte Anweisungen enthalten, wie Ihr Docker-Image gebaut wird.

## Schritt 2: Schreiben Sie die Dockerfile für GridJs

Hier ist ein Beispiel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs/Dockerfile) für die GridJs-Demo mit Java-Anwendung:

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

## Schritt 3: Das Docker-Image erstellen
Builden Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridjs-demo-java .
```
Sie können `gridjs-demo-java` durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Einen Docker-Container ausführen
Sobald das Image erstellt ist, können Sie einen Container mit dem folgenden Befehl starten:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

Oder führen Sie die Demo einfach im Probemodus aus:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Erläuterung der Docker-Run-Befehlsoptionen
-d: Den Container im Detached-Modus (im Hintergrund) starten.
-p 8080:80: Karte Port 80 im Container an Port 8080 auf der Hostmaschine.
-v C:/path/to/license.txt:/app/license: Pfad zur Lizenzdatei auf dem Host-Rechner auf den Dateipfad im Container abbilden.
--name gridjs-demo-container: Einen Namen für den Container vergeben.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container läuft, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Dies listet alle laufenden Container auf. Sie sollten Ihren Container mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:8080/gridjsdemo/index`. Sie sollten Ihre Anwendung laufen sehen.

## Zusätzliche Befehle

### Container stoppen

Um einen laufenden Container zu stoppen, verwenden Sie den folgenden Befehl:

```bash
docker stop gridjs-demo-container
```

### Einen Container entfernen
Um einen gestoppten Container zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rm  gridjs-demo-container
```

### Ein Image entfernen
Um ein Image zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rmi gridjs-demo-java
```




