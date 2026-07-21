---
title: Parsing Pivot Cached Records while loading an Excel file
type: docs
weight: 70
url: /nodejs-cpp/parsing-pivot-cached-records-while-loading-excel-file/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you create a Pivot Table, Microsoft Excel takes a copy of the source data and stores it in the Pivot Cache. The Pivot Cache is held in memory by Microsoft Excel. You cannot see it, but that data is what the Pivot Table references when you build the Pivot Table, change a slicer selection, or move rows/columns around. This enables Microsoft Excel to be very responsive to changes in the Pivot Table, but it can also double the size of your file. After all, the Pivot Cache is just a duplicate of your source data, so it makes sense that your file size could potentially double.

When you load your Excel file into the Workbook object, you can decide whether you also want to load the records of the Pivot Cache, using the [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-) property. The default value of this property is **false**. If the Pivot Cache is large, loading it can affect performance. However, if you need to load the records of the Pivot Cache, you should set this property to **true**.

## **Parsing Pivot Cached Records while loading an Excel file**

The following sample code demonstrates the usage of [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-) property. It loads the [sample Excel file](61767773.xlsx) while parsing the pivot cached records, then refreshes the pivot table and saves it as the [output Excel file](61767774.xlsx).

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
