---
title: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte mit Golang über C++ abrufen
linktitle: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/go-cpp/get-max-index-in-row-and-column/
description: Lernen Sie, wie man den maximalen Spaltenindex in einer Zeile und den maximalen Zeilenindex in einer Spalte über die API Aspose.Cells for C++ erhält.
keywords: Holen Sie sich den Max Spaltenindex in Zeile, holen Sie sich den Max Zeilenindex in Spalte, holen Sie sich den Max Data Spaltenindex in Zeile, holen Sie sich den Max Data Zeilenindex in Spalte.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten in Zeilen oder Spalten manipulieren müssen, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Aspose.Cells bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die Eigenschaften [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) und [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) abrufen und dann die [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) Eigenschaft verwenden, um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu erhalten. Um den maximalen Zeilenindex und den maximalen Zeilen-Datenindex einer Spalte zu ermitteln, müssen Sie einen Bereich in der Spalte erstellen, den Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich das Attribut [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) der Zelle verwenden.

Aspose.Cells bietet die folgenden Eigenschaften und Methoden, um Ihnen bei Ihren Zielen zu helfen.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Holen Sie sich den Max-Spaltenindex in Zeile und den Max-Zeilenindex in Spalte mit Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Das Attribut [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) der Zelle abrufen.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Das Attribut [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) der Zelle abrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
