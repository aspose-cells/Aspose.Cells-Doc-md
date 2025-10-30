---
title: Exportiere Arbeitsblatt CSS separat im Ausgabes HTML mit Golang via C++
linktitle: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/go-cpp/export-worksheet-css-separately-in-output/
description: Erfahren Sie, wie Sie Tabellen CSS beim Konvertieren von Excel Dateien nach HTML separat exportieren, indem Sie Aspose.Cells for C++ verwenden.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Funktion, Tabellen-CSS beim Konvertieren Ihrer Excel-Datei nach HTML separat zu exportieren. Verwenden Sie dazu die [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)-Eigenschaft und setzen Sie sie beim Speichern der Excel-Datei im HTML-Format auf **true**.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt einen Text in Zelle **B5** in **Rot** hinzu und speichert sie dann im HTML-Format unter Verwendung der [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)-Eigenschaft. Bitte sehen Sie sich das [Ausgabe-HTML](60489766.zip) an, das vom Code generiert wurde. Sie werden **stylesheet.css** innerhalb davon als Ergebnis des Beispielcodes finden.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Einzelnes Blatt-Workbook nach HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells nach HTML konvertiert wird, erstellt sie eine HTML-Datei sowie einen Ordner mit CSS und mehreren HTML-Dateien. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Tabs sichtbar. Das gleiche Verhalten ist für eine Arbeitsmappe mit nur einem Arbeitsblatt erforderlich. Früher wurde für einzelne Blätter kein separater Ordner erstellt; es wurde nur eine HTML-Datei erzeugt. Diese HTML-Datei zeigt beim Öffnen im Browser keinen Tab. Microsoft Excel erstellt ebenfalls einen passenden Ordner und HTML für ein einzelnes Blatt, daher ist das gleiche Verhalten über Aspose.Cells APIs implementiert. Die Beispieldatei kann für die Verwendung im untenstehenden Beispielcode heruntergeladen werden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
