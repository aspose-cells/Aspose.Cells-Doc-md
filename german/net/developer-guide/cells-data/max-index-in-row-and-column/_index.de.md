---
title: Ermitteln Sie den maximalen Spaltenindex in der Zeile und den maximalen Zeilenindex in der Spalte
type: docs
weight: 600
url: /de/net/get-max-index-in-row-and-column/
description: Erfahren Sie, wie Sie den maximalen Spaltenindex in Zeile und den maximalen Zeilenindex in Spalte über Aspose.Cells for .NET API erhalten.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Mögliche Nutzungsszenarien**
Wenn Sie nur einige Daten in den Zeilen oder Spalten bearbeiten müssen, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Aspose.Cells bietet diese Funktion. Um den maximalen Spaltenindex für eine Zeile zu erhalten, können Sie Folgendes abrufen:[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) Und[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) Eigenschaften und verwenden Sie dann die[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) -Eigenschaft, um den maximalen Spaltenindex und den maximalen Datenspaltenindex zu erhalten. Um jedoch den maximalen Zeilenindex und den maximalen Zeilendatenindex für eine Spalte zu erhalten, müssen Sie einen Bereich für die Spalte erstellen, dann den Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich den Bereich erhalten[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) Attribut für die Zelle.

Aspose.Cells bietet die folgenden Eigenschaften und Methoden, die Ihnen beim Erreichen Ihrer Ziele helfen.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Erhalten Sie den maximalen Spaltenindex in Zeile und den maximalen Zeilenindex in Spalte mit Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1.  Laden Sie die[Beispieldatei](sample.xlsx).
1. Rufen Sie die Zeile ab, die den maximalen Spaltenindex und den maximalen Datenspaltenindex erhalten muss.
1.  Erhalten[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) Attribut für die Zelle.
1. Erstellen Sie einen Bereich basierend auf der Spalte.
1. Holen Sie sich den Iterator und den Durchlaufbereich.
1.  Erhalten[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) Attribut für die Zelle.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}