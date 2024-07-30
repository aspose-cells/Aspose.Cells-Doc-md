---
title: comment exécuter Aspose.Cells.GridJs dans docker
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Cet article présente comment exécuter GridJs dans docker pour créer une application d édition ou de visualisation de fichiers Excel en ligne.
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

# Guide Docker

## Prérequis

Assurez-vous d'avoir Docker installé sur votre machine. Vous pouvez télécharger et installer Docker depuis le [site officiel de Docker](https://www.docker.com/get-started).

## Étape 1: Créez un fichier Dockerfile

Créez un fichier nommé `Dockerfile` dans votre [répertoire] de projet (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). Le `Dockerfile` devrait contenir des instructions sur la façon de construire votre image Docker.

## Étape 2: Écrire Dockerfile pour GridJs

Voici un exemple de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) pour la démonstration de GridJs avec une application Java :

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

## Étape 3: Construction de l'image Docker
Construisez l'image Docker: Depuis le terminal, exécutez la commande suivante pour construire votre image Docker:
```bash
docker build -t gridjs-demo-java .
```
vous pouvez remplacer gridjs-demo-java par le nom que vous souhaitez donner à votre image Docker.

## Étape 4: Exécution d'un conteneur Docker
Une fois l'image construite, vous pouvez exécuter un conteneur en utilisant la commande suivante:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Explication des options de la commande Docker Run
-d: Exécute le conteneur en mode détaché (en arrière-plan).
-p 8080:80 : Mapper le port 80 dans le conteneur sur le port 8080 de la machine hôte.
--name gridjs-demo-container: Attribuez un nom au conteneur.

## Étape 5: Vérifier que le Conteneur fonctionne
Pour vérifier si votre conteneur fonctionne, utilisez la commande suivante:

```bash
docker ps
```
Cela listera tous les conteneurs en cours d'exécution. Vous devriez voir votre conteneur répertorié avec son nom et son statut.

## Étape 6: Accéder à l'application Web

Ouvrez un navigateur Web et allez à ` http://localhost:8080/gridjsdemo/index`. Vous devriez voir votre application en cours d'exécution.

## Commandes Additionnelles

### Arrêter le Conteneur

Pour arrêter un conteneur en cours d'exécution, utilisez la commande suivante:

```bash
docker stop gridjs-demo-container
```

### Suppression d'un conteneur
Pour supprimer un conteneur arrêté, utilisez la commande suivante :

```bash
docker rm  gridjs-demo-container
```

### Suppression d'une image
Pour supprimer une image, utilisez la commande suivante :

```bash
docker rmi gridjs-demo-java
```




