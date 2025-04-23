---
title: hur man kör Aspose.Cells.GridJs i docker
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Den här artikeln introducerar hur man kör GridJs i docker för att bygga en online Excel redigerare eller visningsapplikation.
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

# Docker Guide

## Förutsättningar

Se till att du har Docker installerat på din maskin. Du kan ladda ner och installera Docker från [officiella Docker-webbplatsen](https://www.docker.com/get-started).

## Steg 1: Skapa en Dockerfile

Skapa en fil som heter `Dockerfile` i ditt projekt [katalog](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/). `Dockerfile` ska innehålla instruktioner för hur du bygger din Docker-bild.

## Steg 2: Skriv Dockerfile för GridJs

Här är ett exempel [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Dockerfile) för GridJs-demo med ASP.NET Core-applikation:

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
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Steg 3: Bygga Docker-bilden
Bygg Docker-bilden: Från terminalen, kör följande kommando för att bygga din Docker-bild:
```bash
docker build -t gridjs-demo-net6 .
```
du kan ersätta gridjs-demo-net6 med det namn du vill ge din Docker-bild.

## Steg 4: Kör en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

eller bara köra demonstrationen i provläget:


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Förklaring av Docker Run-kommandots alternativ
-d: Kör containern i bakgrunden (avskilt läge).
-p 24262:80: Mappar port 80 i containern till port 24262 på värddatorn.
-v C:/path/till/license.txt:/app/license:  Mappar licensfilens sökväg på värddatorn till filens sökväg i containern.
--name gridjs-demo-container: Tilldela ett namn till containern.

## Steg 5: Kontrollera att containern körs
För att kontrollera att din container är igång, använd följande kommando:

```bash
docker ps
```
Detta listas alla aktiva containrar. Du bör se din container listad med namn och status.

## Steg 6: Åtkomst till webbapplikationen

Öppna en webbläsare och gå till `http://localhost:24262/GridJs2/List`. Du bör se din applikation igång.

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
docker rmi gridjs-demo-net6
```




