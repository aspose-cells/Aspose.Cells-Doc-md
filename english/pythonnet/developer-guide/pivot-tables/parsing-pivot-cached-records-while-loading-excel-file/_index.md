---
title: Parsing Pivot Cached Records while loading Excel file
type: docs
weight: 70
url: /python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: How to parse Pivot Cached Records while loading Excel file with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, How to Parse Pivot Cached Records while loading Excel file Using Aspose.Cells for Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you create a Pivot Table, Microsoft Excel takes a copy of the source data and stores it in the Pivot Cache. The Pivot Cache is held **in** the memory of Microsoft Excel. You cannot see it, but that is the data the Pivot Table references when you build your Pivot Table, change a Slicer selection, or move rows/columns around. This enables Microsoft Excel to be very responsive to changes in the Pivot Table, but it can also double the size of your file. After all, the Pivot Cache is just a duplicate of your source data, so it makes sense that your file size could potentially double.

When you load your Excel file **into** the Workbook object, you can decide whether you also want to load the records of the Pivot Cache or not, using the [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/) property. The default value of this property is **false**. If the Pivot Cache is quite big, it can increase performance. But if you also want to load the records of the Pivot Cache, you should set this property **to** **true**.

## **How to Parse Pivot Cached Records while loading Excel file**

The following sample code explains the usage of [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/) property. It loads the [sample Excel file](61767773.xlsx) while parsing the pivot cached records. Then it refreshes the pivot table and saves it as the [output Excel file](61767774.xlsx).

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
