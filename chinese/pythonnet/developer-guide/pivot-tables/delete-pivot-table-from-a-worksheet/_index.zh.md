---
title: 从工作表中删除数据透视表
type: docs
weight: 60
url: /zh/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET 代码用于删除 Excel 工作表中的数据透视表
keywords: Aspose.Cells for Python Excel, Excel Python library, Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 提供了从工作表中删除数据透视表的功能。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用 [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) 方法使用数据透视表对象删除数据透视表，并使用 [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) 方法根据数据透视表集合中的位置来删除数据透视表对象。

{{% /alert %}}

## **使用Aspose.Cells for Python Excel库删除工作表中的数据透视表**

以下示例代码从工作表中删除了两个数据透视表。首先使用[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)方法移除数据透视表，然后使用[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)方法移除数据透视表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
