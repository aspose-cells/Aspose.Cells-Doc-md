---
title: come eseguire Aspose.Cells.GridWeb per costruire un applicazione editor o visualizzatore di fogli online in docker
type: docs
weight: 250
url: /it/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Questo articolo introduce come eseguire GridWeb in docker per costruire un editor o visualizzatore di Excel online.
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

# Guida a Docker

## Prerequisiti

Assicurati di avere Docker installato sul tuo computer. Puoi scaricare e installare Docker dal [sito web ufficiale di Docker](https://www.docker.com/get-started).

## Passaggio 1: Crea un Dockerfile

Crea un file chiamato `Dockerfile` nel tuo progetto [directory](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). Il `Dockerfile` dovrebbe contenere istruzioni su come costruire la tua immagine Docker.

## Passo 2: Scrivi Dockerfile per GridWeb

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) per la demo di GridWeb con un'applicazione Java:

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
Crea l'immagine Docker: Dal terminale, esegui il seguente comando per creare la tua immagine Docker:
```bash
docker build -t gridweb-demo-java .
```
puoi sostituire gridweb-demo-java con il nome che desideri dare alla tua immagine Docker.

## Passo 4: Esecuzione di un Container Docker
Una volta che l'immagine è stata creata, puoi eseguire un container utilizzando il seguente comando:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Spiegazione delle Opzioni del Comando Docker Run
-d: Esegui il container in modalità distaccata (in background).
-p 8080:8080: Mappa la porta 8080 nel container alla porta 8080 sulla macchina host.
--name gridweb-demo-container: Assegna un nome al container.

## Passo 5: Verifica che il Container stia Eseguendo
Per verificare se il tuo container è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i container in esecuzione. Dovresti vedere il tuo container elencato insieme al suo nome e stato.

## Passo 6: Accedi all'Applicazione Web

Apri un browser web e vai a `http://localhost:8080/gridwebdemo/index`. Dovresti vedere la tua applicazione in esecuzione.



## Comandi Aggiuntivi

### Arresto del Container

Per arrestare un container in esecuzione, utilizza il seguente comando:

```bash
docker stop gridweb-demo-container
```

### Rimozione di un contenitore
Per rimuovere un contenitore inattivo, utilizzare il seguente comando:

```bash
docker rm  gridweb-demo-container
```

### Rimozione di un'immagine
Per rimuovere un'immagine, utilizzare il seguente comando:

```bash
docker rmi gridweb-demo-java
```




