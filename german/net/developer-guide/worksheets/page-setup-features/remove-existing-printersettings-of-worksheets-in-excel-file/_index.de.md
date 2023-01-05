---
title: Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in einer Excel-Datei
type: docs
weight: 60
url: /de/net/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel eingeschlossen wird*.Behälter* Dateien mit Druckereinstellungen in den gespeicherten XLSX-Dateien. Druckereinstellungsdateien befinden sich unter*„[Datei „root“]\xl\printerSettings“.* In diesem Dokument wird erläutert, wie Sie vorhandene Druckereinstellungen mithilfe von Aspose.Cells-APIs entfernen.
## **Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in einer Excel-Datei**
Aspose.Cells ermöglicht es Ihnen, vorhandene Druckereinstellungen zu entfernen, die für verschiedene Blätter in der Excel-Datei festgelegt wurden. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte sehen Sie es sich an[Beispiel-Excel-Datei](45056020.xlsx), [Excel-Datei ausgeben](45056021.xlsx), Konsolenausgabe sowie den Screenshot als Referenz.
## **Bildschirmfoto**
![todo: Bild_alt_Text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Konsolenausgabe**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
