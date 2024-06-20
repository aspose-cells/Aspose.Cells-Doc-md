---
title: Entfernen Sie vorhandene Dokumenteinstellungen der Arbeitsblätter in der Excel Datei
type: docs
weight: 40
url: /de/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel die *.bin*-Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einschließt. Druckereinstellungsdateien befinden sich unter *“[Datei "root"]\xl\printerSettings”*. Dieses Dokument erläutert, wie vorhandene Druckereinstellungen mithilfe von Aspose.Cells-APIs entfernt werden können.
## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells ermöglicht es Ihnen, vorhandene Druckereinstellungen für verschiedene Blätter in der Excel-Datei zu entfernen. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte beachten Sie die [Beispiel-Excel-Datei](45056023.xlsx), [Ausgabe-Excel-Datei](45056024.xlsx), die Konsolenausgabe sowie einen Screenshot zur Referenz.
## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Konsolenausgabe**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
