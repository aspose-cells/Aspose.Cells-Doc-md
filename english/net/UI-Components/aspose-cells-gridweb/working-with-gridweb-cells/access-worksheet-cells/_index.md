---
title: Access Worksheet Cell
type: docs
weight: 10
url: /net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: This article introduces how to get cell (GridCell) in GridWeb.
---

{{% alert color="primary" %}} 

This topic discusses cells, looking at Aspose.Cells.GridWeb's most basic feature: accessing cells.

{{% /alert %}} 
## **Accessing Cells in a Worksheet**
Each worksheet contains a property by the name of Cells that is actually a collection of GridCell objects where a GridCell object represents a cell in Aspose.Cells.GridWeb. It is possible to access any cell using Aspose.Cells.GridWeb. There are two preferred methods, each of which is discussed below.


### **Using Cell Name**
All cells have a unique name. For example, A1, A2, B1, B2 etc. Aspose.Cells.GridWeb allows developers to access any desired cell by using the cell name. Simply pass the cell name (as an index) to the Cells collection of the GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Using Row & Column Indices**
A cell can also be recognized by its location in terms of row and column indices. Just pass a cell's row and column indices to the Cells collection of the GridWorksheet. This approach is more faster than the above one.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
