---
title : "Adding Formulas to Cells" 
description : "" 
weight : 16639 
toc : false
type: docs
url: /net/developerguide/griddesktop/cells/adding+formulas+to+cells/
---

# Aspose.Cells for .NET : Adding Formulas to Cells


A cell cannot only just contain a simple value like a numeric figure or some text but we can also insert a formula in a cell as its value. A formula is used in a cell when the value of a cell needs to be determined after some calculations. In this topic, we will discuss that how can we access and modify a formula applied on a cell.

## Adding Formula to a Cell

Adding formula to a cell is just like setting the value of a cell as we have discussed in our previous topic: [Accessing & Modifying the Value of a Cell](https://docs2.aspose.com/cells/net/developerguide/griddesktop/cells/accessing++and++modifying+the+value+of+a+cell) except that in that case, we just added simple values to cells. Now, we will add formulas. Developers can use Value property of a cell to access & modify the formula or otherwise **SetCellValue** method of the cell can also be used to add or modify the formula in a cell.

**IMPORTANT:** The basic difference between using Value property or **SetCellValue** method of a cell is that Value property invokes **RunAllFormulas** method of Grid automatically to recalculate the values of all formulas where as in the case of **SetCellValue** method developers need to call **RunAllFormulas** method explicitly after the formulas are added to cells. Actually, when we use **SetCellValue** method of a cell then this method sets the value of the cell to **FormulaType** only and don't calculate the formula. Moreover, calling **RunAllFormulas** method every time is not necessary. If you want to add many formulas in the cells of a worksheet then you can call **RunAllFormulas** method just once at the end.

A formula is added to a cell as a string value. Moreover, the formula structure must be compatible with the formula structure of MS Excel. All formulas must begin with an **Equal Sign (=)**.

In the example given below, we have added a formula to multiply the values of two cells of the worksheet and store the result into another cell. **RunAllFormulas** method is also invoked at the end.

Now run the application. If you double click on the cell where formula was added then you would notice that the value will be replaced by the formula that is actually calculating the value on back-end.

Aspose.Cells.GridDesktop supports most of the commonly used functions of MS Excel. For more details about the list of supported functions, please [click here.](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/formulacalculationengine/apsclsgridcontrols/list+of+supported+functions)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Adding Formulas to Cells-001.png](https://docs2.aspose.com/cells/net/attachments/5017788/5113901.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Adding Formulas to Cells-002.png](https://docs2.aspose.com/cells/net/attachments/5017788/5113883.png) (image/png)  

