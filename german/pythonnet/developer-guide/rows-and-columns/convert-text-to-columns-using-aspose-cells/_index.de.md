---
title: Text in Spalten konvertieren mithilfe von Aspose.Cells
type: docs
weight: 30
url: /de/python-net/convert-text-to-columns-using-aspose-cells/
description: Dieser Artikel zeigt, wie man Text in Spalten umwandelt mit der Aspose.Cells für Python via .NET API.
keywords: Python Excel Bibliothek, Python Text in Spalten umwandeln, Text in Spalten umwandeln in Python.
---

## **Mögliche Verwendungsszenarien**

Sie können Ihren Text in Spalten mit Microsoft Excel umwandeln. Diese Funktion ist unter * Daten * im Reiter * Daten Tools * verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, muss die Daten einen bestimmten Trennzeichen wie ein Komma (oder ein anderes Zeichen) enthalten, anhand dessen Microsoft Excel den Inhalt einer Zelle in mehrere Zellen aufteilt. Aspose.Cells für Python via .NET bietet diese Funktion ebenfalls über die [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) Methode an.

## **Text in Spalten umwandeln mit Aspose.Cells für die Python Excel Bibliothek**

Der folgende Beispielscode erläutert die Verwendung der [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) Methode. Der Code fügt zuerst einige Personennamen in Spalte A des ersten Arbeitsblatts hinzu. Der Vor- und Nachname ist durch ein Leerzeichen getrennt. Dann wendet er die [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) Methode auf Spalte A an und speichert es als Ausgabedatei Excel. Wenn Sie die [Ausgabedatei Excel](25395213.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A stehen, während die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
