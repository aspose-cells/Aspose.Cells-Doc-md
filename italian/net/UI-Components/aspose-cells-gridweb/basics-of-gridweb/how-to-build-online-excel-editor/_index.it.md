---
title: come eseguire Aspose.Cells.GridWeb in docker
type: docs
weight: 250
url: /it/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb,docker
description: Questo articolo introduce come eseguire GridWeb in docker per creare un applicazione di modifica o visualizzazione di Excel online.
aliases:
  - /net/aspose-cells-gridweb/docker/
  - /net/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /net/aspose-cells-gridweb/run-gridweb-in-docker/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Guida a Docker

## Prerequisiti

Assicurati di avere Docker installato sul tuo computer. Puoi scaricare e installare Docker dal [sito web ufficiale di Docker](https://www.docker.com/get-started).

## Passaggio 1: Crea un Dockerfile

Crea un file chiamato `Dockerfile` nella tua [directory](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/). Il `Dockerfile` dovrebbe contenere istruzioni su come creare l'immagine Docker.

## Passo 2: Scrivere il Dockerfile per GridWeb

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile) per la demo di GridWeb con l'applicazione ASP.NET Core:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["GridWeb.Demo.NET6.0.csproj", "."]
RUN dotnet restore "./GridWeb.Demo.NET6.0.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/publish

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
# the cache file path for GridWeb
RUN mkdir -p /app/filecache
# the cache picture path for GridWeb
RUN mkdir -p /app/piccache
COPY wwwroot/wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "GridWeb.Demo.NET6.0.dll"]
```

## Passo 3: Creazione dell'immagine Docker
Crea l'immagine Docker: Dal terminale, esegui il seguente comando per creare la tua immagine Docker:
```bash
docker build -t gridweb-demo-net6 .
```
puoi sostituire gridweb-demo-net6 con il nome che vuoi dare alla tua immagine Docker.

## Passo 4: Esecuzione di un Container Docker
Una volta che l'immagine è stata creata, puoi eseguire un container utilizzando il seguente comando:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Spiegazione delle Opzioni del Comando Docker Run
-d: Esegui il container in modalità distaccata (in background).
-p 24262:80: Associa la porta 80 del container alla porta 24262 sulla macchina host.
--name gridweb-demo-container: Assegna un nome al container.

## Passo 5: Verifica che il Container stia Eseguendo
Per verificare se il tuo container è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i container in esecuzione. Dovresti vedere il tuo container elencato insieme al suo nome e stato.

## Passo 6: Accedi all'Applicazione Web

Apri un browser web e vai su `http://localhost:24262/`. Dovresti vedere la tua applicazione in esecuzione.

vedrai la guida generale allo sviluppo per GridWeb 

clicca su [demo](http://localhost:24262/grid/index1 "demo") nella pagina, puoi eseguire operazioni di modifica per il file del foglio di calcolo.

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
docker rmi gridweb-demo-net6
```




