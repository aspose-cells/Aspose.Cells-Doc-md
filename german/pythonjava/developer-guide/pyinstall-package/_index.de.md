---
title: Verwenden von PyInstaller zur einfachen Verteilung von Python-Anwendungen
linktitle: Paket mit Pyinstaller
type: docs
weight: 10
url: /de/python-java/pyinstaller-python/
description: Verpacken Sie Python-Code über den Pyinstaller in eine EXE-Datei.
---
##  **Wofür wird PyInstaller verwendet?**
PyInstaller liest ein von Ihnen geschriebenes Python-Skript. Es analysiert Ihren Code, um alle anderen Module und Bibliotheken zu ermitteln, die Ihr Skript zur Ausführung benötigt. Dann sammelt es Kopien all dieser Dateien – einschließlich des aktiven Python-Interpreters!

##  **Warum Pyinstaller zum Paketieren von Python verwenden?**
PyInstaller wird verwendet, um Python-Code in eigenständige ausführbare Anwendungen für verschiedene Betriebssysteme zu packen. Es benötigt ein Python-Skript und generiert eine einzelne ausführbare Datei, die alle erforderlichen Abhängigkeiten enthält und auf Computern ausgeführt werden kann, auf denen Python nicht installiert ist. Dies ermöglicht eine einfache Verteilung und Bereitstellung von Python-Anwendungen, da der Benutzer Python und alle erforderlichen Module nicht auf seinem System installiert haben muss, um die Anwendung auszuführen. Darüber hinaus kann PyInstaller auch zum Erstellen von ausführbaren Dateien mit einer Datei verwendet werden, bei denen es sich um einzelne ausführbare Dateien handelt, die alle erforderlichen Abhängigkeiten für die Anwendung enthalten. Dies kann die Verteilung der Anwendung noch einfacher machen, da der Benutzer nur eine einzige Datei herunterladen muss.

##  **So installieren Sie PyInstaller**
 PyInstaller ist als reguläres Paket Python verfügbar. Die Quellarchive für veröffentlichte Versionen sind verfügbar unter[PyPi](https://pypi.org/project/pyinstaller/) , aber es ist einfacher, die neueste Version mit zu installieren[Pip](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Um eine bestehende PyInstaller-Installation auf die neueste Version zu aktualisieren, verwenden Sie:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Um die aktuelle Entwicklungsversion zu installieren, verwenden Sie:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **Wie erstelle ich eine EXE-Datei mit PyInstaller?**
 Wir nehmen eine einzelne Python-Datei als Beispiel, um die Verpackungsschritte im Detail zu erläutern. Nehmen Sie nach der Installation Python 3.11.0 als Beispiel[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  Erstellen Sie eine Python-Beispieldatei mit dem Namen[example.py](example.py).
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
1. Erstellen Sie einen Ordner als c:\app und kopieren Sie example.py (angehängt) nach c:\app.
1. Öffnen Sie Ihre Eingabeaufforderung und führen Sie den Befehl pyinstaller example.py aus.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Kopieren Sie die JAR-Dateien (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Sie befinden sich im Ordner C:\Python311\Lib\site-packages\asposecells\lib ) nach c:\app.
1.  Bearbeiten Sie die Datei mit dem Suffix „spec“, um einen Datenabschnitt hinzuzufügen[example.spec](example.spec).
![todo:image_alt_text](example.png)
1. Führen Sie „pyinstaller example.spec“ im Eingabeaufforderungsfenster aus.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Wechseln Sie in das Verzeichnis C:\app\dist\example. Dort finden Sie die Datei example.exe.
