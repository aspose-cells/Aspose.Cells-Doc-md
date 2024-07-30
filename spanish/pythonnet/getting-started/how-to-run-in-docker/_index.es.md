---
title: Cómo ejecutar Aspose.Cells para python via .NET en Docker
type: docs
description: "Ejecutar Aspose.Cells en un contenedor Docker para Linux"
weight: 140
url: /es/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Prefacio:

Cada vez más usuarios están utilizando varios productos de nuestra empresa en Docker y se enfrentan a diversos problemas. Este artículo introduce brevemente cómo usar Aspose.Cells para Python via .NET en un entorno Docker basado en Debian Linux.

## Ejemplo:

Ilustramos el uso con un ejemplo simple. En este caso, la funcionalidad es muy directa, simplemente abriendo un archivo de Excel que contiene texto en japonés en aspose_test.py. Aquí, usamos python:3.11 como imagen base, y el Dockerfile correspondiente es el siguiente:

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

Entonces, cuando ejecutamos el siguiente comando, obtenemos el resultado final:
- Construir Imagen de Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Ejecutar Imagen de Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Nota:

Para admitir la apertura de archivos de Excel que contienen varios idiomas, necesitamos instalar ICU. Dado que el contenedor de Python via .NET está basado en .NET Core 3.1, y .NET Core 3.1 tiene requisitos de versión específicos para ICU, que no deben exceder la versión 70, necesitamos instalar una versión específica de ICU.


## Ver También

- [Instalar Docker Desktop en Windows](https://docs.docker.com/docker-for-windows/install/)
