---
title: Schneiden Sie führende leere Zeilen und Spalten beim Exportieren von Tabellen in das Format CSV ab
type: docs
weight: 100
url: /de/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Schneiden Sie führende leere Zeilen und Spalten ab, während Sie Tabellenkalkulationen in das Format CSV exportieren, indem Sie Aspose.Cells for Python via .NET API verwenden.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Mögliche Nutzungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Betrachten Sie zum Beispiel diese Zeile

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

 Standardmäßig verwirft Aspose.Cells for Python via .NET führende leere Spalten und Zeilen beim Speichern nicht. Wenn Sie sie jedoch genauso entfernen möchten wie Microsoft Excel, dann bietet Aspose.Cells for Python via .NET die Möglichkeit**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** Eigentum. Bitte stellen Sie es ein**WAHR**und dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

 Vor der Veröffentlichung von Aspose.Cells for Python via .NET 20.4 war der Standardwert von**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**War**FALSCH**. Seit der Version 20.4 ist der Standardwert von **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** Ist**WAHR.**

{{% /alert %}}

##  **Schneiden Sie führende leere Zeilen und Spalten beim Exportieren von Tabellen in das Format CSV ab**

 Der folgende Beispielcode lädt die[Quell-Excel-Datei](sampleTrimBlankColumns.xlsx) das zwei führende leere Spalten hat. Zunächst wird die Excel-Datei ohne Änderungen im Format CSV gespeichert und dann festgelegt**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** Eigentum zu**WAHR** und speichert es erneut. Der Screenshot zeigt die[Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), [Ausgabe der Datei CSV ohne Zuschneiden](outputWithoutTrimBlankColumns.csv), und das[Ausgabe der Datei CSV mit Zuschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
