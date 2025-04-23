---
title: come eseguire Aspose.Cells.GridWeb per costruire un editor o visualizzatore di fogli di calcolo online in docker
type: docs
weight: 250
url: /it/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, Docker
description: Questo articolo introduce come eseguire GridWeb in Docker per creare un applicazione di editor o visualizzatore Excel online.
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

# Guida Docker

## Prerequisiti

Assicurati di aver installato Docker sul tuo computer. Puoi scaricare e installare Docker dal [sito ufficiale di Docker](https://www.docker.com/get-started).

## Passo 1: Creare un Dockerfile

Crea un file chiamato `Dockerfile` nella [directory](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/) del tuo progetto. Il `Dockerfile` dovrebbe contenere le istruzioni su come creare l'immagine Docker.

## Passo 2: Scrivi Dockerfile per GridWeb

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) per demo di GridWeb con applicazione Java:

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

## Passo 3: Creazione dell'immagine Docker
Costruisci l'immagine Docker: dal terminale, esegui il comando seguente per creare la tua immagine Docker:
```bash
docker build -t gridweb-demo-java .
```
puoi sostituire gridweb-demo-java con il nome che vuoi dare alla tua immagine Docker.

## Passo 4: Esecuzione di un contenitore Docker
Una volta che l’immagine è stata creata, puoi avviare un contenitore usando il comando seguente:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Spiegazione delle opzioni del comando Docker Run
-d: Eseguire il contenitore in modalità distaccata (in background).
-p 8080:8080: Mappa la porta 8080 nel contenitore alla porta 8080 sulla macchina host.
--name gridweb-demo-container: Assegna un nome al contenitore.

## Passo 5: Verificare che il contenitore sia in esecuzione
Per verificare se il tuo contenitore è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i contenitori in esecuzione. Dovresti vedere il tuo contenitore elencato con il suo nome e stato.

## Passo 6: Accesso all'applicazione web

Apri un browser web e vai su `http://localhost:8080/gridwebdemo/index`. Dovresti vedere l'applicazione in esecuzione.



## Comandi aggiuntivi

### Arresto del contenitore

Per arrestare un contenitore in esecuzione, utilizza il seguente comando:

```bash
docker stop gridweb-demo-container
```

### Rimozione di un contenitore
Per rimuovere un contenitore fermo, utilizza il seguente comando:

```bash
docker rm  gridweb-demo-container
```

### Rimozione di un'immagine
Per rimuovere un'immagine, utilizza il seguente comando:

```bash
docker rmi gridweb-demo-java
```




