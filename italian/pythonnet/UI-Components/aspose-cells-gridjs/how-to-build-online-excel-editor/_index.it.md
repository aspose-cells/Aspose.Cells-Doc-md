---
title: come eseguire Aspose.Cells.GridJs in docker
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Questo articolo introduce come eseguire GridJs in docker per creare un applicazione di editor o visualizzatore Excel online.
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

# Guida Docker

## Prerequisiti

Assicurati di aver installato Docker sul tuo computer. Puoi scaricare e installare Docker dal [sito ufficiale di Docker](https://www.docker.com/get-started).

## Passo 1: Creare un Dockerfile

Crea un file denominato `Dockerfile` nella directory del tuo progetto [directory](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/). Il `Dockerfile` dovrebbe contenere istruzioni su come costruire la tua immagine Docker.

## Passo 2: Scrivere Dockerfile per GridJs

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/Dockerfile) per la demo di GridJs con applicazione Python:

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

## Passo 3: Creazione dell'immagine Docker
Costruisci l'immagine Docker: dal terminale, esegui il comando seguente per creare la tua immagine Docker:
```bash
docker build -t gridjs-demo-python .
```
Puoi sostituire gridjs-demo-python con il nome che desideri assegnare alla tua immagine Docker.

## Passo 4: Esecuzione di un contenitore Docker
Una volta che l’immagine è stata creata, puoi avviare un contenitore usando il comando seguente:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

o semplicemente eseguire la demo in modalità prova:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Spiegazione delle opzioni del comando Docker Run
-d: Eseguire il contenitore in modalità distaccata (in background).
-p 2022:2022: Mappare la porta 2022 nel contenitore alla porta 2022 sulla macchina host.
-v C:/path/to/license.txt:/app/license: Mappare il percorso del file licenza sulla macchina host al percorso del file nel contenitore.
--name gridjs-demo-container: Assegna un nome al contenitore.

## Passo 5: Verificare che il contenitore sia in esecuzione
Per verificare se il tuo contenitore è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i contenitori in esecuzione. Dovresti vedere il tuo contenitore elencato con il suo nome e stato.

## Passo 6: Accesso all'applicazione web

Apri un browser e vai su `http://localhost:2022`. Dovresti vedere la tua applicazione in esecuzione.

## Comandi aggiuntivi

### Arresto del contenitore

Per arrestare un contenitore in esecuzione, utilizza il seguente comando:

```bash
docker stop gridjs-demo-container
```

### Rimozione di un contenitore
Per rimuovere un contenitore fermo, utilizza il seguente comando:

```bash
docker rm  gridjs-demo-container
```

### Rimozione di un'immagine
Per rimuovere un'immagine, utilizza il seguente comando:

```bash
docker rmi gridjs-demo-python
```




