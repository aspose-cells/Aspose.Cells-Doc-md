---
title: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/python-net/get-max-index-in-row-and-column/
description: Erfahren Sie, wie Sie den maximalen Spaltenindex in einer Zeile und den maximalen Zeilenindex in einer Spalte über die Aspose.Cells für Python via .NET API erhalten können.
keywords: Python Excel Bibliothek, Python den maximalen Spaltenindex in einer Zeile erhalten, Python den maximalen Zeilenindex in einer Spalte erhalten, Python den maximalen Daten Spaltenindex in einer Zeile erhalten, Python den maximalen Datenzeilenindex in einer Spalte erhalten. 
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten in den Zeilen oder Spalten bearbeiten müssen, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Aspose.Cells für Python via .NET bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die Eigenschaften [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) und [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/) abrufen und dann die Eigenschaft [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) verwenden, um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu erhalten. Aber um den maximalen Zeilenindex und den maximalen Zeilendatenindex in einer Spalte zu erhalten, müssen Sie einen Bereich in der Spalte erstellen, dann den Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich die Eigenschaft [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) auf der Zelle abrufen.

Aspose.Cells für Python via .NET bietet die folgenden Eigenschaften und Methoden, um Ihre Ziele zu erreichen.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Den maximalen Spaltenindex in einer Zeile und den maximalen Zeilenindex in einer Spalte mithilfe der Aspose.Cells für Python-Excel-Bibliothek erhalten**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Die Eigenschaft [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) auf der Zelle abrufen.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Die Eigenschaft [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) auf der Zelle abrufen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
{{< app/cells/assistant language="python-net" >}}
