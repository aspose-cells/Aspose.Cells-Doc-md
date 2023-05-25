---
title: Uso de PyInstaller para distribuir fácilmente aplicaciones Python
linktitle: Paquete usando Pyinstaller
type: docs
weight: 10
url: /es/python-java/pyinstaller-python/
description: Empaquete el código de python a exe a través de pyinstaller.
---
##  **¿Para qué se utiliza PyInstaller?**
PyInstaller lee un script Python escrito por usted. Analiza su código para descubrir todos los demás módulos y bibliotecas que su secuencia de comandos necesita para ejecutarse. Luego recopila copias de todos esos archivos, ¡incluido el intérprete activo Python!

##  **¿Por qué usar Pyinstaller para empaquetar Python?**
PyInstaller se usa para empaquetar el código Python en aplicaciones ejecutables independientes para varios sistemas operativos. Toma un script Python y genera un solo archivo ejecutable que contiene todas las dependencias necesarias y se puede ejecutar en computadoras que no tienen instalado Python. Esto permite una fácil distribución e implementación de las aplicaciones Python, ya que el usuario no necesita tener Python ni los módulos necesarios instalados en su sistema para ejecutar la aplicación. Además, PyInstaller también se puede usar para crear ejecutables de un solo archivo, que son archivos ejecutables únicos que contienen todas las dependencias requeridas para la aplicación. Esto puede facilitar aún más la distribución de la aplicación, ya que el usuario solo necesita descargar un único archivo.

##  **Cómo instalar PyInstaller**
 PyInstaller está disponible como paquete regular Python. Los archivos fuente de las versiones publicadas están disponibles en[PyPi](https://pypi.org/project/pyinstaller/) , pero es más fácil instalar la última versión usando[pepita](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Para actualizar la instalación existente de PyInstaller a la última versión, use:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Para instalar la versión de desarrollo actual, utilice:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **¿Cómo creo un EXE usando PyInstaller?**
 Tomaremos un solo archivo python como ejemplo para explicar los pasos de empaquetado en detalle. Tome Python 3.11.0 como ejemplo después de la instalación[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  Cree un archivo de muestra de python llamado[ejemplo.py](example.py).
{{< highlight "java" >}}

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
1. Cree una carpeta como c:\app y copie example.py (adjunto) a c:\app.
1. Abra su símbolo del sistema y ejecute el comando pyinstaller example.py.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Copie los archivos jar (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Existen en la carpeta C:\Python311\Lib\site-packages\asposecells\lib ) a c:\aplicación.
1.  Edite el archivo con el sufijo de especificación para agregar una sección de datos como[ejemplo.spec](example.spec).
![todo:imagen_alt_texto](example.png)
1. Ejecute pyinstaller example.spec en la ventana del símbolo del sistema.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Cambia el directorio a C:\app\dist\example, y encontrarás el archivo example.exe.
