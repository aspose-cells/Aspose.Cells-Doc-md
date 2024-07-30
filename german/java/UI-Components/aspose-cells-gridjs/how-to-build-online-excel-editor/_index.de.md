---
title: wie man Aspose.Cells.GridJs in Docker ausführt
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,Docker
description: In diesem Artikel wird erläutert, wie man GridJs in Docker ausführt, um eine Online Excel Editor oder Viewer Anwendung zu erstellen.
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

# Docker-Leitfaden

## Voraussetzungen

Stellen Sie sicher, dass Sie Docker auf Ihrem Rechner installiert haben. Sie können Docker von der [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie ein Dockerfile

Erstellen Sie eine Datei mit dem Namen `Dockerfile` in Ihrem Projekt [Verzeichnis](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). Das `Dockerfile` sollte Anweisungen enthalten, wie Ihr Docker-Image erstellt wird.

## Schritt 2: Schreiben Sie Dockerfile für GridJs

Hier ist ein Beispiels-`Dockerfile` (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) für das GridJs-Demo mit einer Java-Anwendung:

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

## Schritt 3: Erstellen des Docker-Images
Bauen Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridjs-demo-java .
```
Sie können `gridjs-demo-java` durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Ausführen eines Docker-Containers
Nachdem das Image erstellt wurde, können Sie einen Container mit dem folgenden Befehl ausführen:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Erklärung der Optionen des Docker Run-Befehls
-d: Führen Sie den Container im Hintergrundmodus (getrennt) aus.
-p 8080:80: Weisen Sie Port 80 im Container Port 8080 auf dem Host-Rechner zu.
--name gridjs-demo-container: Weisen Sie dem Container einen Namen zu.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container ausgeführt wird, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Hier werden alle laufenden Container aufgelistet. Sie sollten Ihren Container zusammen mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu ` http://localhost:8080/gridjsdemo/index`. Sie sollten Ihre Anwendung sehen, die läuft.

## Weitere Befehle

### Stoppen des Containers

Um einen laufenden Container zu stoppen, verwenden Sie den folgenden Befehl:

```bash
docker stop gridjs-demo-container
```

### Entfernen eines Containers
Um einen gestoppten Container zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rm  gridjs-demo-container
```

### Entfernen eines Bildes
Um ein Bild zu entfernen, verwenden Sie den folgenden Befehl:

```bash
docker rmi gridjs-demo-java
```




