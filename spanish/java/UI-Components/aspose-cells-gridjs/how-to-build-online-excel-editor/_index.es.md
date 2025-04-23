---
title: cómo ejecutar Aspose.Cells.GridJs en Docker
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Este artículo introduce cómo ejecutar GridJs en Docker para construir una aplicación de editor o visualizador de Excel en línea.
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

Asegúrese de tener Docker instalado en su máquina. Puede descargar e instalar Docker desde la [página oficial de Docker](https://www.docker.com/get-started).

## Paso 1: Crear un Dockerfile

Crea un archivo llamado `Dockerfile` en el [directorio](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs) de tu proyecto. El `Dockerfile` debe contener instrucciones sobre cómo construir tu imagen de Docker.

## Paso 2: Escribir Dockerfile para GridJs

Aquí tienes un ejemplo de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) para la demostración de GridJs con aplicación Java:

```dockerfile
# Use the maven image to build jar file
FROM maven:3.8.6-amazoncorretto-17 AS build
WORKDIR /usr/src/app


# copy local Maven files to container
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN mvn  package -DskipTests


# Use the jdk8 image as the basic docker image
FROM eclipse/ubuntu_jdk8
WORKDIR /app
# copy build jar file to target container 
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
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
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## Paso 3: Construir la imagen de Docker
Construir la imagen de Docker: Desde la terminal, ejecute el siguiente comando para construir su imagen de Docker:
```bash
docker build -t gridjs-demo-java .
```
puedes reemplazar gridjs-demo-java por el nombre que quieras darle a tu imagen de Docker.

## Paso 4: Ejecutar un contenedor Docker
Una vez que la imagen esté construida, puede ejecutar un contenedor usando el siguiente comando:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

o simplemente ejecutar la demostración en modo de prueba:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Explicación de las opciones del comando Docker Run
-d: Ejecutar el contenedor en modo desacoplado (en segundo plano).
-p 8080:80: Mapear el puerto 80 del contenedor al puerto 8080 en la máquina host.
-v C:/ruta/a/license.txt:/app/license:  Mapear la ruta del archivo de licencia en la máquina host a la ruta del archivo en el contenedor.
--name gridjs-demo-container: Asignar un nombre al contenedor.

## Paso 5: Verificar que el contenedor esté en ejecución
Para verificar si su contenedor está en ejecución, utilice el siguiente comando:

```bash
docker ps
```
Esto listará todos los contenedores en ejecución. Debería ver su contenedor listado junto con su nombre y estado.

## Paso 6: Acceder a la aplicación web

Abre un navegador web y navega a `http://localhost:8080/gridjsdemo/index`. Deberías ver tu aplicación en ejecución.

## Comandos adicionales

### Deteniendo el Contenedor

Para detener un contenedor en ejecución, use el siguiente comando:

```bash
docker stop gridjs-demo-container
```

### Eliminando un Contenedor
Para eliminar un contenedor detenido, use el siguiente comando:

```bash
docker rm  gridjs-demo-container
```

### Eliminando una Imagen
Para eliminar una imagen, use el siguiente comando:

```bash
docker rmi gridjs-demo-java
```




