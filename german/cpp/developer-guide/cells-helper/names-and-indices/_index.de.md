---
title: Namen und Indizes
type: docs
weight: 10
url: /de/cpp/names-and-indices/
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells bietet die Methode [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/), mit der Entwickler den Namen einer Zelle erhalten können, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) verwendet wird, um den Namen einer Zelle anhand eines bekannten Zeilen- und Spaltenindex abzurufen. Der Code gibt die folgende Ausgabe aus.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells bietet die Methode [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/), mit der Entwickler den Zeilen- und Spaltenindex aus dem Zellnamen erhalten können.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) verwendet wird, um den Zeilen- und Spaltenindex aus dem Zellnamen zu erhalten. Der Code gibt die folgende Ausgabe aus.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
