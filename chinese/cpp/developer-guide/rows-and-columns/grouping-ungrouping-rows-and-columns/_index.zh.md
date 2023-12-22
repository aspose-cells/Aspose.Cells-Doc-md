---
title: 对行和列进行分组、取消分组
type: docs
weight: 30
url: /zh/cpp/grouping-ungrouping-rows-and-columns/
---
##  **介绍**
在 Microsoft Excel 文件中，您可以创建数据大纲，以便只需单击鼠标即可显示和隐藏详细级别。

单击*大纲符号**、1、2、3、+ 和 - 快速仅显示为工作表中的部分提供摘要或标题的行或列，或者您可以使用这些符号查看单个摘要下的详细信息或标题。
##  **行列分组管理**
Aspose.Cells提供一堂课，[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了多种管理工作表中的行或列的方法，下面将更详细地讨论其中的一些方法。
###  **对行和列进行分组**
可以通过调用对行或列进行分组[组行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)和[组列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。两种方法都采用以下参数：

- 第一个行/列索引，组中的第一行或第一列。
- 最后一行/列索引，组中的最后一行或最后一列。
- is hide，布尔参数，指定分组后是否隐藏行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **群组设置**
Microsoft Excel 允许您配置组设置以显示：

- 详细信息下方的摘要行。
- 详细信息右侧的摘要列。
##  **取消行和列的分组**
要取消分组任何分组的行或列，请调用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏的[取消行分组](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/)和[取消分组列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)方法。两种方法都采用两个参数：

- 第一行或第一列索引，要取消分组的第一行/列。
- 最后一个行或列索引，最后一个要取消分组的行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
