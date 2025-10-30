---
title: Entfernen Sie führende leere Zeilen und Spalten beim Exportieren von Tabellen in CSV Format mit Golang via C++
linktitle: Entferne führende leere Zeilen und Spalten
type: docs
weight: 100
url: /de/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lerne, wie du führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen im CSV Format mit Aspose.Cells for C++ trimmen kannst.
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält deine Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Zum Beispiel, diese Zeile:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig verwirft Aspose.Cells keine führenden leeren Spalten und Zeilen beim Speichern, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel tut, bietet Aspose.Cells die [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/)-Eigenschaft. Bitte setzen Sie sie auf **true**, dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for C++ 20.4 war der Standardwert von [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) **false**. Seit der Version 20.4 ist der Standardwert von [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die zwei führende leere Spalten hat. Zuerst speichert die Excel-Datei im CSV-Format ohne Änderungen und dann setzt es die [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/)-Eigenschaft auf **true** und speichert sie erneut. Der Screenshot zeigt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die [Ausgabe-CSV-Datei ohne Abschneiden](outputWithoutTrimBlankColumns.csv) und die [Ausgabe-CSV-Datei mit Abschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
