---
title: Abschneiden führender Leerzeilen und spalten beim Exportieren von Tabellenkalkulationen in das CSV Format
type: docs
weight: 50
url: /de/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Beispielweise betrachten Sie diese Zeile

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig verwirft Aspose.Cells keine führenden leeren Spalten und Zeilen beim Speichern, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel tut, bietet Aspose.Cells die [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)-Eigenschaft. Bitte setzen Sie sie auf **true**, dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for .NET 20.4 war der Standardwert für [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) **false**. Seit der Version 20.4 ist der Standardwert für [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielscode lädt die Quell-Excel-Datei, die zwei führende leere Spalten hat. Zuerst speichert er die Excel-Datei im CSV-Format ohne Änderungen und dann setzt er die [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)-Eigenschaft auf **true** und speichert sie erneut. Der Screenshot zeigt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), [Ausgabedatei im CSV-Format ohne Abschneiden](outputWithoutTrimBlankColumns.csv) und die [Ausgabedatei im CSV-Format mit Abschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
