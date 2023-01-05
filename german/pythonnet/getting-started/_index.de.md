---
title: Einstieg
linktitle: Einstieg
type: docs
weight: 4
url: /de/python-net/getting-started/ 
keywords: python, excel, instal
description: Setup Aspose.Cells for Python via .NET und Installationsrichtlinien.
---
## **System Anforderungen**
 Aspose.Cells for Python via .NET ist plattformunabhängig API und kann auf jeder Plattform (Windows und Linux) eingesetzt werden[Python](https://www.python.org/downloads/) ist installiert.

## **Python-Version**
- Python 3,6 oder höher

## **Installation**
### **Windows:**
 Sie können ganz einfach unter Aspose.Cells for Python via .NET aus[pypi](https://pypi.org/project/aspose-cells-python/) mit folgendem Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
 Sie können ganz einfach unter Aspose.Cells for Python via .NET aus[pypi](https://pypi.org/project/aspose-cells-python/) mit folgendem Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Mac OS:**
 Sie können ganz einfach unter Aspose.Cells for Python via .NET aus[pypi](https://pypi.org/project/aspose-cells-python/) mit folgendem Befehl.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Hinweis: Wenn Ihr Python Python 3.7 ist (nehmen Sie hier beispielsweise Python 3.7), können nach der Installation von aspose-cells-python die folgenden Fehler auftreten
 '/usr/local/lib/libpython3.7m.dylib' (keine solche Datei), '/usr/lib/libpython3.7m.dylib' (keine solche Datei) Eingabeaufforderung.
 Fügen Sie in einer solchen Situation bitte den folgenden Befehl zu Ihrem bash_profile hinzu (finden Sie zuerst, wo libpython3.7m.dylib ist, nehmen Sie /Library/Frameworks/Python.framework/Versions/3.7/lib
 zum Beispiel hier)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
## **Erstellen der Hello World-Anwendung**

-  Erstellen Sie eine Datei mit dem Namen**Erstellen von HelloWorldFile.py** und verwenden Sie den folgenden Beispielcode:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Speichern Sie nun den obigen Code in „CreatingHelloWorldFile.py“ und führen Sie „python CreatingHelloWorldFile.py“ @command prompt aus.

