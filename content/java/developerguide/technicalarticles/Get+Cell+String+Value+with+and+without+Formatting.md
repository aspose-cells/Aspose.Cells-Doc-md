+++
title = "Get Cell String Value with and without Formatting" 
description = "" 
weight = 12489 
+++

Aspose.Cells for Java : Get Cell String Value with and without Formatting  

# Aspose.Cells for Java : Get Cell String Value with and without Formatting


Aspose.Cells provides a method [Cell.getStringValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getStringValue(int)) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [Cell.getStringValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getStringValue(int)) method. It takes [CellValueFormatStrategy](https://apireference.aspose.com/java/cells/com.aspose.cells/CellValueFormatStrategy) enum as a parameter which has the following values

*   [CellValueFormatStrategy.CELL\_STYLE](https://apireference.aspose.com/java/cells/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
*   [CellValueFormatStrategy.DISPLAY\_STYLE](https://apireference.aspose.com/java/cells/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
*   [CellValueFormatStrategy.NONE](https://apireference.aspose.com/java/cells/com.aspose.cells/cellvalueformatstrategy#NONE)

#### Get Cell String Value with and without Formatting

The following sample code explains the use of [Cell.getStringValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getStringValue(int)) method.


#### Console Output

Below is the console output of the above sample code.

0.010.012345

