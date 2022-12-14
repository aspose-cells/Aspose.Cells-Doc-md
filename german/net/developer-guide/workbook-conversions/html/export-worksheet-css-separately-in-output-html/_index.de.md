---
title: Arbeitsblatt-CSS separat in Ausgabe-HTML exportieren
type: docs
weight: 80
url: /de/net/export-worksheet-css-separately-in-output/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells bietet die Funktion, Arbeitsblatt-CSS separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwende[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) Eigenschaft für diesen Zweck und setzen Sie sie auf**Stimmt** beim Speichern einer Excel-Datei im HTML-Format.

## **Arbeitsblatt-CSS separat in Ausgabe-HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei und fügt etwas Text in die Zelle ein**B5** in**Rot** Farbe und speichert es dann im HTML-Format mit[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)Eigentum. Bitte sehen Sie sich ... an[HTML ausgeben](60489766.zip) generiert durch den Code als Referenz. Du wirst finden**stylesheet.css**darin als Ergebnis des Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportieren Sie eine Einzelblatt-Arbeitsmappe in HTML**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells in HTML konvertiert wird, wird eine HTML-Datei zusammen mit einem Ordner erstellt, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten ist für eine Arbeitsmappe mit einem einzelnen Arbeitsblatt erforderlich, wenn sie in HTML konvertiert wird. Früher wurde kein separater Ordner für Einzelblatt-Arbeitsmappen erstellt und es wurde nur eine HTML-Datei erstellt. Eine solche HTML-Datei zeigt keine Registerkarte, wenn sie im Browser geöffnet wird. MS Excel erstellt auch den richtigen Ordner und HTML für ein einzelnes Blatt, und daher wird das gleiche Verhalten mit Aspose.Cells-APIs implementiert. Die Beispieldatei kann über den folgenden Link heruntergeladen werden, um sie im folgenden Beispielcode zu verwenden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
