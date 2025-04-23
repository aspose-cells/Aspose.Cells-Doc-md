---
title: comment exécuter Aspose.Cells.GridWeb dans Docker
type: docs
weight: 250
url: /fr/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Cet article présente comment exécuter GridWeb dans Docker pour construire une application d éditeur ou de visualisation Excel en ligne.
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

# Guide Docker

## Prérequis

Assurez-vous d'avoir Docker installé sur votre machine. Vous pouvez télécharger et installer Docker depuis le [site officiel de Docker](https://www.docker.com/get-started).

## Étape 1 : Créer un Dockerfile

Créez un fichier nommé `Dockerfile` dans votre [répertoire](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/). Le `Dockerfile` doit contenir des instructions sur la façon de construire votre image Docker.

## Étape 2 : Écrire Dockerfile pour GridWeb

Voici un exemple de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile) pour la démo GridWeb avec une application ASP.NET Core :

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

## Étape 3 : Construction de l'image Docker
Construire l'image Docker : Depuis le terminal, exécutez la commande suivante pour construire votre image Docker :
```bash
docker build -t gridweb-demo-net6 .
```
vous pouvez remplacer gridweb-demo-net6 par le nom que vous souhaitez donner à votre image Docker.

## Étape 4 : Exécution d'un conteneur Docker
Une fois l'image construite, vous pouvez exécuter un conteneur à l'aide de la commande suivante :

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Explication des options de la commande Docker Run
-d : Exécuter le conteneur en mode détaché (en arrière-plan).
-p 24262:80 : Mapper le port 80 du conteneur au port 24262 sur la machine hôte.
--name gridweb-demo-container : Assigner un nom au conteneur.

## Étape 5 : Vérifier que le conteneur fonctionne
Pour vérifier si votre conteneur fonctionne, utilisez la commande suivante :

```bash
docker ps
```
Cela listera tous les conteneurs en cours d'exécution. Vous devriez voir votre conteneur avec son nom et son statut.

## Étape 6 : Accéder à l'application web

Ouvrez un navigateur web et allez à `http://localhost:24262/`. Vous devriez voir votre application en cours d'exécution.

vous verrez le guide général de développement pour GridWeb 

cliquez sur [demo](http://localhost:24262/grid/index1 "demo") sur la page, vous pouvez effectuer une opération d'édition pour le fichier de feuille de calcul.

## Commandes supplémentaires

### Arrêter le conteneur

Pour arrêter un conteneur en cours d'exécution, utilisez la commande suivante :

```bash
docker stop gridweb-demo-container
```

### Supprimer un conteneur
Pour supprimer un conteneur arrêté, utilisez la commande suivante :

```bash
docker rm  gridweb-demo-container
```

### Supprimer une image
Pour supprimer une image, utilisez la commande suivante :

```bash
docker rmi gridweb-demo-net6
```




