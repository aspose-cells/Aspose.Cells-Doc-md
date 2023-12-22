---
title: Holen Sie sich den Index Cells
type: docs
weight: 600
url: /de/net/get-cells-index/
description: Erfahren Sie, wie Sie Zeilen oder Spalten anhand des Zeilen-, Spalten- oder Zellennamens eingeben. Konvertieren Sie den Namen der Zelle in einen nullbasierten Zeilen- und Spaltenindex.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Die Standardansicht von Excel ist die Referenz im A1-Stil. Jede Spalte ist als A, B, C... definiert, und die Zellen werden als A1, B2, C3... usw. bezeichnet.
Möglicherweise möchten Sie wissen, in welcher Zeile und Spalte sich diese Zelle befindet.

{{% /alert %}}


##  **Mögliche Nutzungsszenarien**
 Wenn Sie bestimmte Daten im Arbeitsblatt nur anhand des Zeilen- und Spaltenindex bearbeiten müssen, müssen Sie die Spalten- und Spaltenindizes dieser bestimmten Zelle kennen.
 Aspose.Cells bietet diese Funktion, um den Zeilen- und Spaltenindex anhand des Namens der Zeile, Spalte und Zelle abzurufen.
Aspose.Cells bietet die folgenden Eigenschaften und Methoden, die Ihnen beim Erreichen Ihrer Ziele helfen.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Hinweis: Die Indizierung ist in Aspose.Cells für .Net nullbasiert, aber die ID von Row ist in MS Excel einsbasiert.

##  **Rufen Sie Cells-Indizes mit Aspose.Cells ab**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie eine Arbeitsmappe und fügen Sie einige Daten hinzu.
1. Suchen Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Rufen Sie den Zeilenindex und den Spaltenindex anhand des Namens der Zelle ab.
1. Rufen Sie den Spaltenindex anhand des Namens der Spalte ab.
1. Zeilenindex anhand des Zeilennamens abrufen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}