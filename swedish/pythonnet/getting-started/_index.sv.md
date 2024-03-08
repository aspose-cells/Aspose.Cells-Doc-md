---
title: Komma igång
linktitle: Komma igång
type: docs
weight: 4
url: /sv/python-net/getting-started/
description: Lär dig hur du installerar Aspose.Cells for Python via .NET och skapar Hello World-applikationen.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
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

- Obs: På grund av vårt beroende av SkiaSharps grafikbibliotek, om du stöter på följande fel:
**System.DllNotFoundException: Det går inte att ladda det delade biblioteket 'libSkiaSharp' eller något av dess beroenden.** vänligen installera SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Efter installationen, kör följande kommando
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Om du vill ha det enklare kan du naturligtvis också ladda ner[libSkiaSharp.dylib](libSkiaSharp.dylib) och då**kopiera** det till**/usr/local/lib** katalog.

##  **Så här skapar du Hello World-applikationen med Aspose.Cells for Python via .NET**

-  Skapa en fil med namnet**Skapar HelloWorldFile.py** och använd följande exempelkod:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Spara nu koden ovan till "CreatingHelloWorldFile.py" och kör "python CreatingHelloWorldFile.py" @kommandotolken.

##  **Python via .NET Exempel github**
-  Besök gärna[Aspose.Cells for Python via .NET Exempel](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github för att se fler exempelkoder.


