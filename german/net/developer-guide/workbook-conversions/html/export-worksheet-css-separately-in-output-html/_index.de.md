---
title: Arbeitsblatt-CSS separat in Ausgabe HTML exportieren
type: docs
weight: 80
url: /de/net/export-worksheet-css-separately-in-output/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells bietet die Funktion zum separaten Exportieren von Arbeitsblatt-CSS, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwenden[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) Eigenschaft für diesen Zweck und setzen Sie sie auf**wahr** beim Speichern der Excel-Datei im Format HTML.

## **Arbeitsblatt-CSS separat in Ausgabe HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei und fügt etwas Text in die Zelle ein**B5** in**Rot**Farbe und speichert es dann im Format HTML mit[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) Eigentum. Bitte sehen Sie sich ... an[Ausgang HTML](60489766.zip) generiert durch den Code als Referenz. Du wirst finden**stylesheet.css**darin als Ergebnis des Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportieren Sie eine Einzelblatt-Arbeitsmappe nach HTML**

Wenn eine Arbeitsmappe mit mehreren Blättern mithilfe von Aspose.Cells in HTML konvertiert wird, wird eine HTML-Datei zusammen mit einem Ordner erstellt, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten ist für eine Arbeitsmappe mit einem einzelnen Arbeitsblatt erforderlich, wenn sie in HTML konvertiert wird. Früher wurde kein separater Ordner für Arbeitsmappen mit einem einzelnen Blatt erstellt, und es wurde nur die Datei HTML erstellt. Eine solche HTML-Datei zeigt keine Registerkarte, wenn sie im Browser geöffnet wird. MS Excel erstellt auch den richtigen Ordner und HTML für ein einzelnes Blatt, und daher wird dasselbe Verhalten mit Aspose.Cells-APIs implementiert. Die Beispieldatei kann über den folgenden Link heruntergeladen werden, um sie im folgenden Beispielcode zu verwenden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
