---
title: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/java/export-worksheet-css-separately-in-output-html/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Möglichkeit, das Arbeitsblatt-CSS separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML konvertieren. Bitte verwenden Sie die Eigenschaft HtmlSaveOptions.ExportWorksheetCSSSeparately für diesen Zweck und setzen Sie sie beim Speichern der Excel-Datei im HTML-Format auf true.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt etwas Text in die Zelle B5 in roter Farbe ein und speichert sie dann im HTML-Format unter Verwendung der Eigenschaft HtmlSaveOptions.ExportWorksheetCSSSeparately. Bitte sehen Sie sich das [Ausgabe-HTML](60489780.zip) an, das vom Code generiert wurde, um eine Referenz zu erhalten. Sie finden darin auch die stylesheet.css als Ergebnis des Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Einzelarbeitsblatt-Arbeitsmappe in HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern unter Verwendung von Aspose.Cells in HTML umgewandelt wird, wird eine HTML-Datei zusammen mit einem Ordner erstellt, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten wird für eine Arbeitsmappe mit einem einzelnen Arbeitsblatt benötigt, wenn sie in HTML umgewandelt wird. Früher wurde kein separater Ordner für Arbeitsmappen mit einem einzigen Blatt erstellt und es wurde nur eine HTML-Datei erstellt. Eine solche HTML-Datei zeigt im Browser keine Registerkarte an. Excel erstellt auch für einzelne Blätter einen ordnungsgemäßen Ordner und HTML und daher wird dasselbe Verhalten unter Verwendung von Aspose.Cells implementiert. Die Beispieldatei kann über den folgenden Link heruntergeladen und im unten stehenden Beispielcode verwendet werden:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
