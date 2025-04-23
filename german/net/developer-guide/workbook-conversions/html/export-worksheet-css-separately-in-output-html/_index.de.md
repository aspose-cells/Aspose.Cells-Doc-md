---
title: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/net/export-worksheet-css-separately-in-output/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Möglichkeit, das Arbeitsblatt-CSS separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwenden Sie die [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)-Eigenschaft für diesen Zweck und setzen Sie sie auf **true**, während Sie die Excel-Datei im HTML-Format speichern.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt einen Text in Zelle **B5** in **Rot** hinzu und speichert sie dann im HTML-Format unter Verwendung der [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)-Eigenschaft. Bitte sehen Sie sich das [Ausgabe-HTML](60489766.zip) an, das vom Code generiert wurde. Sie werden **stylesheet.css** innerhalb davon als Ergebnis des Beispielcodes finden.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Einzelarbeitsblatt-Arbeitsmappe in HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern unter Verwendung von Aspose.Cells in HTML umgewandelt wird, wird eine HTML-Datei zusammen mit einem Ordner erstellt, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten ist erforderlich für eine Arbeitsmappe mit einem einzigen Arbeitsblatt, wenn sie in HTML umgewandelt wird. Früher wurde für Arbeitsmappen mit nur einem Arbeitsblatt kein separater Ordner erstellt und es wurde nur eine HTML-Datei erstellt. Eine solche HTML-Datei zeigt beim Öffnen im Browser keine Registerkarte an. MS Excel erstellt auch einen ordnungsgemäßen Ordner und HTML für ein einzelnes Arbeitsblatt und daher wird dasselbe Verhalten mit Hilfe von Aspose.Cells-APIs implementiert. Die Beispieldatei kann von folgendem Link heruntergeladen werden, um sie im unten stehenden Beispielcode zu verwenden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
