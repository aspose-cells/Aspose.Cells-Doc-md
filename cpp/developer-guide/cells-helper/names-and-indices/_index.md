---
title: Names and Indices
type: docs
weight: 10
url: /cpp/names-and-indices/
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.
Aspose.Cells provides the ICellsHelper.CellIndexToName_i method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use ICellsHelper.CellIndexToName_i to access the a cell's name given a known row and column index. The code generates the following output.



{{< gist "aspose-cells" "9f351edfebf7c0f682eedd4dec8eb98c" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.
Aspose.Cells provides the ICellsHelper.CellNameToIndex_i method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use CellsHelper.CellNameToIndex to get the row and column index from the cell's name. The code generates the following output.



{{< gist "aspose-cells" "9f351edfebf7c0f682eedd4dec8eb98c" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
