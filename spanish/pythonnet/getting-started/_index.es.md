---
title: Empezando
linktitle: Empezando
type: docs
weight: 4
url: /es/python-net/getting-started/
description: Aprenda cómo instalar Aspose.Cells para Python via .NET y crear una aplicación Hello World.
keywords: Cómo instalar Aspose.Cells para Python via .NET en Windows Linux y MacOS, pautas de instalación para Aspose.Cells para Python via .NET, programa Hello World de Python Via .NET. 
---

## **Requisitos del sistema**
Aspose.Cells para Python via .NET es una API independiente de la plataforma y se puede utilizar en cualquier plataforma (Windows y Linux) donde [Python](https://www.python.org/downloads/) esté instalado. 

## **Versión de Python**
- Python 3.6 o superior

## **Instalación**
### **Windows:**
Puede usar fácilmente Aspose.Cells for Python via .NET desde [pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Puede usar fácilmente Aspose.Cells for Python via .NET desde [pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: Debe ejecutar el siguiente comando antes de la instalación
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Puede usar fácilmente Aspose.Cells for Python via .NET desde [pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: Si su versión de Python es Python3.7(tome python3.7, por ejemplo), después de instalar aspose-cells-python, puede haber los siguientes errores
  '/usr/local/lib/libpython3.7m.dylib' (no existe ese archivo), '/usr/lib/libpython3.7m.dylib' (no existe ese archivo) aparece.
  En tal situación, por favor agregue el siguiente comando a su bash_profile(Encuentre dónde está libpython3.7m.dylib primero, tome /Library/Frameworks/Python.framework/Versions/3.7/lib
  por ejemplo aquí)
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Nota: Debido a nuestra dependencia de la biblioteca de gráficos SkiaSharp, si encuentra el siguiente error:
**System.DllNotFoundException: No se puede cargar la biblioteca compartida 'libSkiaSharp' o una de sus dependencias.** por favor instale SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
Después de la instalación, por favor ejecute el siguiente comando 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Por supuesto, si lo quiere más simple, también puede descargar [libSkiaSharp.dylib](libSkiaSharp.dylib) y luego **copiarlo** al directorio **/usr/local/lib**.

## **Cómo Crear la Aplicación Hola Mundo usando Aspose.Cells for Python via .NET**

- Cree un archivo llamado **CreandoArchivoHolaMundo.py** y use el siguiente código de ejemplo:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ahora guarde el código anterior en "CreandoArchivoHolaMundo.py" y ejecute "python CreandoArchivoHolaMundo.py" en la línea de comandos.

## **Ejemplo Python via .NET Github**
- Por favor visite el [Ejemplo Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github para ver más códigos de muestra.


