---
title: Clear filter in Pivot Table
type: docs
weight: 130
url: /nodejs-cpp/clear-filter-in-pivot-table/
description: How to clear a PivotFilter from a specific PivotField in a pivot table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, Clear PivotFilter in Pivot Table Using Aspose.Cells for Node.js via C++ Excel Library.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you create a pivot table with known data and want to filter the pivot table, you need to learn to use filters. It can help you filter the data you want effectively. By using the Aspose.Cells for Node.js via C++ API, you can operate filters on field values in Pivot Tables. 

## **How to Clear filter in Pivot Table in Excel**
To clear a filter in a PivotTable in Excel, follow these steps:

1. Select the PivotTable from which you want to clear the filter. 
2. Click on the drop‑down arrow for the filter you want to clear in the pivot table.
3. Select **Clear Filter** from the drop‑down menu.  
   <img src="1.png" width=80% />
4. If you want to clear all filters from the pivot table, you can also click on the **Clear Filters** button in the **PivotTable Analyze** tab on the ribbon in Excel.  
   <img src="2.png" width=80% />

## **How to Clear filter in Pivot Table Using Aspose.Cells for Node.js via C++**
Clear filter in a PivotTable using Aspose.Cells for Node.js via C++. Please see the following sample code.  
1. Set the data and create a PivotTable based on it.  
2. Add a filter on the row field of the pivot table.  
3. Save the workbook in [output XLSX](out_add.xlsx) format. After executing the example code, a pivot table with a Top10 filter is added to the worksheet.  
4. Clear the filter on a specific **PivotField**. After executing the code to clear the filter, the filter on the specific PivotField will be cleared. Please check the [output XLSX](out_delete.xlsx).

## **Sample Code**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Clear-filter-in-PivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
