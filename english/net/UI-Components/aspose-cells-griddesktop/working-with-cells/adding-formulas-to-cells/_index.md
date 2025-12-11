---
title: Adding Formula to Cell
type: docs
weight: 30
url: /net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop,formula
description: This article introduces how to get or set a formula in a cell in the worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

A cell can contain not only a simple value like a numeric figure or some text, but also a formula as its value. A formula is used in a cell when the cell's value needs to be determined after some calculations. In this topic, we will discuss how to access and modify a formula applied to a cell.

{{% /alert %}} 
## **Adding Formula to a Cell**
Adding a formula to a cell is just like setting the value of a cell as we discussed in our previous topic: [Accessing & Modifying the Value of a Cell](/cells/net/accessing-and-modifying-the-value-of-a-cell/) except that in that case, we only added simple values to cells. Now, we will add formulas. Developers can use the **Value** property of a cell to access and modify the formula, or they can use the **SetCellValue** method of the cell to add or modify the formula.

**IMPORTANT:** The basic difference between using the **Value** property or the **SetCellValue** method of a cell is that the **Value** property invokes the **RunAllFormulas** method of Grid automatically to recalculate the values of all formulas, whereas in the case of the **SetCellValue** method developers need to call **RunAllFormulas** explicitly after the formulas are added to cells. Actually, when we use **SetCellValue**, this method sets the value of the cell to **FormulaType** only and does not calculate the formula. Moreover, calling **RunAllFormulas** every time is not necessary. If you want to add many formulas in the cells of a worksheet, you can call **RunAllFormulas** just once at the end.

A formula is added to a cell as a string value. Moreover, the formula structure must be compatible with the formula structure of MS Excel. All formulas must begin with an **Equal Sign (=)**.

In the example given below, we have added a formula to multiply the values of two cells of the worksheet and store the result in another cell. The **RunAllFormulas** method is also invoked at the end.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}

Now run the application. If you double‑click on the cell where the formula was added, you will notice that the value is replaced by the formula that is actually calculating the value on the back end.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop supports most of the commonly used functions of MS Excel. For more details about the list of supported functions, please [click here.](/cells/net/list-of-supported-functions/)

{{% /alert %}}
