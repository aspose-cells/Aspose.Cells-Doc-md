---
title: comment exécuter Aspose.Cells.GridJs dans un docker
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Cet article présente comment exécuter GridJs dans un docker pour créer une application d éditeur ou de visualiseur Excel en ligne.
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

# Guide Docker

## Prérequis

Assurez-vous d'avoir Docker installé sur votre machine. Vous pouvez télécharger et installer Docker depuis le [site officiel de Docker](https://www.docker.com/get-started).

## Étape 1 : Créer un Dockerfile

Créez un fichier nommé `Dockerfile` dans votre [répertoire](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs). Le `Dockerfile` doit contenir les instructions sur la façon de construire votre image Docker.

## Étape 2 : Écrire le Dockerfile pour GridJs

Voici un exemple de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) pour la démo GridJs avec application Python :

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

## Étape 3 : Construction de l'image Docker
Construire l'image Docker : Depuis le terminal, exécutez la commande suivante pour construire votre image Docker :
```bash
docker build -t gridjs-demo-python .
```
vous pouvez remplacer gridjs-demo-python par le nom que vous souhaitez donner à votre image Docker.

## Étape 4 : Exécution d'un conteneur Docker
Une fois l'image construite, vous pouvez exécuter un conteneur à l'aide de la commande suivante :

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

ou simplement exécuter la démo en mode d'essai :


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Explication des options de la commande Docker Run
-d : Exécuter le conteneur en mode détaché (en arrière-plan).
-p 2022:2022 : Mapper le port 2022 dans le conteneur au port 2022 sur la machine hôte.
-v C:/path/to/license.txt:/app/license : Mapper le chemin du fichier de licence sur la machine hôte au chemin du fichier dans le conteneur.
--name gridjs-demo-container : Assigner un nom au conteneur.

## Étape 5 : Vérifier que le conteneur fonctionne
Pour vérifier si votre conteneur fonctionne, utilisez la commande suivante :

```bash
docker ps
```
Cela listera tous les conteneurs en cours d'exécution. Vous devriez voir votre conteneur avec son nom et son statut.

## Étape 6 : Accéder à l'application web

Ouvrez un navigateur web et rendez-vous sur `http://localhost:2022`. Vous devriez voir votre application en cours d'exécution.

## Commandes supplémentaires

### Arrêter le conteneur

Pour arrêter un conteneur en cours d'exécution, utilisez la commande suivante :

```bash
docker stop gridjs-demo-container
```

### Supprimer un conteneur
Pour supprimer un conteneur arrêté, utilisez la commande suivante :

```bash
docker rm  gridjs-demo-container
```

### Supprimer une image
Pour supprimer une image, utilisez la commande suivante :

```bash
docker rmi gridjs-demo-python
```




