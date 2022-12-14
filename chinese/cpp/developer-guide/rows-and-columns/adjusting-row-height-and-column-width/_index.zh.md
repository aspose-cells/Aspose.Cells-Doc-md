---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

使用电子表格并将数据添加到行或列时，您可能需要更改行高或列宽。有时，对行或列应用格式意味着当前的高度或宽度需要更改才能显示数据。通常，用户使用 Microsoft Excel 在所见即所得的环境中调整行高和列宽。但是，使用 Aspose.Cells 开发人员可以在运行时执行这些操作。

{{% /alert %}} 
## **使用行**
### **调整行高**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[IWorksheet 集合](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)代表工作表中所有单元格的集合。这[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection 提供了多种方法来管理工作表中的行或列。下面将更详细地讨论其中的一些。
#### **设置行高**
可以通过调用来设置单行的高度[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏的[设置行高](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)方法。这[设置行高](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)方法采用以下参数，如下所示：

- **行索引**，您要更改其高度的行的索引。
- **行高**应用于行的行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **设置工作表中所有行的高度**
如果开发人员需要为工作表中的所有行设置相同的行高，他们可以使用[设置标准高度](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **使用列**
### **设置列宽**
通过调用设置列的宽度[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏的[设置列宽](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)方法。这[设置列宽](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)方法采用以下参数：

- **列索引**，您要更改其宽度的列的索引。
- **列宽**所需的列宽。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **设置工作表中所有列的宽度**
要为工作表中的所有列设置相同的列宽，请使用[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏的[设置标准宽度](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
