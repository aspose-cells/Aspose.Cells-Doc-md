---
title: Entfernen Sie vorhandene Dokumenteinstellungen der Arbeitsblätter in der Excel Datei
type: docs
weight: 60
url: /de/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In diesem Artikel lernen Sie, wie Sie die bestehenden PrinterSettings eines Arbeitsblatts in der Excel Datei mithilfe des Page Setup Objekts programmgesteuert mit Beispielcode aus der Aspose.Cells für Python Excel Bibliothek entfernen.
keywords: Python Excel Bibliothek, Python, Druckereinstellungen des Arbeitsblatts entfernen, Druckereinstellungen des Excel Arbeitsblatts entfernen.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel *.bin*-Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einschließt. Druckereinstellungen befinden sich unter *“[file "root"]\xl\printerSettings”.* Dieses Dokument erklärt, wie man bestehende Druckereinstellungen mit Aspose.Cells für Python via .NET APIs entfernt.

## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells für Python via .NET ermöglicht es, bestehende Druckereinstellungen, die für verschiedene Blätter in der Excel-Datei festgelegt sind, zu entfernen. Der folgende Beispielcode zeigt, wie alle Druckereinstellungen für alle Arbeitsblätter im Arbeitsbuch entfernt werden. Bitte schauen Sie sich die [Beispieldatei](45056020.xlsx), die [Ausgabedatei](45056021.xlsx), die Konsole-Ausgabe sowie den Screenshot als Referenz an.

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
