---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

使用电子表格并将数据添加到行或列时，您可能需要更改行高或列宽。有时，对行或列应用格式意味着当前的高度或宽度需要更改才能显示数据。通常，用户使用 Microsoft Excel 在所见即所得的环境中调整行高和列宽。但是，使用 Aspose.Cells 开发人员可以在运行时执行这些操作。行和列的索引将从 0 开始。

{{% /alert %}} 
## **使用行**
### **调整行高**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection 提供了多种方法来管理工作表中的行或列。下面将更详细地讨论其中的一些。
### **设置行高**
可以通过调用来设置单行的高度[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[设置行高](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)） 方法。这[设置行高](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)方法采用以下参数：

- **行索引**，您要更改其高度的行的索引。
- **行高**应用于行的行高。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **设置所有行的高度**
要为工作表中的所有行设置相同的行高，请使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[设置标准高度](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **使用列**
### **设置列宽**
通过调用设置列的宽度[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[设置列宽](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)） 方法。这[设置列宽](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)方法采用以下参数：

- **列索引**，您要更改其宽度的列的索引。
- **列宽**所需的列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **设置所有列的宽度**
要为工作表中的所有列设置相同的列宽，请使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[设置标准宽度](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
