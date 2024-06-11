---
title: 分组、取消分组行和列
type: docs
weight: 30
url: /zh/cpp/grouping-ungrouping-rows-and-columns/
---

## **介绍**
在 Microsoft Excel 文件中，您可以创建一个数据大纲，以便通过单击鼠标来显示和隐藏不同级别的细节。

单击**大纲符号** 1、2、3、+ 和 -，快速显示工作表中提供摘要或标题的行或列，或者您可以使用这些符号来查看摘要或标题下的详细信息。
## **行和列的分组管理**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，它表示一个 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问 Excel 文件中的每个工作表。一个工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了一个 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合，表示工作表中的所有单元格。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合提供了几种管理工作表中行或列的方法，下面更详细地讨论了其中的一些。
### **分组行和列**
可以通过调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) 和 [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) 方法对行或列进行分组。这两种方法都接受以下参数：

- 第一个行/列索引，分组中的第一行或列。
- 最后一个行/列索引，分组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **分组设置**
Microsoft Excel 允许您配置用于显示的分组设置：

- 详细信息下面的摘要行。
- 详细信息右侧的摘要列。
## **取消行和列的分组**
要取消任何已分组的行或列，调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) 和 [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) 方法。这两种方法都需要两个参数：

- 第一个要取消分组的行或列索引。
- 最后一个要取消分组的行或列索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
