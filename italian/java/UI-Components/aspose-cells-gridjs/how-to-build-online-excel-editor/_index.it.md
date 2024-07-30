---
title: come eseguire Aspose.Cells.GridJs in docker
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Questo articolo introduce come eseguire GridJs in docker per creare un applicazione online per la modifica o la visualizzazione di fogli Excel.
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

# Guida a Docker

## Prerequisiti

Assicurati di avere Docker installato sul tuo computer. Puoi scaricare e installare Docker dal [sito web ufficiale di Docker](https://www.docker.com/get-started).

## Passaggio 1: Crea un Dockerfile

Crea un file chiamato `Dockerfile` nella tua [directory](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs) di progetto. Il `Dockerfile` dovrebbe contenere istruzioni su come creare la tua immagine Docker.

## Passo 2: Scrivi il Dockerfile per GridJs

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) per la demo di GridJs con applicazione java:

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

## Passo 3: Creazione dell'immagine Docker
Crea l'immagine Docker: Dal terminale, esegui il seguente comando per creare la tua immagine Docker:
```bash
docker build -t gridjs-demo-java .
```
puoi sostituire gridjs-demo-java con il nome che desideri dare alla tua immagine Docker.

## Passo 4: Esecuzione di un Container Docker
Una volta che l'immagine è stata creata, puoi eseguire un container utilizzando il seguente comando:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Spiegazione delle Opzioni del Comando Docker Run
-d: Esegui il container in modalità distaccata (in background).
-p 8080:80: Mappa la porta 80 del container alla porta 8080 sulla macchina host.
--name gridjs-demo-container: Assegna un nome al container.

## Passo 5: Verifica che il Container stia Eseguendo
Per verificare se il tuo container è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i container in esecuzione. Dovresti vedere il tuo container elencato insieme al suo nome e stato.

## Passo 6: Accedi all'Applicazione Web

Apri un browser web e vai a `http://localhost:8080/gridjsdemo/index`. Dovresti vedere la tua applicazione in esecuzione.

## Comandi Aggiuntivi

### Arresto del Container

Per arrestare un container in esecuzione, utilizza il seguente comando:

```bash
docker stop gridjs-demo-container
```

### Rimozione di un contenitore
Per rimuovere un contenitore inattivo, utilizzare il seguente comando:

```bash
docker rm  gridjs-demo-container
```

### Rimozione di un'immagine
Per rimuovere un'immagine, utilizzare il seguente comando:

```bash
docker rmi gridjs-demo-java
```




