---
title: 查找并刷新父数据透视表的嵌套或子数据透视表
type: docs
weight: 50
url: /zh/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据源，因此称为子数据透视表或嵌套数据透视表。您可以使用以下命令找到父数据透视表的子数据透视表[**数据透视表.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()） 方法。

## **查找并刷新父数据透视表的嵌套或子数据透视表**

下面的示例代码加载[示例 Excel 文件](61767766.xlsx)包含三个数据透视表。底部的两个数据透视表是上述数据透视表的子项，如屏幕截图所示。该代码使用[**数据透视表.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()方法，然后将它们一一刷新。

![待办事项：图像_替代_文本](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
