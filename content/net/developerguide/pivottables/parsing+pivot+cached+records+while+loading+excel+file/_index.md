---
title : "Parsing Pivot Cached Records while loading Excel file" 
description : "" 
weight : 12240 
toc : false
type: docs
url: /net/developerguide/pivottables/parsing+pivot+cached+records+while+loading+excel+file/
---

# Aspose.Cells for .NET : Parsing Pivot Cached Records while loading Excel file


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Parsing Pivot Cached Records while loading Excel file](#parsing-pivot-cached-records-while-loading-excel-file)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

When you create a Pivot Table, Microsoft Excel takes a copy of the source data and stores it in the Pivot Cache. The Pivot Cache is held inside the memory of Microsoft Excel. You cannot see it but that is the data the Pivot Table references when you build your Pivot Table or change a Slicer selection or move rows/columns around. This enables Microsoft Excel to be very responsive to changes in the Pivot Table but it can also double the size of your file. After all, the Pivot Cache is just a duplicate of your source data so it makes sense that your file size will be potentially double.

When you load your Excel file inside the Workbook object, you can decide whether you also want to load the records of Pivot Cache or not, using the [LoadOptions.ParsingPivotCachedRecords](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) property. The default value of this property is **false**. If Pivot Cache is quite big, it can increase the performance. But if you also want to load the records of Pivot Cache, you should set this property as **true**.

## Parsing Pivot Cached Records while loading Excel file

The following sample code explains the usage of [LoadOptions.ParsingPivotCachedRecords](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) property. It loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/61540923/61767773.xlsx) while parsing the pivot cached records. Then it refreshes the pivot table and saves it as the [output Excel file](https://docs2.aspose.com/cells/net/attachments/61540923/61767774.xlsx).

## Sample Code

