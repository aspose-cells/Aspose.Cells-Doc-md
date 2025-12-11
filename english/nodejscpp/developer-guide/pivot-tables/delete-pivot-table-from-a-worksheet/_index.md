---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 60
url: /nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for Node.js via C++ code to remove PivotTable for Excel worksheets
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, remove pivot table from worksheet, remove pivot table from Excel, how to delete pivot table with Aspose.Cells for Node.js via C++, delete pivot table, delete pivot table from Excel, delete pivot table, Aspose.Cells for Node.js via C++ remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ provides a feature to delete a PivotTable from a worksheet. You can delete the PivotTable using a PivotTable object or its position. Please use the [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) method to delete the PivotTable using the object and the [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) method to delete the PivotTable using its position inside the collection.

{{% /alert %}}

## **How to Delete Pivot Table from Worksheet Using Aspose.Cells for Node.js via C++**

The following sample code deletes two PivotTables from the worksheet. First, it removes a PivotTable using the [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) method, and then it removes a PivotTable using the [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) method.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
