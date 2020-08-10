---
title: Adding Formulas to Cells
type: docs
weight: 30
url: /net/adding-formulas-to-cells/
---

{{% alert color="primary" %}} 

A cell cannot only just contain a simple value like a numeric figure or some text but we can also insert a formula in a cell as its value. A formula is used in a cell when the value of a cell needs to be determined after some calculations. In this topic, we will discuss that how can we access and modify a formula applied on a cell.

{{% /alert %}} 
## **Adding Formula to a Cell**
Adding formula to a cell is just like setting the value of a cell as we have discussed in our previous topic: [Accessing & Modifying the Value of a Cell](/cells/net/accessing-and-modifying-the-value-of-a-cell/) except that in that case, we just added simple values to cells. Now, we will add formulas. Developers can use Value property of a cell to access & modify the formula or otherwise **SetCellValue** method of the cell can also be used to add or modify the formula in a cell.

**IMPORTANT:** The basic difference between using Value property or **SetCellValue** method of a cell is that Value property invokes **RunAllFormulas** method of Grid automatically to recalculate the values of all formulas where as in the case of **SetCellValue** method developers need to call **RunAllFormulas** method explicitly after the formulas are added to cells. Actually, when we use **SetCellValue** method of a cell then this method sets the value of the cell to **FormulaType** only and don't calculate the formula. Moreover, calling **RunAllFormulas** method every time is not necessary. If you want to add many formulas in the cells of a worksheet then you can call **RunAllFormulas** method just once at the end.

A formula is added to a cell as a string value. Moreover, the formula structure must be compatible with the formula structure of MS Excel. All formulas must begin with an **Equal Sign (=)**.

In the example given below, we have added a formula to multiply the values of two cells of the worksheet and store the result into another cell. **RunAllFormulas** method is also invoked at the end.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Now run the application. If you double click on the cell where formula was added then you would notice that the value will be replaced by the formula that is actually calculating the value on back-end.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop supports most of the commonly used functions of MS Excel. For more details about the list of supported functions, please [click here.](/cells/net/list-of-supported-functions/)

{{% /alert %}}
