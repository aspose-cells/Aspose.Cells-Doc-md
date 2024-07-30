---
title: Entfernen Sie vorhandene Dokumenteinstellungen der Arbeitsblätter in der Excel Datei
type: docs
weight: 60
url: /de/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In diesem Artikel erfahren Sie, wie Sie vorhandene Druckereinstellungen des Arbeitsblatts in der Excel Datei programmgesteuert durch das Seiteneinrichtungsobjekt mithilfe des Beispielscodes von Aspose.Cells für die Python Excel Bibliothek entfernen können.
keywords: Python Excel Bibliothek, Python Entfernen Sie Druckereinstellungen des Arbeitsblatts, Python Entfernen Sie Druckereinstellungen des Excel Arbeitsblatts.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel die *.bin*-Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einschließt. Druckereinstellungsdateien befinden sich unter *"[Datei \"root\"]\xl\printerSettings".* Dieses Dokument erläutert, wie Sie vorhandene Druckereinstellungen mithilfe der Aspose.Cells-APIs für Python via .NET entfernen können.

## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells für Python via .NET erlaubt es Ihnen, vorhandene Druckereinstellungen für verschiedene Arbeitsblätter in der Excel-Datei zu entfernen. Der folgende Beispielcode veranschaulicht, wie Sie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernen können. Sehen Sie sich die [Beispiel-Excel-Datei](45056020.xlsx), die [Ausgabedatei Excel](45056021.xlsx), die Konsolenausgabe sowie den Screenshot als Referenz an.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
