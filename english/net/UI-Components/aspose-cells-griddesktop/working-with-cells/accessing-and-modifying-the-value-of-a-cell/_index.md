---
title: Accessing  and  Modifying the Value of a Cell
type: docs
weight: 20
url: /net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: This article introduces how to get and modify cell value in GridDesktop.
---

{{% alert color="primary" %}} 

In our previous topic, we have discussed about accessing cells of a worksheet. In this topic, we will simply extend that topic to show developers that how can they access and modify the values of cells using the API of Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Access and Modify Cell Value using Aspose.Cells.GridDesktop**
Before accessing and modifying the value of a cell, we should know that how to access cells. There are three approaches to access cells of a worksheet. For more details about these three approaches, please [Accessing Cells in a Worksheet.](/cells/net/accessing-cells-in-a-worksheet/)

Each cell has a property named Value . So, once a cell is accessed, developers can access and modify the contents of the Value property in order to access and change the value of a cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANT:** Using Value property of a cell to modify its value is a good approach for setting the value of a single or few cells. If you need to set the values of many cells then the performance of this approach would not be good. So, to set the values of many cells, you should use **SetCellValue** method of the cell for improving the performance of your applications. A modified version of the above code snippet using **SetCellValue** method is shown below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
