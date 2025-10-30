---
title: come eseguire Aspose.Cells.GridJs in docker
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Questo articolo introduce come eseguire GridJs in docker per creare un applicazione di editor o visualizzatore Excel online.
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

# Guida Docker

## Prerequisiti

Assicurati di aver installato Docker sul tuo computer. Puoi scaricare e installare Docker dal [sito ufficiale di Docker](https://www.docker.com/get-started).

## Passo 1: Creare un Dockerfile

Crea un file chiamato `Dockerfile` nella [directory](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs) del tuo progetto. Il `Dockerfile` dovrebbe contenere le istruzioni su come costruire la tua immagine Docker.

## Passo 2: Scrivere Dockerfile per GridJs

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs/Dockerfile) per la demo GridJs con applicazione Java:

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

## Passo 3: Creazione dell'immagine Docker
Costruisci l'immagine Docker: dal terminale, esegui il comando seguente per creare la tua immagine Docker:
```bash
docker build -t gridjs-demo-java .
```
Puoi sostituire gridjs-demo-java con il nome che vuoi dare alla tua immagine Docker.

## Passo 4: Esecuzione di un contenitore Docker
Una volta che l’immagine è stata creata, puoi avviare un contenitore usando il comando seguente:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

o semplicemente eseguire la demo in modalità prova:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Spiegazione delle opzioni del comando Docker Run
-d: Eseguire il contenitore in modalità distaccata (in background).
-p 8080:80: Mappa la porta 80 nel container alla porta 8080 sulla macchina host.
-v C:/path/to/license.txt:/app/license: Mappare il percorso del file licenza sulla macchina host al percorso del file nel contenitore.
--name gridjs-demo-container: Assegna un nome al contenitore.

## Passo 5: Verificare che il contenitore sia in esecuzione
Per verificare se il tuo contenitore è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i contenitori in esecuzione. Dovresti vedere il tuo contenitore elencato con il suo nome e stato.

## Passo 6: Accesso all'applicazione web

Apri un browser e vai su `http://localhost:8080/gridjsdemo/index`. Dovresti vedere la tua applicazione in esecuzione.

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
docker rmi gridjs-demo-java
```




