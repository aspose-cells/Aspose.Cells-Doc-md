---
title: Empezando
linktitle: Empezando
type: docs
weight: 4
url: /es/python-net/getting-started/ 
keywords: python, excel, instal
description: Configuración Aspose.Cells for Python via .NET y pautas de instalación.
---
## **Requisitos del sistema**
 Aspose.Cells for Python via .NET es independiente de la plataforma API y se puede usar en cualquier plataforma (Windows y Linux) donde[Python](https://www.python.org/downloads/) esta instalado.

## **Python Versión**
- Python 3.6 o superior

## **Instalación**
### **Windows:**
 Puede usar fácilmente Aspose.Cells for Python via .NET desde[pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
 Puede usar fácilmente Aspose.Cells for Python via .NET desde[pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Mac OS:**
 Puede usar fácilmente Aspose.Cells for Python via .NET desde[pypi](https://pypi.org/project/aspose-cells-python/) con el siguiente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: si su python es Python3.7 (tome python3.7, por ejemplo, aquí), después de instalar aspose-cells-python, puede haber los siguientes errores
 '/usr/local/lib/libpython3.7m.dylib' (no existe tal archivo), '/usr/lib/libpython3.7m.dylib' (no existe tal archivo).
 En tal situación, agregue el siguiente comando a su bash_profile (Encuentre dónde está libpython3.7m.dylib primero, tome /Library/Frameworks/Python.framework/Versions/3.7/lib
 por ejemplo aquí)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
## **Creación de la aplicación Hello World**

-  Crear un archivo llamado**CreandoHelloWorldFile.py** y use el siguiente código de muestra:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ahora guarde el código anterior en "CreatingHelloWorldFile.py" y ejecute "python CreatingHelloWorldFile.py" en el símbolo del sistema.

