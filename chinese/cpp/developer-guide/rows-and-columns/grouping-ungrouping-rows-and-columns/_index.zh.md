---
title: 分组、取消分组行和列
type: docs
weight: 30
url: /zh/cpp/grouping-ungrouping-rows-and-columns/
---

## **介绍**
在 Microsoft Excel 文件中，您可以为数据创建概要，让您单击一次鼠标即可显示和隐藏详细级别。

单击 **概要符号** 1,2,3, + 和 -，快速显示仅提供工作表中各个部分摘要或标题的行或列，或者可以使用符号查看个别摘要或标题下的详细信息。
## **行和列的分组管理**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 代表一个 Microsoft Excel 文件。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问 Excel 文件中的每个工作表。 工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个表示工作表中所有单元格的 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合提供了几种在工作表中管理行或列的方法，下面更详细地讨论了其中几种。
### **分组行和列**
可以通过调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) 和 [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) 方法对行或列进行分组。 两种方法都接受以下参数:

- 组的第一行/列索引，组中的第一行或列。
- 组的最后一行/列索引，组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定在分组后是否隐藏行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **分组设置**
Microsoft Excel 允许您配置用于显示的组设置：

- 详细下面的摘要行。
- 摘要列放在详细信息右侧。
## **取消分组行和列**
要取消任何已分组的行或列，请调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) 和 [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) 方法。 这两个方法都需要两个参数：

- 要取消分组的第一行或列索引，即要取消分组的第一行/列。
- 要取消分组的最后一行或列索引，即要取消分组的最后一行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
