---
title: So läuft Aspose.Cells.GridJs in Docker
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: Dieser Artikel beschreibt, wie man GridJs in Docker ausführt, um einen Online Excel Editor oder Viewer zu erstellen.
aliases:
  - /python-net/aspose-cells-gridjs/docker/
  - /python-net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Docker Anleitung

## Voraussetzungen

Stellen Sie sicher, dass Docker auf Ihrem Rechner installiert ist. Sie können Docker vom [offiziellen Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Schritt 1: Erstellen Sie eine Dockerfile

Erstellen Sie in Ihrem Projektordner eine Datei namens `Dockerfile`. Das `Dockerfile` sollte Anweisungen enthalten, wie Sie Ihr Docker-Image bauen.

## Schritt 2: Schreiben Sie die Dockerfile für GridJs

Hier ist ein Beispiel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) für die GridJs-Demo mit Python-Anwendung:

```dockerfile
# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
	fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  

# copy all to  /app  
COPY . /app  


RUN pip install --no-cache-dir -r requirements.txt  
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/



# start cmd
CMD [ "python", "./main.py" ]
```

## Schritt 3: Das Docker-Image erstellen
Builden Sie das Docker-Image: Führen Sie im Terminal den folgenden Befehl aus, um Ihr Docker-Image zu erstellen:
```bash
docker build -t gridjs-demo-python .
```
Sie können gridjs-demo-python durch den Namen ersetzen, den Sie Ihrem Docker-Image geben möchten.

## Schritt 4: Einen Docker-Container ausführen
Sobald das Image erstellt ist, können Sie einen Container mit dem folgenden Befehl starten:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

Oder führen Sie die Demo einfach im Probemodus aus:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Erläuterung der Docker-Run-Befehlsoptionen
-d: Den Container im Detached-Modus (im Hintergrund) starten.
-p 2022:2022: Den Port 2022 im Container auf Port 2022 des Host-Rechners abbilden.
-v C:/path/to/license.txt:/app/license: Pfad zur Lizenzdatei auf dem Host-Rechner auf den Dateipfad im Container abbilden.
--name gridjs-demo-container: Einen Namen für den Container vergeben.

## Schritt 5: Überprüfen, ob der Container läuft
Um zu überprüfen, ob Ihr Container läuft, verwenden Sie den folgenden Befehl:

```bash
docker ps
```
Dies listet alle laufenden Container auf. Sie sollten Ihren Container mit seinem Namen und Status sehen.

## Schritt 6: Zugriff auf die Webanwendung

Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:2022`. Sie sollten Ihre Anwendung laufen sehen.

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
docker rmi gridjs-demo-python
```




