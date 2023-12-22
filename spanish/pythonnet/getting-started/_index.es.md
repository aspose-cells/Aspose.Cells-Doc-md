---
title: Empezando
linktitle: Empezando
type: docs
weight: 4
url: /es/python-net/getting-started/
description: Aprenda a instalar Aspose.Cells for Python via .NET y crear la aplicación Hello World.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **Requisitos del sistema**
 Aspose.Cells for Python via .NET es independiente de la plataforma API y se puede utilizar en cualquier plataforma (Windows y Linux) donde[Python](https://www.python.org/downloads/) esta instalado.

##  **Python Versión**
- Python 3.6 o superior

##  **Instalación**
###  **Windows:**
 Puede utilizar fácilmente Aspose.Cells for Python via .NET desde[pipi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Puede utilizar fácilmente Aspose.Cells for Python via .NET desde[pipi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: debe ejecutar el siguiente comando antes de la instalación
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS:**
 Puede utilizar fácilmente Aspose.Cells for Python via .NET desde[pipi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: Si su Python es Python3.7 (tome python3.7, por ejemplo, aquí), después de instalar aspose-cells-python, pueden ocurrir los siguientes errores
 '/usr/local/lib/libpython3.7m.dylib' (no existe tal archivo), mensaje '/usr/lib/libpython3.7m.dylib' (no existe tal archivo).
 En tal situación, agregue el siguiente comando a su bash_profile (busque primero dónde está libpython3.7m.dylib, tome /Library/Frameworks/Python.framework/Versions/3.7/lib
 por ejemplo aquí)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Nota: Debido a nuestra dependencia de la biblioteca de gráficos SkiaSharp, si encuentra el siguiente error:
**System.DllNotFoundException: no se puede cargar la biblioteca compartida 'libSkiaSharp' o una de sus dependencias.** instale SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Después de la instalación, ejecute el siguiente comando
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Por supuesto, si lo quieres más sencillo, también puedes descargarlo.[libSkiaSharp.dylib](libSkiaSharp.dylib) y luego**Copiar** a la**/usr/local/lib** directorio.

##  **Cómo crear la aplicación Hello World usando Aspose.Cells for Python via .NET**

-  Crea un archivo llamado**CreandoHelloWorldFile.py** y utilice el siguiente código de muestra:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ahora guarde el código anterior en "CreatingHelloWorldFile.py" y ejecute el símbolo del sistema "python CreatingHelloWorldFile.py".

