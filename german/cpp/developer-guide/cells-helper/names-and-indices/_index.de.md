---
title: Namen und Indizes
type: docs
weight: 10
url: /de/cpp/names-and-indices/
---
## **Rufen Sie den Namen Cell aus den Zeilen- und Spaltenindizes ab**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erklärt, wie.
Aspose.Cells stellt die ICellsHelper.CellIndexToName_i-Methode bereit, die es Entwicklern ermöglicht, den Namen einer Zelle abzurufen, wenn sie den Zeilen- und Spaltenindex bereitstellen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung von ICellsHelper.CellIndexToName_i für den Zugriff auf den Namen einer Zelle bei einem bekannten Zeilen- und Spaltenindex. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Rufen Sie Zeilen- und Spaltenindizes von Cell Name ab**
Es ist möglich, einen Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erklärt, wie.
Aspose.Cells stellt die ICellsHelper.CellNameToIndex_i-Methode bereit, die es Entwicklern ermöglicht, einen Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie CellsHelper.CellNameToIndex verwendet wird, um den Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
