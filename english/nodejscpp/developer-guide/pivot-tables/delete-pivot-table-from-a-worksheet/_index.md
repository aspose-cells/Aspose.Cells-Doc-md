---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 60
url: /nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for Node.js via C++ code to remove PivotTable for Excel Worksheets
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, remove pivot table from worksheet, remove pivot table from excel, how to delete pivot table with Aspose.Cells for Node.js via C++, delete pivot table, delete pivot table from excel, delete pivot table, Aspose.Cells for Node.js via C++ remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) method to delete the pivot table using pivot table object and [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) method to delete pivot table object using its position inside the pivot table collection.

{{% /alert %}}

## **How to Delete Pivot Table from Worksheet Using Aspose.Cells for Node.js via C++**

The following sample code deletes two pivot tables from the worksheet. First it removes pivot table using [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) method and then it removes pivot table using [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) method

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
