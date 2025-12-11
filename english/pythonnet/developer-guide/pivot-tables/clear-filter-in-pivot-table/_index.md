---
title: Clear filter in Pivot Table
type: docs
weight: 130
url: /python-net/clear-filter-in-pivot-table/
description: How to Clear PivotFilter from the specific PivotField in pivot table with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Clear PivotFilter in Pivot Table Using Aspose.Cells for Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you create a pivot table with known data and want to filter the pivot table, you need to learn and use filters. It can help you filter out the data you want effectively. By using the Aspose.Cells for Python via .NET API, you can operate filters on field values in Pivot Tables. 

## **How to Clear a Filter in a Pivot Table in Excel**
To clear a filter in a PivotTable in Excel, follow these steps:

1. Select the PivotTable from which you want to clear the filter.  
2. Click on the drop‑down arrow for the filter you want to clear in the pivot table.  
3. Select **Clear Filter** from the drop‑down menu.  
   <img src="1.png" width=80% />
4. If you want to clear all filters from the pivot table, you can also click on the **Clear Filters** button on the **PivotTable Analyze** tab of the ribbon in Excel.  
   <img src="2.png" width=80% />

## **How to Clear a Filter in a Pivot Table Using Aspose.Cells for Python via .NET**
Clear a filter in a Pivot Table using Aspose.Cells for Python via .NET. Please see the following sample code.

1. Set the data and create a PivotTable based on it.  
2. Add a filter on the row field of the pivot table.  
3. Save the workbook in [output XLSX](out_add.xlsx) format. After executing the example code, a pivot table with a Top 10 filter is added to the worksheet.  
4. Clear the filter on a specific pivot field. After executing the code to clear the filter, the filter on the specific pivot field will be cleared. Please check the [output XLSX](out_delete.xlsx).

## **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Clear-filter-in-PivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}
