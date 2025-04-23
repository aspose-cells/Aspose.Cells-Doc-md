---
title: cómo ejecutar Aspose.Cells.GridWeb para construir un editor o visor de hojas de cálculo en línea en docker
type: docs
weight: 250
url: /es/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Este artículo introduce cómo ejecutar GridWeb en docker para construir una aplicación de editor o visor de Excel en línea.
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

# Guía de Docker

## Requisitos previos

Asegúrese de tener Docker instalado en su máquina. Puede descargar e instalar Docker desde la [página oficial de Docker](https://www.docker.com/get-started).

## Paso 1: Crear un Dockerfile

Crea un archivo llamado `Dockerfile` en el [directorio](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/) de tu proyecto. El `Dockerfile` debe contener instrucciones sobre cómo construir tu imagen de Docker.

## Paso 2: Escribir Dockerfile para GridWeb

Aquí hay un ejemplo de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) para la demo de GridWeb con la aplicación Java:

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

## Paso 3: Construir la imagen de Docker
Construir la imagen de Docker: Desde la terminal, ejecute el siguiente comando para construir su imagen de Docker:
```bash
docker build -t gridweb-demo-java .
```
puedes reemplazar gridweb-demo-java con el nombre que deseas darle a tu imagen de Docker.

## Paso 4: Ejecutar un contenedor Docker
Una vez que la imagen esté construida, puede ejecutar un contenedor usando el siguiente comando:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Explicación de las opciones del comando Docker Run
-d: Ejecutar el contenedor en modo desacoplado (en segundo plano).
-p 8080:8080: Mapea el puerto 8080 en el contenedor al puerto 8080 en la máquina host.
--name gridweb-demo-container: Asigna un nombre al contenedor.

## Paso 5: Verificar que el contenedor esté en ejecución
Para verificar si su contenedor está en ejecución, utilice el siguiente comando:

```bash
docker ps
```
Esto listará todos los contenedores en ejecución. Debería ver su contenedor listado junto con su nombre y estado.

## Paso 6: Acceder a la aplicación web

Abre un navegador web y ve a `http://localhost:8080/gridwebdemo/index`. Deberías ver tu aplicación en funcionamiento.



## Comandos adicionales

### Deteniendo el Contenedor

Para detener un contenedor en ejecución, use el siguiente comando:

```bash
docker stop gridweb-demo-container
```

### Eliminando un Contenedor
Para eliminar un contenedor detenido, use el siguiente comando:

```bash
docker rm  gridweb-demo-container
```

### Eliminando una Imagen
Para eliminar una imagen, use el siguiente comando:

```bash
docker rmi gridweb-demo-java
```




