---
title: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/python-net/export-worksheet-css-separately-in-output/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells für Python via .NET bietet die Möglichkeit, CSS für das Arbeitsblatt separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwenden Sie dazu die [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)-Eigenschaft und setzen Sie sie beim Speichern der Excel-Datei in HTML auf **true**.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt einen Text in Zelle **B5** in **Rot** hinzu und speichert sie dann im HTML-Format unter Verwendung der [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)-Eigenschaft. Bitte sehen Sie sich das [Ausgabe-HTML](60489766.zip) an, das vom Code generiert wurde. Sie werden **stylesheet.css** innerhalb davon als Ergebnis des Beispielcodes finden.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Einzelarbeitsblatt-Arbeitsmappe in HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells für Python via .NET in HTML konvertiert wird, erstellt sie eine HTML-Datei zusammen mit einem Ordner, der CSS und mehrere HTML-Dateien enthält. Beim Öffnen dieser HTML-Datei im Browser sind die Tabs sichtbar. Das gleiche Verhalten ist auch bei einer Arbeitsmappe mit einem einzelnen Arbeitsblatt erforderlich. Früher wurde für Arbeitsmappen mit nur einem Blatt kein separater Ordner erstellt, sondern nur die HTML-Datei. Diese HTML-Datei zeigt beim Öffnen im Browser keine Tabs. MS Excel erstellt jedoch auch für ein einzelnes Blatt einen ordnungsgemäßen Ordner und HTML, daher ist dieses Verhalten mithilfe der APIs von Aspose.Cells für Python via .NET implementiert worden. Die Beispieldatei kann unter folgendem Link heruntergeladen werden, um im unten angeführten Beispielcode verwendet zu werden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
