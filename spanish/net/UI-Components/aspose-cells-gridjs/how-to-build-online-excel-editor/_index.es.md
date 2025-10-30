---
title: cómo ejecutar Aspose.Cells.GridJs en Docker
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Este artículo introduce cómo ejecutar GridJs en Docker para construir una aplicación de editor o visualizador de Excel en línea.
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

# Guía de Docker

## Requisitos previos

Asegúrese de tener Docker instalado en su máquina. Puede descargar e instalar Docker desde la [página oficial de Docker](https://www.docker.com/get-started).

## Paso 1: Crear un Dockerfile

Crea un archivo llamado `Dockerfile` en el [directorio](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/). El `Dockerfile` debe contener instrucciones sobre cómo construir tu imagen de Docker.

## Paso 2: Escribir Dockerfile para GridJs

Aquí tienes un ejemplo de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Dockerfile) para la demo de GridJs con una aplicación ASP.NET Core:

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

## Paso 3: Construir la imagen de Docker
Construir la imagen de Docker: Desde la terminal, ejecute el siguiente comando para construir su imagen de Docker:
```bash
docker build -t gridjs-demo-net6 .
```
puede reemplazar gridjs-demo-net6 con el nombre que desee para su imagen de Docker.

## Paso 4: Ejecutar un contenedor Docker
Una vez que la imagen esté construida, puede ejecutar un contenedor usando el siguiente comando:

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

o simplemente ejecutar la demostración en modo de prueba:


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Explicación de las opciones del comando Docker Run
-d: Ejecutar el contenedor en modo desacoplado (en segundo plano).
-p 24262:80: Mapear el puerto 80 en el contenedor al puerto 24262 en la máquina host.
-v C:/ruta/a/license.txt:/app/license:  Mapear la ruta del archivo de licencia en la máquina host a la ruta del archivo en el contenedor.
--name gridjs-demo-container: Asignar un nombre al contenedor.

## Paso 5: Verificar que el contenedor esté en ejecución
Para verificar si su contenedor está en ejecución, utilice el siguiente comando:

```bash
docker ps
```
Esto listará todos los contenedores en ejecución. Debería ver su contenedor listado junto con su nombre y estado.

## Paso 6: Acceder a la aplicación web

Abra un navegador web y vaya a `http://localhost:24262/GridJs2/List`. Debería ver su aplicación en ejecución.

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
docker rmi gridjs-demo-net6
```




