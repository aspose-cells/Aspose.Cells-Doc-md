---
title: hur man kör Aspose.Cells.GridJs i docker
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Den här artikeln introducerar hur man kör GridJs i docker för att bygga en online Excel redigerare eller visningsapplikation.
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

# Docker Guide

## Förutsättningar

Se till att du har Docker installerat på din maskin. Du kan ladda ner och installera Docker från [officiella Docker-webbplatsen](https://www.docker.com/get-started).

## Steg 1: Skapa en Dockerfile

Skapa en fil som heter `Dockerfile` i ditt projekt [katalog](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs). `Dockerfile` ska innehålla instruktioner om hur du bygger din Docker-image.

## Steg 2: Skriv Dockerfile för GridJs

Här är ett exempel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) för GridJs-demo med Python-applikation:

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

## Steg 3: Bygga Docker-bilden
Bygg Docker-bilden: Från terminalen, kör följande kommando för att bygga din Docker-bild:
```bash
docker build -t gridjs-demo-python .
```
du kan ersätta gridjs-demo-python med det namn du vill ge din Docker-bild.

## Steg 4: Kör en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

eller bara köra demonstrationen i provläget:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Förklaring av Docker Run-kommandots alternativ
-d: Kör containern i bakgrunden (avskilt läge).
-p 2022:2022: Koppla port 2022 i containern till port 2022 på värdmaskinen.
-v C:/path/till/license.txt:/app/license:  Mappar licensfilens sökväg på värddatorn till filens sökväg i containern.
--name gridjs-demo-container: Tilldela ett namn till containern.

## Steg 5: Kontrollera att containern körs
För att kontrollera att din container är igång, använd följande kommando:

```bash
docker ps
```
Detta listas alla aktiva containrar. Du bör se din container listad med namn och status.

## Steg 6: Åtkomst till webbapplikationen

Öppna en webbläsare och gå till `http://localhost:2022`. Du bör se din applikation köras.

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
docker rmi gridjs-demo-python
```




