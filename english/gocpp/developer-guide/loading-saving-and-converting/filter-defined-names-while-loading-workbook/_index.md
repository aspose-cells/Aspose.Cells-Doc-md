---
title: Filter Defined Names while Loading a Workbook
type: docs
weight: 50
url: /go-cpp/filter-defined-names-while-loading-workbook/
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to filter or remove defined names present inside a workbook. Please use [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) to filter defined names while loading the workbook. Please note that if you remove defined names, formulas inside the workbook may break.

## **Filter Defined Names while Loading a Workbook**

The following sample code loads the [sample Excel file](61767860.xlsx), which has a formula in cell **C1** containing the defined names, i.e., `=SUM(MyName1, MyName2)`. Since we are using [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) to remove the defined names while loading the workbook, the formula in cell C1 of the [output Excel file](61767861.xlsx) breaks up, and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}