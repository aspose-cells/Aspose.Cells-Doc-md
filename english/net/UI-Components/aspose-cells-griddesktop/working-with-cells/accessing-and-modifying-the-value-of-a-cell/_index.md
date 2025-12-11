---
title: Accessing and Modifying the Value of a Cell
type: docs
weight: 20
url: /net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: This article introduces how to get and modify cell value in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In our previous topic, we discussed accessing cells of a worksheet. In this topic, we will simply extend that topic to show developers how they can access and modify the values of cells using the API of Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Access and Modify Cell Values using Aspose.Cells.GridDesktop**
Before accessing and modifying the value of a cell, we should know how to access cells. There are three approaches to access cells of a worksheet. For more details about these three approaches, please [Accessing Cells in a Worksheet.](/cells/net/accessing-cells-in-a-worksheet/)

Each cell has a property named **Value**. So, once a cell is accessed, developers can modify the contents of the **Value** property in order to change the value of a cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANT:** Using the **Value** property of a cell to modify its value is a good approach for setting the value of a single or a few cells. If you need to set the values of many cells, then the performance of this approach would not be good. Therefore, to set the values of many cells, you should use the **SetCellValue** method of the cell to improve the performance of your applications. A modified version of the above code snippet using the **SetCellValue** method is shown below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
