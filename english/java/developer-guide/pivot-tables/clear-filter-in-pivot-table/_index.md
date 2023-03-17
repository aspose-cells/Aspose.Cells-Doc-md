---
title: Clear filter in Pivot Table
type: docs
weight: 130
url: /java/clear-filter-in-pivot-table/
description: How to Clear PivotFilter from the specific PivotField in pivot table with Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---

## **Possible Usage Scenarios**
When you create a pivot table with known data and want to filter the pivot table, you need to learn and use filter. It can help you filter out the data you want effectively. By using the Aspose.Cells API, you can operate filter on field values in Pivot Tables. 

## **Clear filter in Pivot Table in Excel**
Clear filter in Pivot Table in Excel, follow these steps:

1. Select the PivotTable that you want to clear filter to. 
2. Click on the drop-down arrow for the filter you want to clear in the pivot table.
3. Select the "Clear Filter" from the drop-down menu.
<img src="1.png" width=80% />
4. If you want to clear all filters from the pivot table, you can also click on the "Clear Filters" button in PivotTable Analyze tab on the ribbon in Excel.
<img src="2.png" width=80% />

## **Clear filter in Pivot Table**
Please see the following sample code. It sets the data and creates a PivotTable based on it. Then add a filter on the row field of the pivot table. Finally, it saves the workbook in [output XLSX](out_add.xlsx) format. After executing the example code, a pivot table with top10 filter is added to the worksheet. After adding a filter, when we need unfiltered data, we can clear the filter on a specific pivotfield. After executing the code to clear the filter, the filter on the specific pivotfield will be cleared. Please check the [output XLSX](out_delete.xlsx).

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}