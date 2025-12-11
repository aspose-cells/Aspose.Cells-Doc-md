---
title: Pivot Filter with Golang via C++
linktitle: Pivot Filter
type: docs
weight: 130
url: /go-cpp/add-or-clear-pivot-filter/
description: Learn how to add a filter to a pivot table with Aspose.Cells using C++.
keywords: Adding a filter to a pivot table without Office 2013, Office 2016, Office 2019 and Office 365.
---

## **Possible Usage Scenarios**
When you create a pivot table with known data and want to filter the pivot table, you need to learn how to use filters. It can help you effectively filter the data you want. By using the Aspose.Cells API, you can add and clear filters on field values in Pivot Tables. 

## **Add Filter in Pivot Table in Excel**
To add a filter in a Pivot Table in Excel, follow these steps:

1. Select the PivotTable that you want to add a filter to.  
2. Click on the drop‑down arrow for the filter you want to add in the pivot table.  
3. Select **"Top 10"** from the drop‑down menu.  
   <br>
   <img src="3.png" width=80% />
4. Set the show mode and the number of filters.  
   <br>
   <img src="4.png" width=80% />

## **Add Filter in Pivot Table**
Please see the following sample code. It sets the data and creates a PivotTable based on it. Then it adds a filter on the row field of the pivot table. Finally, it saves the workbook in [output XLSX](filterout.xlsx) format. After executing the example code, a pivot table with a Top 10 filter is added to the worksheet.

### **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddFilterInPivotTable.go" >}}

## **Clear Filter in Pivot Table in Excel**
To clear a filter in a Pivot Table in Excel, follow these steps:

1. Select the PivotTable that you want to clear the filter from.  
2. Click on the drop‑down arrow for the filter you want to clear in the pivot table.  
3. Select **"Clear Filter"** from the drop‑down menu.  
   <br>
   <img src="1.png" width=80% />
4. If you want to clear all filters from the pivot table, you can also click on the **"Clear Filters"** button in the **PivotTable Analyze** tab on the ribbon in Excel.  
   <br>
   <img src="2.png" width=80% />

## **Clear Filter in Pivot Table**
Clear a filter in a Pivot Table using Aspose.Cells. Please see the following sample code.  

1. Set the data and create a PivotTable based on it.  
2. Add a filter on the row field of the pivot table.  
3. Save the workbook in [output XLSX](out_add.xlsx) format. After executing the example code, a pivot table with a Top 10 filter is added to the worksheet.  
4. Clear the filter on a specific pivot field. After executing the code to clear the filter, the filter on the specific pivot field will be cleared. Please check the [output XLSX](out_delete.xlsx).

### **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddFilterInPivotTable-1.go" >}}