---
title: 查找和刷新父数据透视表的嵌套或子数据透视表
type: docs
weight: 50
url: /zh/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据来源，因此被称为子数据透视表或嵌套数据透视表。您可以使用[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren())方法找到父数据透视表的子数据透视表。

## **查找和刷新父数据透视表的嵌套或子数据透视表**

以下示例代码加载了包含三个数据透视表的[sample Excel文件](61767766.xlsx)。底部的两个数据透视表是上面数据透视表的子数据透视表，如屏幕截图所示。该代码使用[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren())方法查找子数据透视表，然后一个接一个地刷新它们。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
