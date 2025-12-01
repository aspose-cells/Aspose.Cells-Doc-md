---
title: Filter Defined Names while loading Workbook
type: docs
weight: 50
url: /python-net/filter-defined-names-while-loading-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells for Python via .NET allows you to filter or remove defined names present inside the workbook. Please use [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) to load defined names and use ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) to remove them while loading the workbook. Please note, if you will remove defined names, then formulas inside the workbook may break up.

## **Filter Defined Names while loading Workbook**

The following sample code loads the [sample Excel file](61767860.xlsx) which has a formula in cell **C1** containing the defined names i.e. *=SUM(MyName1, MyName2)*. Since we are using ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) to remove the defined names while loading the workbook, the formula in cell C1 in [output Excel file](61767861.xlsx) breaks up and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
