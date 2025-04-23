---
title: Entfernen Sie vorhandene Dokumenteinstellungen der Arbeitsblätter in der Excel Datei
type: docs
weight: 60
url: /de/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In diesem Artikel erfahren Sie, wie Sie vorhandene Druckereinstellungen des Arbeitsblatts innerhalb der Excel Datei programmgesteuert durch das Page Setup Objekt mit Beispielcode mithilfe von C# API oder .NET Bibliothek entfernen.
keywords: Druckereinstellungen des Arbeitsblatts in c# entfernen, Druckereinstellungen des Excel Arbeitsblatts in c# entfernen
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel * .bin * -Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einführt. Druckereinstellungsdateien befinden sich unter * "[Datei \"Root \ "] \ xl \ printerSettings ".* Dieses Dokument erläutert, wie vorhandene Druckereinstellungen mithilfe von Aspose.Cells-APIs entfernt werden.
## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells ermöglicht es Ihnen, vorhandene Druckereinstellungen für verschiedene Arbeitsblätter in der Excel-Datei zu entfernen. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte beachten Sie die [Beispiel-Excel-Datei](45056020.xlsx), [Ausgabedatei](45056021.xlsx), Konsolenausgabe sowie den Screenshot zur Referenz.
## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Konsolenausgabe**
{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
