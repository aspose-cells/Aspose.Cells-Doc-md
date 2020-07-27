+++
title = "Get Cell String Value with and without Formatting" 
description = "" 
weight = 20491 
+++

Aspose.Cells for .NET : Get Cell String Value with and without Formatting  

# Aspose.Cells for .NET : Get Cell String Value with and without Formatting


Aspose.Cells provides a method [Cell.GetStringValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstringvalue) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [Cell.GetStringValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstringvalue) method. It takes [CellValueFormatStrategy](https://apireference.aspose.com/net/cells/aspose.cells/cellvalueformatstrategy) enum as a parameter which has the following values

*   CellValueFormatStrategy.CellStyle
*   CellValueFormatStrategy.DisplayStyle
*   CellValueFormatStrategy.None

The following sample code explains the use of [Cell.GetStringValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstringvalue) method.

