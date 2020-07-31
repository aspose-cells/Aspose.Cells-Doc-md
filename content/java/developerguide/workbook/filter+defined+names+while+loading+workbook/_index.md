---
title : "Filter Defined Names while loading Workbook" 
description : "" 
weight : 12104 
toc : false
type: docs
url: /java/developerguide/workbook/filter+defined+names+while+loading+workbook/
---

# Aspose.Cells for Java : Filter Defined Names while loading Workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Filter Defined Names while loading Workbook](#filter-defined-names-while-loading-workbook)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells allows you to filter or remove defined names present inside the workbook. Please use [LoadDataFilterOptions.DEFINED\_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to load defined names and use ~[LoadDataFilterOptions.DEFINED\_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to remove them while loading the workbook. Please note, if you will remove defined names, then formulas inside the workbook may break up. 

## Filter Defined Names while loading Workbook

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/61542593/61767873.xlsx) which has a formula in cell C1 containing the defined names i.e. *\=SUM(MyName1, MyName2)*. Since, we are using ~[LoadDataFilterOptions.DEFINED\_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to remove the defined names while loading the workbook, the formula in cell C1 in [output Excel file](https://docs2.aspose.com/cells/java/attachments/61542593/61767872.xlsx) breaks up and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![](https://docs2.aspose.com/cells/java/attachments/61542593/61767871.png)  

## Sample Code

