---
title: Cómo ejecutar Aspose.Cells para Python via .NET en Docker
type: docs
description: "Ejecutar Aspose.Cells en un contenedor Docker para Linux"
weight: 140
url: /es/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Prefacio:

Cada vez más usuarios utilizan varios productos de nuestra empresa en Docker y encuentran diversos problemas. Este artículo presenta brevemente cómo usar Aspose.Cells para Python via .NET en un entorno Docker basado en Debian Linux.

## Ejemplo:

Ilustramos el uso con un ejemplo simple. En este caso, la funcionalidad es muy sencilla, solo abrir un archivo Excel que contiene texto en japonés en aspose_test.py. Aquí, usamos python:3.11 como imagen base, y el Dockerfile correspondiente es el siguiente:

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

Luego, cuando ejecutamos el siguiente comando, obtenemos el resultado final:
- Construir Imagen de Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Ejecutar Imagen de Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Nota:

Para soportar la apertura de archivos Excel que contienen varios idiomas, necesitamos instalar ICU. Considerando que el wrapper de Python via .NET está basado en .NET Core 3.1, y que .NET Core 3.1 tiene requisitos específicos de versión para ICU, que no deben exceder la versión 70, necesitamos instalar una versión específica de ICU.


## Ver También

- [Instalar Docker Desktop en Windows](https://docs.docker.com/docker-for-windows/install/)
