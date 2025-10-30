---
title: Erste Schritte
linktitle: Erste Schritte
type: docs
weight: 4
url: /de/python-net/getting-started/
description: Lernen Sie, wie Sie Aspose.Cells für Python via .NET installieren und eine Hello World Anwendung erstellen.
keywords: Wie installiert man Aspose.Cells für Python via .NET in Windows, Linux und MacOS? Installationsrichtlinien für Aspose.Cells für Python via .NET und ein Hello World Programm durch Python über .NET. 
---

## **Systemanforderungen**
Aspose.Cells für Python via .NET ist eine plattformunabhängige API und kann auf jeder Plattform (Windows und Linux) verwendet werden, auf der [Python](https://www.python.org/downloads/) installiert ist. 

## **Python-Version**
- Python 3.6 oder höher

## **Installation**
### **Windows:**
Aspose.Cells für Python via .NET kann leicht über den Befehl [pypi](https://pypi.org/project/aspose-cells-python/) verwendet werden.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Aspose.Cells für Python via .NET kann leicht über den Befehl [pypi](https://pypi.org/project/aspose-cells-python/) verwendet werden.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Hinweis: Sie müssen den folgenden Befehl vor der Installation ausführen.
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Aspose.Cells für Python via .NET kann leicht über den Befehl [pypi](https://pypi.org/project/aspose-cells-python/) verwendet werden.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Hinweis: Wenn Ihr Python Python3.7 ist (hier als Beispiel), können nach der Installation von aspose-cells-python die folgenden Fehler auftreten:
  '/usr/local/lib/libpython3.7m.dylib' (Datei nicht gefunden), '/usr/lib/libpython3.7m.dylib' (Datei nicht gefunden) Meldung.
  In einer solchen Situation fügen Sie bitte den folgenden Befehl zu Ihrer bash_profile hinzu (Finden Sie zuerst heraus, wo sich libpython3.7m.dylib befindet, nehmen Sie z. B. /Library/Frameworks/Python.framework/Versions/3.7/lib als Beispiel).
  - Hinweis: Aufgrund unserer Abhängigkeit von der Grafikbibliothek SkiaSharp, wenn Ihnen der folgende Fehler begegnet:
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

**System.DllNotFoundException: Kann die freigegebene Bibliothek 'libSkiaSharp' oder eine ihrer Abhängigkeiten nicht laden.** installieren Sie bitte SkiaSharp.
Nach der Installation führen Sie bitte den folgenden Befehl aus
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
Nach der Installation führen Sie bitte den folgenden Befehl aus 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Natürlich können Sie auch, wenn Sie es einfacher möchten, [libSkiaSharp.dylib](libSkiaSharp.dylib) herunterladen und dann **kopieren** Sie es in das Verzeichnis **/usr/local/lib**.

> ⚠️ **Hinweis:**  
In einigen Fällen kann es nach der Installation einer neuen Version von **aspose-cells-python** zu einem Fehler wie folgt kommen:

**Beim Initialisieren des Hosts für den Typ ‘WrpNs_Aspose.WrpNs_Cells.WrpCs_Workbook_xxxxxx (Assembly=WrpInterop.Aspose.Cells)’ ist ein Fehler aufgetreten - Methode ‘call_000_xxxxxx’ wurde nicht gefunden**

Dies deutet darauf hin, dass die vorherige Version nicht vollständig deinstalliert wurde, was zu einem Konflikt zwischen der neu installierten Version und der alten führt.  
Sie können dieses Problem beheben, indem Sie die folgenden Schritte ausführen:

- Erstellen Sie zunächst eine saubere virtuelle Umgebung, um sicherzustellen, dass die neueste Version auf Ihrem Windows-Computer ordnungsgemäß funktioniert:

```
# Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate
# Install aspose-cells-python
pip install aspose-cells-python
```
Führen Sie dann Ihr Programm aus.

- Wenn Sie Ihre ursprüngliche Umgebung weiterhin verwenden möchten, versuchen Sie bitte die folgenden Schritte:

```
pip uninstall aspose-cells-python
```
Stellen Sie sicher, dass die Deinstallation erfolgreich war. Wenn während der Deinstallation Fehler auftreten, versuchen Sie, den Befehl mehrfach auszuführen.
Alternativ können Sie Ihr **site-packages**-Verzeichnis suchen, in der Regel etwas wie:

```
\Python3x\Lib\site-packages
```

Löschen Sie dann manuell die folgenden Verzeichnisse (falls vorhanden):

```
aspose
aspose_cells*
```

Danach installieren Sie das Paket erneut:

```
pip install aspose-cells-python
```

## **Wie man die Hello World-Anwendung mit Aspose.Cells für Python via .NET erstellt**

- Erstellen Sie eine Datei mit dem Namen **CreatingHelloWorldFile.py** und verwenden Sie den folgenden Beispielcode:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Speichern Sie den obigen Code jetzt unter "CreatingHelloWorldFile.py" und führen Sie "python CreatingHelloWorldFile.py" im Befehlsfenster aus.

## **Python via .NET Beispiel github**
- Bitte besuchen Sie das [Aspose.Cells for Python via .NET Beispiel](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github, um weitere Beispielscodes anzuzeigen.


{{< app/cells/assistant language="python-net" >}}
