---
title: Namen und Indizes
type: docs
weight: 10
url: /de/go-cpp/names-and-indices/
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**

Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells bietet die Methode [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), mit der Entwickler den Namen einer Zelle erhalten können, wenn sie die Zeilen- und Spaltenindizes angeben.

{{% alert color="primary" %}}

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie man [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) verwendet, um den Namen einer Zelle anhand eines bekannten Zeilen- und Spaltenindex abzurufen. Der Code erzeugt die folgende Ausgabe.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**

Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells stellt die Methode [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) bereit, mit der Entwickler den Zeilen- und Spaltenindex aus dem Namen einer Zelle erhalten können.

{{% alert color="primary" %}}

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie man [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) verwendet, um den Zeilen- und Spaltenindex anhand des Zellennamens zu erhalten. Der Code erzeugt die folgende Ausgabe.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
