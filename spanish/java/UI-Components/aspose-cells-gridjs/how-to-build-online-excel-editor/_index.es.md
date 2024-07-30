---
title: cómo ejecutar Aspose.Cells.GridJs en docker
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Este artículo presenta cómo ejecutar GridJs en docker para construir una aplicación en línea de edición o visualización de excel.
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

# Guía de Docker

## Requisitos previos

Asegúrese de tener Docker instalado en su máquina. Puede descargar e instalar Docker desde el [sitio web oficial de Docker](https://www.docker.com/get-started).

## Paso 1: Crear un Dockerfile

Cree un archivo llamado `Dockerfile` en su [directorio](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs) del proyecto. El `Dockerfile` debe contener instrucciones sobre cómo construir su imagen de Docker.

## Paso 2: Escriba el Dockerfile para GridJs

Aquí hay un ejemplo de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) para la demostración de GridJs con una aplicación Java:

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

## Paso 3: Construyendo la Imagen de Docker
Construya la imagen de Docker: Desde el terminal, ejecute el siguiente comando para construir su imagen de Docker:
```bash
docker build -t gridjs-demo-java .
```
puede reemplazar gridjs-demo-java con el nombre que desee darle a su imagen de Docker.

## Paso 4: Ejecutando un Contenedor Docker
Una vez que la imagen esté construida, puede ejecutar un contenedor utilizando el siguiente comando:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Explicación de las opciones del comando Docker Run
-d: Ejecutar el contenedor en modo desprendido (en segundo plano).
-p 8080:80: Mapear el puerto 80 en el contenedor al puerto 8080 en la máquina host.
--name gridjs-demo-container: Asignar un nombre al contenedor.

## Paso 5: Verificar que el Contenedor se está Ejecutando
Para verificar si su contenedor se está ejecutando, use el siguiente comando:

```bash
docker ps
```
Esto listará todos los contenedores en ejecución. Debería ver su contenedor en la lista junto con su nombre y estado.

## Paso 6: Acceder a la Aplicación Web

Abra un navegador web y vaya a `http://localhost:8080/gridjsdemo/index`. Debería ver su aplicación en ejecución.

## Comandos Adicionales

### Detener el Contenedor

Para detener un contenedor en ejecución, use el siguiente comando:

```bash
docker stop gridjs-demo-container
```

### Eliminar un contenedor
Para eliminar un contenedor detenido, utiliza el siguiente comando:

```bash
docker rm  gridjs-demo-container
```

### Eliminar una imagen
Para eliminar una imagen, utiliza el siguiente comando:

```bash
docker rmi gridjs-demo-java
```




