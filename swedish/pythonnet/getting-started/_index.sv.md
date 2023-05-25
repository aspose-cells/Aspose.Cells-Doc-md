---
title: Komma igång
linktitle: Komma igång
type: docs
weight: 4
url: /sv/python-net/getting-started/ 
keywords: python, excel, instal
description: Installation Aspose.Cells for Python via .NET och installationsriktlinjer.
---
##  **Systemkrav**
 Aspose.Cells for Python via .NET är plattformsoberoende API och kan användas på vilken plattform som helst (Windows och Linux) där[Python](https://www.python.org/downloads/) är installerad.

##  **Python Version**
- Python 3.6 eller högre

##  **Installation**
###  **Windows:**
 Du kan enkelt använda Aspose.Cells for Python via .NET från[pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Du kan enkelt använda Aspose.Cells for Python via .NET från[pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Obs: Du måste köra följande kommando innan installationen
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS:**
 Du kan enkelt använda Aspose.Cells for Python via .NET från[pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Obs: Om din python är Python3.7 (ta python3.7, till exempel här), efter installation av aspose-cells-python kan det finnas följande fel
 '/usr/local/lib/libpython3.7m.dylib' (ingen sådan fil), '/usr/lib/libpython3.7m.dylib' (ingen sådan fil) prompt.
 I en sådan situation, vänligen lägg till följande kommando till din bash_profile (Find var är libpython3.7m.dylib först, ta /Library/Frameworks/Python.framework/Versions/3.7/lib
 till exempel här)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
##  **Skapar Hello World-applikationen**

-  Skapa en fil med namnet**Skapar HelloWorldFile.py** och använd följande exempelkod:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Spara nu koden ovan till "CreatingHelloWorldFile.py" och kör "python CreatingHelloWorldFile.py" @kommandotolken.

