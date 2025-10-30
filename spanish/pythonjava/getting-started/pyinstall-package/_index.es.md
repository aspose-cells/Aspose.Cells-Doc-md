---
title: Usar PyInstaller para Distribuir Fácilmente Aplicaciones Python
linktitle: Empaquetar Usando Pyinstaller
type: docs
weight: 10
url: /es/python-java/pyinstaller-python/
description: Empaquetar código python a exe a través de pyinstaller.
---

## **¿Para qué se utiliza PyInstaller?**
PyInstaller lee un script de Python escrito por ti. Analiza tu código para descubrir cada otro módulo y biblioteca que tu script necesita para ejecutarse. Luego recopila copias de todos esos archivos, ¡incluido el intérprete de Python activo!

## **¿Por qué usar Pyinstaller para empaquetar Python?**
PyInstaller se utiliza para empaquetar código Python en aplicaciones ejecutables independientes para varios sistemas operativos. Toma un script de Python y genera un solo archivo ejecutable que contiene todas las dependencias necesarias y puede ejecutarse en computadoras que no tienen Python instalado. Esto permite una distribución y despliegue fáciles de aplicaciones de Python, ya que el usuario no necesita tener Python y los módulos necesarios instalados en su sistema para ejecutar la aplicación. Además, PyInstaller también se puede utilizar para crear ejecutables de un solo archivo, que son archivos ejecutables únicos que contienen todas las dependencias necesarias para la aplicación. Esto puede hacer que sea aún más fácil distribuir la aplicación, ya que el usuario solo necesita descargar un solo archivo.

## **Cómo Instalar PyInstaller**
PyInstaller está disponible como un paquete regular de Python. Los archivos fuente de las versiones lanzadas están disponibles en [PyPi](https://pypi.org/project/pyinstaller/), pero es más fácil instalar la última versión usando [pip](https://pip.pypa.io/en/stable/):
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Para actualizar la instalación existente de PyInstaller a la última versión, use:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Para instalar la versión de desarrollo actual, use:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **¿Cómo creo un EXE usando PyInstaller?**
Tomaremos un solo archivo de Python como ejemplo para explicar detalladamente los pasos de empaquetado. Tomemos Python 3.11.0 como ejemplo después de instalar [aspose.cells](https://pypi.org/project/aspose-cells/).

1. Cree un archivo de muestra en Python llamado [example.py](example.py).
{{< highlight java >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. Cree una carpeta como c:\app y copie example.py(adjunto) a c:\app.
1. Abra su símbolo del sistema y ejecute el comando pyinstaller example.py.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Copie los archivos jars(aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Están en la carpeta C:\Python311\Lib\site-packages\asposecells\lib) a c:\app.
1. Edite el archivo con el sufijo spec para agregar sección de datos como [example.spec](example.spec).
![todo:image_alt_text](example.png)
1. Ejecute pyinstaller example.spec en la ventana del símbolo del sistema.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Cambie el directorio a C:\app\dist\example, y encontrará el archivo example.exe.
