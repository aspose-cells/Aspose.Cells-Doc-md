---
title: cómo ejecutar Aspose.Cells.GridJs en Docker
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Este artículo introduce cómo ejecutar GridJs en Docker para construir una aplicación de editor o visualizador de Excel en línea.
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

# Guía de Docker

## Requisitos previos

Asegúrese de tener Docker instalado en su máquina. Puede descargar e instalar Docker desde la [página oficial de Docker](https://www.docker.com/get-started).

## Paso 1: Crear un Dockerfile

Crea un archivo llamado `Dockerfile` en el [directorio](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs) de tu proyecto. El `Dockerfile` debe contener instrucciones sobre cómo construir tu imagen de Docker.

## Paso 2: Escribir Dockerfile para GridJs

Aquí tienes un ejemplo de [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) para la demostración de GridJs con aplicación en python:

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

## Paso 3: Construir la imagen de Docker
Construir la imagen de Docker: Desde la terminal, ejecute el siguiente comando para construir su imagen de Docker:
```bash
docker build -t gridjs-demo-python .
```
puedes reemplazar gridjs-demo-python por el nombre que deseas darle a tu imagen Docker.

## Paso 4: Ejecutar un contenedor Docker
Una vez que la imagen esté construida, puede ejecutar un contenedor usando el siguiente comando:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

o simplemente ejecutar la demostración en modo de prueba:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Explicación de las opciones del comando Docker Run
-d: Ejecutar el contenedor en modo desacoplado (en segundo plano).
-p 2022:2022: Mapea el puerto 2022 en el contenedor al puerto 2022 en la máquina anfitriona.
-v C:/ruta/a/license.txt:/app/license:  Mapear la ruta del archivo de licencia en la máquina host a la ruta del archivo en el contenedor.
--name gridjs-demo-container: Asignar un nombre al contenedor.

## Paso 5: Verificar que el contenedor esté en ejecución
Para verificar si su contenedor está en ejecución, utilice el siguiente comando:

```bash
docker ps
```
Esto listará todos los contenedores en ejecución. Debería ver su contenedor listado junto con su nombre y estado.

## Paso 6: Acceder a la aplicación web

Abre un navegador web y navega a `http://localhost:2022`. Deberías ver tu aplicación en ejecución.

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
docker rmi gridjs-demo-python
```




