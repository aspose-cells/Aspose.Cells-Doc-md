---
title: Erste Schritte
linktitle: Erste Schritte
type: docs
weight: 4
url: /de/python-net/getting-started/
description: Erfahren Sie, wie Sie Aspose.Cells, for Python und via .NET installieren und die Anwendung Hello World erstellen.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **System Anforderungen**
 Aspose.Cells for Python via .NET ist plattformunabhängig API und kann auf jeder Plattform (Windows und Linux) verwendet werden[Python](https://www.python.org/downloads/) ist installiert.

##  **Python Version**
- Python 3.6 oder höher

##  **Installation**
###  **Windows:**
 Sie können ganz einfach Aspose.Cells for Python via .NET von verwenden[Pypi](https://pypi.org/project/aspose-cells-python/) mit dem folgenden Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Sie können ganz einfach Aspose.Cells for Python via .NET von verwenden[Pypi](https://pypi.org/project/aspose-cells-python/) mit dem folgenden Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Hinweis: Sie müssen vor der Installation den folgenden Befehl ausführen
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS:**
 Sie können ganz einfach Aspose.Cells for Python via .NET von verwenden[Pypi](https://pypi.org/project/aspose-cells-python/) mit dem folgenden Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Hinweis: Wenn es sich bei Ihrer Python um Python3.7 handelt (nehmen Sie hier beispielsweise Python3.7), können nach der Installation von aspose-cells-python die folgenden Fehler auftreten
 Eingabeaufforderung „/usr/local/lib/libpython3.7m.dylib“ (keine solche Datei), „/usr/lib/libpython3.7m.dylib“ (keine solche Datei).
 Fügen Sie in einer solchen Situation bitte den folgenden Befehl zu Ihrem bash_profile hinzu (Finden Sie zuerst heraus, wo sich libpython3.7m.dylib befindet, und nehmen Sie /Library/Frameworks/Python.framework/Versions/3.7/lib
 zum Beispiel hier)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Hinweis: Aufgrund unserer Abhängigkeit von der SkiaSharp-Grafikbibliothek tritt die folgende Fehlermeldung auf:
**System.DllNotFoundException: Die gemeinsam genutzte Bibliothek „libSkiaSharp“ oder eine ihrer Abhängigkeiten kann nicht geladen werden.** Bitte installieren Sie SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Führen Sie nach der Installation bitte den folgenden Befehl aus
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Wenn Sie es einfacher möchten, können Sie es natürlich auch herunterladen[libSkiaSharp.dylib](libSkiaSharp.dylib) und dann**Kopieren** es zum**/usr/local/lib** Verzeichnis.

##  **So erstellen Sie die Hello World-Anwendung mit Aspose.Cells for Python via .NET**

-  Erstellen Sie eine Datei mit dem Namen**Erstellen von HelloWorldFile.py** und verwenden Sie den folgenden Beispielcode:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Speichern Sie nun den obigen Code unter „CreatingHelloWorldFile.py“ und führen Sie die @Eingabeaufforderung „python CreatingHelloWorldFile.py“ aus.

