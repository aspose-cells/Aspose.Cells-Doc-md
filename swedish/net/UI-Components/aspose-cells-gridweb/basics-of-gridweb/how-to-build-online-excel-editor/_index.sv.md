---
title: hur man kör Aspose.Cells.GridWeb i docker
type: docs
weight: 250
url: /sv/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Denna artikel introducerar hur man kör GridWeb i docker för att bygga en online excel redigerare eller visningsapplikation.
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

# Docker Guide

## Förutsättningar

Se till att du har Docker installerat på din maskin. Du kan ladda ner och installera Docker från [officiella Docker-webbplatsen](https://www.docker.com/get-started).

## Steg 1: Skapa en Dockerfile

Skapa en fil med namnet `Dockerfile` i ditt projekt [katalog](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/). `Dockerfile` ska innehålla instruktioner om hur du bygger din Docker-image.

## Steg 2: Skriv Dockerfile för GridWeb

Här är ett exempel på [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridWeb/Dockerfile) för GridWeb-demo med ASP.NET Core-applikation:

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

## Steg 3: Bygga Docker-bilden
Bygg Docker-bilden: Från terminalen, kör följande kommando för att bygga din Docker-bild:
```bash
docker build -t gridweb-demo-net6 .
```
du kan ersätta gridweb-demo-net6 med det namn du vill ge din Docker-bild.

## Steg 4: Kör en Docker-container
När bilden är byggd kan du köra en container med följande kommando:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Förklaring av Docker Run-kommandots alternativ
-d: Kör containern i bakgrunden (avskilt läge).
-p 24262:80: Mappar port 80 i containern till port 24262 på värddatorn.
--name gridweb-demo-container: Tilldela ett namn till containern.

## Steg 5: Kontrollera att containern körs
För att kontrollera att din container är igång, använd följande kommando:

```bash
docker ps
```
Detta listas alla aktiva containrar. Du bör se din container listad med namn och status.

## Steg 6: Åtkomst till webbapplikationen

Öppna en webbläsare och gå till `http://localhost:24262/`. Du bör se din applikation köras.

du kommer att se den generella utvecklingsguiden för GridWeb 

klicka på [demo](http://localhost:24262/grid/index1 "demo") på sidan, du kan utföra redigeringsoperationer för kalkylbladsfilen.

## Ytterligare Kommandon

### Stanna containern

För att stoppa en körande containter, använd följande kommando:

```bash
docker stop gridweb-demo-container
```

### Ta bort en container
För att ta bort en stoppad container, använd följande kommando:

```bash
docker rm  gridweb-demo-container
```

### Ta bort en bild
För att ta bort en bild, använd följande kommando:

```bash
docker rmi gridweb-demo-net6
```




