---
title: come eseguire Aspose.Cells.GridWeb in Docker
type: docs
weight: 250
url: /it/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, Docker
description: Questo articolo introduce come eseguire GridWeb in Docker per creare un applicazione di editor o visualizzatore Excel online.
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

# Guida Docker

## Prerequisiti

Assicurati di aver installato Docker sul tuo computer. Puoi scaricare e installare Docker dal [sito ufficiale di Docker](https://www.docker.com/get-started).

## Passo 1: Creare un Dockerfile

 Crea un file chiamato `Dockerfile` nella [directory](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/) del tuo progetto. Il `Dockerfile` dovrebbe contenere le istruzioni su come costruire la tua immagine Docker.

## Passo 2: Scrivi Dockerfile per GridWeb

Ecco un esempio di [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile) per la demo di GridWeb con applicazione ASP.NET Core:

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
Costruisci l'immagine Docker: dal terminale, esegui il comando seguente per creare la tua immagine Docker:
```bash
docker build -t gridweb-demo-net6 .
```
Puoi sostituire gridweb-demo-net6 con il nome che desideri dare alla tua immagine Docker.

## Passo 4: Esecuzione di un contenitore Docker
Una volta che l’immagine è stata creata, puoi avviare un contenitore usando il comando seguente:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Spiegazione delle opzioni del comando Docker Run
-d: Eseguire il contenitore in modalità distaccata (in background).
-p 24262:80: Mappa la porta 80 nel contenitore alla porta 24262 sulla macchina host.
--name gridweb-demo-container: Assegna un nome al contenitore.

## Passo 5: Verificare che il contenitore sia in esecuzione
Per verificare se il tuo contenitore è in esecuzione, utilizza il seguente comando:

```bash
docker ps
```
Questo elencherà tutti i contenitori in esecuzione. Dovresti vedere il tuo contenitore elencato con il suo nome e stato.

## Passo 6: Accesso all'applicazione web

Apri un browser web e vai a `http://localhost:24262/`. Dovresti vedere la tua applicazione in esecuzione.

vedrai la guida generale di sviluppo per GridWeb 

clicca [demo](http://localhost:24262/grid/index1 "demo") nella pagina, puoi eseguire operazioni di modifica sul file di foglio di calcolo.

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
docker rmi gridweb-demo-net6
```




