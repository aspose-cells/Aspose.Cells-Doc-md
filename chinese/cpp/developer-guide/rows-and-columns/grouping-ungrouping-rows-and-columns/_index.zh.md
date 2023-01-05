---
title: 分组、取消分组行和列
type: docs
weight: 30
url: /zh/cpp/grouping-ungrouping-rows-and-columns/
---
## **介绍**
在 Microsoft Excel 文件中，您可以为数据创建一个大纲，以便通过单击鼠标来显示和隐藏详细信息级别。

点击**大纲符号**、1、2、3、+ 和 - 以仅快速显示为工作表中的部分提供摘要或标题的行或列，或者您可以使用这些符号来查看单个摘要或标题下的详细信息。
## **行列分组管理**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了一个[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)代表工作表中所有单元格的集合。

这[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection 提供了多种方法来管理工作表中的行或列，下面将详细讨论其中的一些方法。
### **分组行和列**
可以通过调用[组行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332)和[组列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。这两种方法都采用以下参数：

- 第一行/列索引，组中的第一行或第一列。
- 最后一行/列索引，组中的最后一行或最后一列。
- is hidden，布尔型参数，指定分组后是否隐藏行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **群组设置**
Microsoft Excel 允许您配置组设置以显示：

- 详细信息下方的汇总行。
- 详细信息右侧的摘要列。
## **取消分组行和列**
要取消分组任何已分组的行或列，请调用[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏的[解组行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1)和[取消组合列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)方法。两种方法都有两个参数：

- 第一行或列索引，要取消分组的第一行/列。
- 最后一行或最后一列索引，要取消分组的最后一行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
