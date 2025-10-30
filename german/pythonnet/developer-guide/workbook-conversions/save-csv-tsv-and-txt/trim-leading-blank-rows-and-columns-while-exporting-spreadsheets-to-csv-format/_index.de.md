---
title: Abschneiden führender Leerzeilen und spalten beim Exportieren von Tabellenkalkulationen in das CSV Format
type: docs
weight: 100
url: /de/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen im CSV Format unter Verwendung der Aspose.Cells für Python via .NET API.
keywords: Python Führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen im CSV Format trimmen, Führende leere Zeilen und Spalten beim Speichern von Excel im CSV Format in Python via NET, Python Führende leere Zeilen und Spalten beim Exportieren von Excel ins CSV Format.
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Beispielweise betrachten Sie diese Zeile

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig verwirft Aspose.Cells for Python via .NET keine führenden leeren Spalten und Zeilen beim Speichern, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel tut, bietet Aspose.Cells for Python via .NET die [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)-Eigenschaft. Bitte setzen Sie sie auf **true**, dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for Python via .NET 20.4 war der Standardwert von [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) **false**. Seit der Veröffentlichung von 20.4 ist der Standardwert von [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die zwei führende leere Spalten hat. Zuerst speichert die Excel-Datei im CSV-Format ohne Änderungen und dann setzt es die [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)-Eigenschaft auf **true** und speichert sie erneut. Der Screenshot zeigt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die [Ausgabe-CSV-Datei ohne Abschneiden](outputWithoutTrimBlankColumns.csv) und die [Ausgabe-CSV-Datei mit Abschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
