---
title: wie man Aspose.Cells.GridJs in Docker ausführt
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,Docker
description: In diesem Artikel wird erläutert, wie man GridJs in Docker ausführt, um eine Online Excel Editor oder Viewer Anwendung zu erstellen.
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
---

# Docker-Leitfaden

## Voraussetzungen

Stellen Sie sicher, dass Sie Docker auf Ihrem Rechner installiert haben. Sie können Docker von der [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie ein Dockerfile

Erstellen Sie eine Datei mit dem Namen `Dockerfile` in Ihrem Projekt [Verzeichnis](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/). Der `Dockerfile` sollte Anweisungen enthalten, wie Ihr Docker-Image erstellt werden soll.

## Schritt 2: Schreiben Sie Dockerfile für GridJs

Hier finden Sie ein Beispiel für [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Dockerfile) für das GridJs-Demo mit einer ASP.NET Core-Anwendung:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
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
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Schritt 3: Erstellen des Docker-Images
Bauen Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridjs-demo-net6 .
```
Sie können gridjs-demo-net6 durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Ausführen eines Docker-Containers
Nachdem das Image erstellt wurde, können Sie einen Container mit dem folgenden Befehl ausführen:

```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```
Erklärung der Optionen des Docker Run-Befehls
-d: Führen Sie den Container im Hintergrundmodus (getrennt) aus.
-p 24262:80: Ordnen Sie Port 80 im Container Port 24262 an der Hostmaschine zu.
--name gridjs-demo-container: Weisen Sie dem Container einen Namen zu.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container ausgeführt wird, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Hier werden alle laufenden Container aufgelistet. Sie sollten Ihren Container zusammen mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:24262/GridJs2/List`. Sie sollten Ihre Anwendung in Betrieb sehen.

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
docker rmi gridjs-demo-net6
```




