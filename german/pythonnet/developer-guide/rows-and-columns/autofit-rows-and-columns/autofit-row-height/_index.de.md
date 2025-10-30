---
title: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/python-net/autofit-row-height/
description: Erfahren Sie, wie Sie die Zeilen anpassen, die nicht individuell angepasst wurden, durch die Aspose.Cells für Python via .NET API.
keywords: Python Excel Bibliothek, Python AutoFit Zeilenhöhe beim Laden der Datei, Passen Sie automatisch die Zeilenhöhe an, wenn Sie die Excel Datei öffnen. 
---

## **Mögliche Verwendungsszenarien**
Die Höhe der Zeile passt sich automatisch der Schriftart des Inhalts an, aber wenn die Höhe der gecachten Zeile nicht der Höhe des Inhalts in der Datei entspricht, wird MS Excel die Zeilenhöhe automatisch anpassen, wenn die Datei geladen wird, während Aspose.Cells für Python via .NET sie nicht automatisch anpasst, um die Leistung zu verbessern. Wenn Sie das Aspose.Cells für Python via .NET Programm verwenden müssen, um die Zeilenhöhe automatisch anzugleichen, wenn Dateien geladen werden, können Sie das über den Parameter [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) erreichen.

Bitte beachten Sie die folgenden Bilddaten. Wir können beobachten, dass die zwischengespeicherte Zeilenhöhe in Zeile 11 15 beträgt, aber Excel passt die Zeilenhöhe automatisch an, wenn die Datei geladen wird.
<br>
<img src="1.png" width=70% />

## **Zeilenhöhe anpassen mit Aspose.Cells für Python Excel Bibliothek**
Wenn Sie die Datei direkt laden und sie als PDF speichern, wird die Daten nicht vollständig in PDF angezeigt, weil die Zeilenhöhe des zwischengespeicherten Inhalts nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
Wenn Sie den Parameter [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) auf true setzen, wenn Sie die Datei laden, wird Aspose.Cells für Python via .NET die Zeilenhöhe automatisch anpassen. Die angepasste Zeilenhöhe kann effektiv den Anzeigeanforderungen des Texts entsprechen.
<br>
<img src="3.png" width=70% />

## **Python-Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
