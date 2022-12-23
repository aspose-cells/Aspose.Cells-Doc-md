---
title: Trimmen Sie führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen in das Format CSV
type: docs
weight: 100
url: /de/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Mögliche Nutzungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Betrachten Sie beispielsweise diese Zeile

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft-Excel öffnen, verwirft Microsoft-Excel diese führenden leeren Zeilen und Spalten.

 Standardmäßig verwirft Aspose.Cells führende leere Spalten und Zeilen beim Speichern nicht, aber wenn Sie sie entfernen möchten, genau wie Microsoft Excel, dann bietet Aspose.Cells**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** Eigentum. Bitte setzen Sie es auf**wahr**und dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

 Vor der Veröffentlichung von Aspose.Cells for .NET 20.4 war der Standardwert von**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** war**FALSCH** . Seit Version 20.4 ist der Standardwert von**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** ist**WAHR.**

{{% /alert %}}

## **Trimmen Sie führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen in das Format CSV**

 Der folgende Beispielcode lädt die[Excel-Quelldatei](sampleTrimBlankColumns.xlsx) die zwei führende leere Spalten hat. Es speichert zuerst die Excel-Datei im Format CSV ohne Änderungen und setzt dann**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** Eigentum zu**wahr** und speichert es wieder. Der Screenshot zeigt die[Excel-Quelldatei](sampleTrimBlankColumns.xlsx), [Ausgabe CSV Datei ohne Trimmen](outputWithoutTrimBlankColumns.csv), und die[Ausgabe CSV Datei mit Beschnitt](outputTrimBlankColumns.csv).

![todo: Bild_alt_Text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
