---
title: Arbeitsblatt-CSS separat in Ausgabe HTML exportieren
type: docs
weight: 80
url: /de/java/export-worksheet-css-separately-in-output-html/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells bietet die Funktion, Arbeitsblatt-CSS separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwenden Sie die Eigenschaft HtmlSaveOptions.ExportWorksheetCSSSeparately für diesen Zweck und setzen Sie sie auf true, während Sie die Excel-Datei im HTML-Format speichern.

## **Arbeitsblatt-CSS separat in Ausgabe HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt Text in Zelle B5 in roter Farbe hinzu und speichert ihn dann im Format HTML mithilfe der Eigenschaft HtmlSaveOptions.ExportWorksheetCSSSeparately. Bitte sehen Sie sich ... an[Ausgang HTML](60489780.zip)generiert durch den Code für eine Referenz. Als Ergebnis des Beispielcodes finden Sie stylesheet.css darin.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exportieren Sie eine Einzelblatt-Arbeitsmappe nach HTML**

Wenn eine Arbeitsmappe mit mehreren Blättern mithilfe von Aspose.Cells in HTML konvertiert wird, wird eine HTML-Datei zusammen mit einem Ordner erstellt, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten ist für eine Arbeitsmappe mit einem einzelnen Arbeitsblatt erforderlich, wenn sie in HTML konvertiert wird. Früher wurde kein separater Ordner für Arbeitsmappen mit einem einzelnen Blatt erstellt, und es wurde nur die Datei HTML erstellt. Eine solche HTML-Datei zeigt keine Registerkarte, wenn sie im Browser geöffnet wird. Excel erstellt den richtigen Ordner und HTML auch für einzelne Blätter, und daher wird das gleiche Verhalten mit Aspose.Cells implementiert. Die Beispieldatei kann über den folgenden Link heruntergeladen werden, um sie im folgenden Beispielcode zu verwenden:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
