---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 60
url: /python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET code to remove PivotTable for Excel Worksheets
keywords: Aspose.Cells for Python Excel, Excel Python library, Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) method to delete the pivot table using pivot table object and [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) method to delete pivot table object using its position inside the pivot table collection.

{{% /alert %}}

## **How to Delete Pivot Table from Worksheet Using Aspose.Cells for Python Excel Library**

The following sample code deletes two pivot tables from the worksheet. First it removes pivot table using [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) method and then it removes pivot table using [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) method

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
