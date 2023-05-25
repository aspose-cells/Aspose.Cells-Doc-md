---
title: Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in der Excel-Datei
type: docs
weight: 60
url: /de/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In diesem Artikel erfahren Sie, wie Sie vorhandene Druckereinstellungen des Arbeitsblatts in der Excel-Datei über das Objekt „Seite einrichten“ programmgesteuert mit Beispielcode unter Verwendung der Bibliothek C#, API oder .NET entfernen.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **Mögliche Nutzungsszenarien**
Manchmal möchten Entwickler die Einbindung von Excel verhindern*.Behälter* Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien. Die Dateien mit den Druckereinstellungen befinden sich darunter*„[Datei „root“]\xl\printerSettings“.* In diesem Dokument wird erläutert, wie Sie vorhandene Druckereinstellungen mithilfe der APIs Aspose.Cells entfernen.
##  **Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Mit Aspose.Cells können Sie vorhandene Druckereinstellungen entfernen, die für verschiedene Blätter in der Excel-Datei angegeben wurden. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte sehen Sie es sich an[Beispiel-Excel-Datei](45056020.xlsx), [Excel-Datei ausgeben](45056021.xlsx)Konsolenausgabe sowie der Screenshot als Referenz.
##  **Bildschirmfoto**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **Konsolenausgabe**
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
