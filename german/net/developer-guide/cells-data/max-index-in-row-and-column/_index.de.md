---
title: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/net/get-max-index-in-row-and-column/
description: Erfahren Sie, wie Sie den Max Spaltenindex in Zeile und den Max Zeilenindex in Spalte über die Aspose.Cells for .NET API erhalten.
keywords: Holen Sie sich den Max Spaltenindex in Zeile, holen Sie sich den Max Zeilenindex in Spalte, holen Sie sich den Max Data Spaltenindex in Zeile, holen Sie sich den Max Data Zeilenindex in Spalte. 
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten in den Zeilen oder Spalten manipulieren müssen, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Aspose.Cells bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die Eigenschaften [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) und [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) erhalten und dann die Eigenschaft [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) verwenden, um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu erhalten. Um jedoch den maximalen Zeilenindex und den maximalen Zeilen-Datenindex in einer Spalte zu erhalten, müssen Sie einen Bereich in der Spalte erstellen, dann den Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich das Attribut [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) auf dem Zelle erhalten.

Aspose.Cells bietet die folgenden Eigenschaften und Methoden, um Ihnen bei Ihren Zielen zu helfen.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Holen Sie sich den Max-Spaltenindex in Zeile und den Max-Zeilenindex in Spalte mit Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Das Attribut [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) auf der Zelle erhalten.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Holen Sie sich das Attribut [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) der Zelle.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
{{< app/cells/assistant language="csharp" >}}
