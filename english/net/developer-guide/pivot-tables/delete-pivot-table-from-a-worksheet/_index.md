---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 60
url: /net/delete-pivot-table-from-a-worksheet/
description: C# code to remove PivotTable for Excel Worksheets
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides a feature to delete or remove a **Pivot Table** from a **Worksheet**. You can delete the pivot table using a pivot table object or a pivot table position. Please use the [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) method to delete the pivot table using a pivot table object and the [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) method to delete the pivot table using its position within the pivot table collection.

{{% /alert %}}

The following sample code deletes two pivot tables from the worksheet. First, it removes a pivot table using the **Worksheet.PivotTables.Remove()** method, and then it removes a pivot table using the **Worksheet.PivotTables.RemoveAt()** method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
