---
title: 从工作表中删除数据透视表
type: docs
weight: 60
url: /zh/python-net/delete-pivot-table-from-a-worksheet/
description: 通过Python通过.NET代码删除Excel工作表的数据透视表
keywords: 使用Aspose.Cells for Python Excel库禁用数据透视表选项卡
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET提供了一个删除或移除工作表中数据透视表的功能。您可以使用数据透视表对象或数据透视表位置删除数据透视表。请使用[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)方法通过数据透视表对象删除数据透视表，并使用[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)方法通过其在数据透视表集合中的位置删除数据透视表对象。

{{% /alert %}}

## **使用Aspose.Cells for Python Excel库从工作表中删除数据透视表**

以下示例代码从工作表中删除了两个数据透视表。首先，它使用[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)方法删除数据透视表，然后使用[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)方法删除数据透视表

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
