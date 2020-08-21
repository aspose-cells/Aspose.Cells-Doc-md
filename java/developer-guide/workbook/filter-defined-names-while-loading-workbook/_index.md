---
title: Filter Defined Names while loading Workbook
type: docs
weight: 50
url: /java/filter-defined-names-while-loading-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to filter or remove defined names present inside the workbook. Please use [LoadDataFilterOptions.DEFINED_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to load defined names and use ~[LoadDataFilterOptions.DEFINED_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to remove them while loading the workbook. Please note, if you will remove defined names, then formulas inside the workbook may break up. 
## **Filter Defined Names while loading Workbook**
The following sample code loads the [sample Excel file](61767873.xlsx) which has a formula in cell C1 containing the defined names i.e. *=SUM(MyName1, MyName2)*. Since, we are using ~[LoadDataFilterOptions.DEFINED_NAMES](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) to remove the defined names while loading the workbook, the formula in cell C1 in [output Excel file](61767872.xlsx) breaks up and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
