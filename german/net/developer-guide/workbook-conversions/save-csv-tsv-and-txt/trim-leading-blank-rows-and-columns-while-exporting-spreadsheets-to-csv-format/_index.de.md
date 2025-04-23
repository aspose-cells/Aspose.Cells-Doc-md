---
title: Abschneiden führender Leerzeilen und spalten beim Exportieren von Tabellenkalkulationen in das CSV Format
type: docs
weight: 100
url: /de/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Beispielweise betrachten Sie diese Zeile

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig verwirft Aspose.Cells keine führenden leeren Spalten und Zeilen beim Speichern, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel tut, bietet Aspose.Cells die [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)-Eigenschaft. Bitte setzen Sie sie auf **true**, dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for .NET 20.4 war der Standardwert für [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) **false**. Seit der Version 20.4 ist der Standardwert für [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die zwei führende leere Spalten hat. Zuerst speichert die Excel-Datei im CSV-Format ohne Änderungen und dann setzt es die [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)-Eigenschaft auf **true** und speichert sie erneut. Der Screenshot zeigt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die [Ausgabe-CSV-Datei ohne Abschneiden](outputWithoutTrimBlankColumns.csv) und die [Ausgabe-CSV-Datei mit Abschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
