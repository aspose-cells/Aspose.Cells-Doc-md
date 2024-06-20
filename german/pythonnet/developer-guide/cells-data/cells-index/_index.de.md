---
title: Zellenindex erhalten
type: docs
weight: 600
url: /de/python-net/get-cells-index/
description: Lernen Sie, wie Sie die Zeile oder Spalte anhand des Namens der Zeile durch die Aspose.Cells for Python via .NET API erhalten, Spalte oder Zellen. Konvertieren Sie den Namen der Zelle in den nullbasierten Zeilen und Spaltenindex durch die Aspose.Cells for Python via .NET API.
keywords: Python Excel, Zeilenindex und Spaltenindex nach Namen der Zelle mit Python abrufen, Spaltenindex nach Namen der Spalte mit Python abrufen, Zeilenindex nach Namen der Zeile mit Python abrufen, Index nach Namen der Zelle mit Python abrufen. 
---

{{% alert color="primary" %}}
Die Standardansicht von Excel ist das A1-Stil-Bezugssystem. Jede Spalte ist als A, B, C...definiert und die Zellen sind als A1, B2, C3... usw. bezeichnet.
Sie möchten vielleicht wissen, welche Zeile und Spalte diese Zelle ist.

{{% /alert %}}


## **Mögliche Verwendungsszenarien**
Wenn Sie nur eine bestimmte Daten auf dem Arbeitsblatt mit Zeilen- und Spaltenindex manipulieren müssen, müssen Sie die Spalten- und Zeilenindizes dieser bestimmten Zelle kennen. 
Aspose.Cells für Python via .NET bietet diese Funktion, um den Zeilen- und Spaltenindex nach dem Namen der Zeile, Spalte und Zelle zu erhalten. 
Aspose.Cells für Python via .NET bietet die folgenden Eigenschaften und Methoden, um Ihre Ziele zu erreichen.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Hinweis: Die Indizierung erfolgt in Aspose.Cells für Python via .NET nullbasiert, aber die ID der Zeile ist in MS Excel einsbasiert.

## **Holen Sie sich Zellenindizes mit der Aspose.Cells for Python Excel-Bibliothek**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Finden Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Holen Sie sich den Zeilenindex und Spaltenindex nach dem Namen der Zelle.
1. Holen Sie sich den Spaltenindex nach dem Namen der Spalte.
1. Holen Sie sich den Zeilenindex nach dem Namen der Zeile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
