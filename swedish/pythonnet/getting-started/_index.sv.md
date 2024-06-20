---
title: Komma igång
linktitle: Komma igång
type: docs
weight: 4
url: /sv/python-net/getting-started/
description: Lär dig hur du installerar Aspose.Cells för Python via .NET och skapar en Hello World applikation.
keywords: Hur man installerar Aspose.Cells för Python via .NET i Windows Linux och MacOS, installationsanvisningar för Aspose.Cells för Python via .NET, Python Via .NET Hello World programmet. 
---

## **Systemkrav**
Aspose.Cells för Python via .NET är en plattformsoberoende API och kan användas på vilken plattform som helst (Windows och Linux) där [Python](https://www.python.org/downloads/) är installerat. 

## **Python Version**
- Python 3.6 eller högre

## **Installation**
### **Windows:**
Du kan enkelt använda Aspose.Cells för Python via .NET från [pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Du kan enkelt använda Aspose.Cells för Python via .NET från [pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Observera: Du måste köra följande kommando innan installation
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Du kan enkelt använda Aspose.Cells för Python via .NET från [pypi](https://pypi.org/project/aspose-cells-python/) med följande kommando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Observera: Om din python är Python3.7 (ta python3.7, till exempel här), efter installation av aspose-cells-python, kan följande fel uppstå
  ' /usr/local/lib/libpython3.7m.dylib ' (ingen sådan fil), '/usr/lib/libpython3.7m.dylib' (ingen sådan fil) prompt.
  I en sådan situation, lägg till följande kommando i din bash_profile (Hitta var libpython3.7m.dylib är först, ta /Library/Frameworks/Python.framework/Versions/3.7/lib
  till exempel här)
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Observera: Eftersom vi förlitar oss på grafikbiblioteket SkiaSharp, om du stöter på följande fel:
**System.DllNotFoundException: Unable to load shared library 'libSkiaSharp' or one of its dependencies.** var god installera SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
Efter installation, kör följande kommando 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Naturligtvis, om du vill ha det enklare, kan du även ladda ner [libSkiaSharp.dylib](libSkiaSharp.dylib) och sedan **kopiera** det till **/usr/local/lib** -katalogen.

## **Hur man skapar Hello World-applikationen med hjälp av Aspose.Cells för Python via .NET**

- Skapa en fil med namnet ** CreatingHelloWorldFile.py ** och använd följande exemplarkod:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Spara koden ovan till "CreatingHelloWorldFile.py" och kör "python CreatingHelloWorldFile.py" @kommandoprompt.

## **Python via .NET exempel github**
- Besök [Aspose.Cells för Python via .NET Exempel](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github för att se fler exemplarkoder.


