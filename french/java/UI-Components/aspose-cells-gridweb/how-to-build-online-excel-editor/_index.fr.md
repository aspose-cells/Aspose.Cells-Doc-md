---
title: Comment exécuter Aspose.Cells.GridWeb pour construire une application éditeur ou visualiseur de feuille de calcul en ligne dans Docker
type: docs
weight: 250
url: /fr/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Cet article présente comment exécuter GridWeb dans Docker pour construire une application d éditeur ou de visualisation Excel en ligne.
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

# Guide Docker

## Prérequis

Assurez-vous d'avoir Docker installé sur votre machine. Vous pouvez télécharger et installer Docker depuis le [site officiel de Docker](https://www.docker.com/get-started).

## Étape 1 : Créer un Dockerfile

Créez un fichier nommé `Dockerfile` dans votre [répertoire](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). Le `Dockerfile` doit contenir des instructions sur la façon de construire votre image Docker.

## Étape 2 : Écrire Dockerfile pour GridWeb

Voici un exemple [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) pour une démo GridWeb avec une application Java :

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

## Étape 3 : Construction de l'image Docker
Construire l'image Docker : Depuis le terminal, exécutez la commande suivante pour construire votre image Docker :
```bash
docker build -t gridweb-demo-java .
```
Vous pouvez remplacer gridweb-demo-java par le nom que vous souhaitez donner à votre image Docker.

## Étape 4 : Exécution d'un conteneur Docker
Une fois l'image construite, vous pouvez exécuter un conteneur à l'aide de la commande suivante :

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Explication des options de la commande Docker Run
-d : Exécuter le conteneur en mode détaché (en arrière-plan).
-p 8080:8080 : Mapper le port 8080 dans le conteneur au port 8080 sur la machine hôte.
--name gridweb-demo-container : Assigner un nom au conteneur.

## Étape 5 : Vérifier que le conteneur fonctionne
Pour vérifier si votre conteneur fonctionne, utilisez la commande suivante :

```bash
docker ps
```
Cela listera tous les conteneurs en cours d'exécution. Vous devriez voir votre conteneur avec son nom et son statut.

## Étape 6 : Accéder à l'application web

Ouvrez un navigateur web et allez à `http://localhost:8080/gridwebdemo/index`. Vous devriez voir votre application fonctionner.



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
docker rmi gridweb-demo-java
```




