---
title: 查找并刷新父数据透视表的嵌套或子数据透视表
type: docs
weight: 60
url: /zh/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 如何查找并刷新父数据透视表的嵌套或子数据透视表 Aspose.Cells for Python via .NET。
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据源，因此称为子数据透视表或嵌套数据透视表。您可以使用以下命令找到父数据透视表的子数据透视表[**数据透视表.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)方法。

##  **查找并刷新父数据透视表的嵌套或子数据透视表**

以下示例代码加载[Excel 文件示例](61767747.xlsx)包含三个数据透视表。底部的两个数据透视表是上面的数据透视表的子表，如此屏幕截图所示。该代码使用以下命令查找子数据透视表[**数据透视表.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)方法，然后一一刷新。

![待办事项：图像_替代_文本](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
