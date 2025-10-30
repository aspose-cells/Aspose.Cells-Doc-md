---
title: Zellenindex mit Golang über C++ erhalten
linktitle: Zellenindex erhalten
type: docs
weight: 600
url: /de/go-cpp/get-cells-index/
description: Lernen Sie, wie man die Zeilen oder Spaltenindex anhand des Namens der Zeile, Spalte oder Zelle erhält. Den Namen der Zelle mithilfe von Aspose.Cells mit Golang über C++ in einen nullbasierten Zeilen und Spaltenindex umwandeln.
keywords: Zeilen und Spaltenindex nach dem Namen der Zelle erhalten, Spaltenindex nach dem Namen der Spalte erhalten, Zeilenindex nach dem Namen der Zeile erhalten, Index nach dem Namen der Zelle erhalten.
---

{{% alert color="primary" %}}
Die Standardansicht von Excel ist die A1-Referenz. Dabei ist jede Spalte als A, B, C... definiert, und die Zellen sind als A1, B2, C3... benannt.
 Sie möchten vielleicht wissen, in welcher Zeile und Spalte sich diese Zelle befindet.

{{% /alert %}}

## **Mögliche Verwendungsszenarien**

 Wenn Sie nur bestimmte Daten im Arbeitsblatt anhand von Zeilen- und Spaltenindex manipulieren möchten, müssen Sie die Zeilen- und Spaltenindizes dieser speziellen Zelle kennen.
 Aspose.Cells bietet diese Funktion, um Zeilen- und Spaltenindex anhand des Namens der Zeile, Spalte und Zelle zu ermitteln.
 Aspose.Cells stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Hinweis: Die Indizierung ist nullbasiert in Aspose.Cells for C++, aber die ID der Zeile ist einsbasiert in MS Excel.

## **Zellenindizes mithilfe von Aspose.Cells abrufen**

Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Finden Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Holen Sie sich den Zeilenindex und Spaltenindex nach dem Namen der Zelle.
1. Holen Sie sich den Spaltenindex nach dem Namen der Spalte.
1. Holen Sie sich den Zeilenindex nach dem Namen der Zeile.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
