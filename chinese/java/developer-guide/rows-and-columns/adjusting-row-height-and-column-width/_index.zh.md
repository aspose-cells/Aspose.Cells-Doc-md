---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

在处理电子表格并向行或列添加数据时，您可能需要更改行的高度或列的宽度。有时候，向行或列应用格式意味着当前的高度或宽度需要更改以显示数据。通常，用户在WYSIWYG环境中使用Microsoft Excel调整行高和列宽。但是，使用Aspose.Cells，开发人员可以在运行时执行这些操作。行和列的索引将从0开始。

{{% /alert %}} 
## **处理行**
### **调整行高**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个允许访问Excel文件中每个工作表的[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供表示工作表中所有单元格的[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合提供了几种方法来管理工作表中的行或列。以下是其中一些更详细的讨论。
### **设置行高**
通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\))方法，可以设置单个行的高度。[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\))方法采用以下参数：

- **行索引**，要更改其高度的行的索引。
- **行高**，要应用于该行的行高。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **设置所有行的相同行高度**
要为工作表中的所有行设置相同的行高度，请使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **处理列**
### **设置列的宽度**
通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\))方法，可以设置列的宽度。[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\))方法采用以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽**，所需的列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **设置所有列的相同列宽度**
要为工作表中的所有列设置相同的列宽度，请使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
