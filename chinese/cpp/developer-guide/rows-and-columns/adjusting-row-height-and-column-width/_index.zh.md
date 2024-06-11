---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

在处理电子表格并添加数据到行或列时，您可能需要更改行的高度或列的宽度。有时，在行或列上应用格式意味着当前的高度或宽度需要更改以显示数据。通常，用户在Microsoft Excel中在所见即所得的环境下调整行高和列宽。但是，使用Aspose.Cells，开发人员可以在运行时执行这些操作。

{{% /alert %}} 
## **处理行**
### **调整行高**
Aspose.Cells提供了一个代表Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类代表。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合，表示工作表中的所有单元格。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了若干方法来管理工作表中的行或列。以下是其中一些更详细的讨论。
#### **设置行的高度**
可以通过调用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法来设置单行的高度。[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法采用以下参数：

- **行索引**，要更改高度的行的索引。
- **行高**，要应用于该行的行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **设置工作表中所有行的高度**
如果开发人员需要为工作表中的所有行设置相同的行高，可以使用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **使用列**
### **设置列的宽度**
通过调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) 方法来设置列的宽度。[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) 方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽度**，所需的列宽度。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **设置工作表中所有列的宽度**
要在工作表中为所有列设置相同的列宽度，请使用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) 方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
