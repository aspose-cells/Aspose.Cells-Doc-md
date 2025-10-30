---
title: Mit PyInstaller Python Anwendungen einfach verteilen
linktitle: Paketierung mit PyInstaller
type: docs
weight: 10
url: /de/python-java/pyinstaller-python/
description: Python Code mit PyInstaller zu einer ausführbaren Datei (exe) paketieren
---

## **Wofür wird PyInstaller verwendet?**
PyInstaller liest ein von Ihnen geschriebenes Python-Skript. Es analysiert Ihren Code, um jedes andere Modul und jede Bibliothek zu entdecken, die Ihr Skript zum Ausführen benötigt. Dann sammelt es Kopien all dieser Dateien – einschließlich des aktiven Python-Interpreters!

## **Warum PyInstaller zum Verpacken von Python verwenden?**
PyInstaller wird verwendet, um Python-Code in eigenständige ausführbare Anwendungen für verschiedene Betriebssysteme zu verpacken. Es nimmt ein Python-Skript und generiert eine einzelne ausführbare Datei, die alle notwendigen Abhängigkeiten enthält und auf Computern ausgeführt werden kann, auf denen kein Python installiert ist. Dies ermöglicht eine einfache Verteilung und Bereitstellung von Python-Anwendungen, da der Benutzer Python und benötigte Module nicht auf seinem System installiert haben muss, um die Anwendung auszuführen. Darüber hinaus kann PyInstaller auch verwendet werden, um Ein-Datei-Ausführbare zu erstellen, die einzelne ausführbare Dateien sind, die alle erforderlichen Abhängigkeiten für die Anwendung enthalten. Dies kann die Verteilung der Anwendung noch einfacher machen, da der Benutzer nur eine Datei herunterladen muss.

## **Wie man PyInstaller installiert**
PyInstaller ist als reguläres Python-Paket verfügbar. Die Quellarchive für veröffentlichte Versionen sind von [PyPi](https://pypi.org/project/pyinstaller/) verfügbar, aber es ist einfacher, die neueste Version mit [pip](https://pip.pypa.io/en/stable/) zu installieren:
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Um eine vorhandene PyInstaller-Installation auf die neueste Version zu aktualisieren, verwenden Sie:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Um die aktuelle Entwicklerversion zu installieren, verwenden Sie:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **Wie erstellt man eine EXE-Datei mit PyInstaller**
Wir verwenden eine einzelne Python-Datei als Beispiel, um die Verpackungsschritte detailliert zu erläutern. Nehmen Sie Python 3.11.0 als Beispiel und installieren Sie [aspose.cells](https://pypi.org/project/aspose-cells/).

1. Erstellen Sie eine Python-Beispieldatei mit dem Namen [example.py](example.py).
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
1. Erstellen Sie einen Ordner als c:\app und kopieren Sie die Datei example.py (angehängt) in c:\app.
1. Öffnen Sie die Eingabeaufforderung und führen Sie den Befehl pyinstaller example.py aus.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Kopieren Sie die JAR-Dateien (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Sie befinden sich im Ordner C:\Python311\Lib\site-packages\asposecells\lib) nach c:\app.
1. Bearbeiten Sie die Datei mit der Suffix-Spezifikation, um einen Datenabschnitt hinzuzufügen, wie in [example.spec](example.spec).
![todo:image_alt_text](example.png)
1. Führen Sie den Befehl pyinstaller example.spec im Eingabeaufforderungsfenster aus.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Wechseln Sie in das Verzeichnis C:\app\dist\example und Sie finden die Datei example.exe.
