---
title: Filter Defined Names while loading Workbook
type: docs
weight: 50
url: /net/filter-defined-names-while-loading-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to filter or remove defined names present inside the workbook. Please use [LoadDataFilterOptions.DefinedNames](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions) to load defined names and use ~[LoadDataFilterOptions.DefinedNames](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions) to remove them while loading the workbook. Please note, if you will remove defined names, then formulas inside the workbook may break up. 
## **Filter Defined Names while loading Workbook**
The following sample code loads the [sample Excel file](attachments/61542294/61767860.xlsx) which has a formula in cell **C1** containing the defined names i.e. *=SUM(MyName1, MyName2)*. Since we are using ~[LoadDataFilterOptions.DefinedNames](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions) to remove the defined names while loading the workbook, the formula in cell C1 in [output Excel file](attachments/61542294/61767861.xlsx) breaks up and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
