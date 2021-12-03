---
title: Get Cell String Value with and without Formatting
type: docs
weight: 230
url: /java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells provides a method [Cell.getStringValue()](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [Cell.getStringValue()](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) method. It takes [CellValueFormatStrategy](https://apireference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) enum as a parameter which has the following values

- [CellValueFormatStrategy.CELL_STYLE](https://apireference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://apireference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Get Cell String Value with and without Formatting**
The following sample code explains the use of [Cell.getStringValue()](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) method.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Console Output**
Below is the console output of the above sample code.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
