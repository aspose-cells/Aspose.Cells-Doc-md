---
title : "Names and Indices" 
description : "" 
weight : 12053 
toc : false
type: docs
url: /cpp/developerguide/helper/names+and+indices/
---

# Aspose.Cells for C++ : Names and Indices


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Get Cell Name from Row and Column Indices](#get-cell-name-from-row-and-column-indices)
*   2 [Get Row and Column Indices from Cell Name](#get-row-and-column-indices-from-cell-name)
{{< /panel >}}
 

## Get Cell Name from Row and Column Indices

It is possible to find a cell's name given the row and column index. This article explains how.  
Aspose.Cells provides the `ICellsHelper.CellIndexToName_i` method which allows developers to get a cell's name if they provide the row and column index.

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

The following sample code illustrates how to use `ICellsHelper.CellIndexToName_i` to access the a cell's name given a known row and column index. The code generates the following output.

## Get Row and Column Indices from Cell Name

It is possible to find a row and column index of the cell from its name. This article explains how.  
Aspose.Cells provides the `ICellsHelper.CellNameToIndex_i` method which allows developers to get a row and column index from the cell's name.

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

The following sample code illustrates how to use `CellsHelper.CellNameToIndex` to get the row and column index from the cell's name. The code generates the following output.

