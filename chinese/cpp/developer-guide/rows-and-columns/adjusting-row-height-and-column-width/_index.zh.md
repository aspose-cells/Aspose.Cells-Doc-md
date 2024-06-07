---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

在处理电子表格并向行或列添加数据时，您可能需要更改行的高度或列的宽度。有时，在行或列应用格式时，当前的高度或宽度需更改以显示数据。通常，用户在Microsoft Excel的所见即所得环境中调整行高和列宽。但是，使用Aspose.Cells，开发人员可以在运行时执行这些操作。

{{% /alert %}} 
## **处理行**
### **调整行高**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，表示Microsoft Excel文件。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个表示工作表中所有单元格的[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合。 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了几种方法来管理工作表中的行或列。以下是其中一些方法的更详细讨论。
#### **设置单行高度**
可以通过调用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法来设置单行的高度。 [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法需传入以下参数：

- **行索引**，要更改其高度的行的索引。
- **行高**，要应用于该行的行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **设置工作表中所有行的高度**
如果开发人员需要为工作表中的所有行设置相同的行高，可以使用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **处理列**
### **设置列的宽度**
通过调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) 方法来设置列的宽度。[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) 方法接受以下参数:

- **列索引**，要更改其宽度的列的索引。
- **列宽**，所需的列宽。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **设置工作表中所有列的相同列宽，使用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) 方法。**
如果要为工作表中的所有列设置相同的列宽，请使用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) 方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
