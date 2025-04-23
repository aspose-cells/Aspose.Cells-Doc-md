---
title: Zellenindex erhalten
type: docs
weight: 600
url: /de/net/get-cells-index/
description: Erfahren Sie, wie Sie Zeilen oder Spalten mithilfe des Namens von Zeile, Spalte oder Zellen erhalten. Konvertieren Sie den Namen der Zelle in den nullbasierten Zeilen und Spaltenindex.
keywords: Zeilen und Spaltenindex nach dem Namen der Zelle erhalten, Spaltenindex nach dem Namen der Spalte erhalten, Zeilenindex nach dem Namen der Zeile erhalten, Index nach dem Namen der Zelle erhalten. 
---

{{% alert color="primary" %}}
Die Standardansicht von Excel ist das A1-Stil-Bezugssystem. Jede Spalte ist als A, B, C...definiert und die Zellen sind als A1, B2, C3... usw. bezeichnet.
Sie möchten vielleicht wissen, welche Zeile und Spalte diese Zelle ist.

{{% /alert %}}


## **Mögliche Verwendungsszenarien**
Wenn Sie nur eine bestimmte Daten auf dem Arbeitsblatt mit Zeilen- und Spaltenindex manipulieren müssen, müssen Sie die Spalten- und Zeilenindizes dieser bestimmten Zelle kennen. 
Aspose.Cells bietet diese Funktion, um den Zeilen- und Spaltenindex nach dem Namen der Zeile, Spalte und Zelle zu erhalten. 
Aspose.Cells bietet die folgenden Eigenschaften und Methoden, um Ihnen bei Ihren Zielen zu helfen.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Hinweis: Die Indizierung ist in Aspose.Cells für .NET nullbasiert, aber die ID der Zeile ist in MS Excel einsbasiert.

## **Zellenindizes mithilfe von Aspose.Cells abrufen**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Finden Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Holen Sie sich den Zeilenindex und Spaltenindex nach dem Namen der Zelle.
1. Holen Sie sich den Spaltenindex nach dem Namen der Spalte.
1. Holen Sie sich den Zeilenindex nach dem Namen der Zeile.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
{{< app/cells/assistant language="csharp" >}}
