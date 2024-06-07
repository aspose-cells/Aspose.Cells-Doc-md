---
title: 查找和刷新父数据透视表的嵌套或子数据透视表
type: docs
weight: 60
url: /zh/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据源，因此被称为子数据透视表或嵌套数据透视表。您可以使用[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)方法找到父数据透视表的子数据透视表。

## **查找和刷新父数据透视表的嵌套或子数据透视表**

以下示例代码加载了包含三个数据透视表的[示例Excel文件](61767747.xlsx)。底部两个数据透视表是上面数据透视表的子数据透视表，如此屏幕截图所示。该代码使用[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)方法找到子数据透视表，然后逐个刷新这些数据透视表。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
