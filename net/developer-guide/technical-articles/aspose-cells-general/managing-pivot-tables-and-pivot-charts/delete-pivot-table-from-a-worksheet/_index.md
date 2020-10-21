---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 60
url: /net/delete-pivot-table-from-a-worksheet/
description: C# code to remove PivotTable for Excel Worksheets
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---

{{% alert color="primary" %}}

Aspose.Cells provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.PivotTables.Remove()**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) method to delete the pivot table using pivot table object and [**Worksheet.PivotTables.RemoveAt()**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) method to delete pivot table object using its position inside the pivot table collection.

{{% /alert %}}

The following sample code deletes two pivot tables from the worksheet. First it removes pivot table using [**Worksheet.PivotTables.Remove()**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) method and then it removes pivot table using [**Worksheet.PivotTables.RemoveAt()**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) method

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
