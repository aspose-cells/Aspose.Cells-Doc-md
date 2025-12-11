---
title: AutoFit Columns and Rows while loading HTML in Workbook
type: docs
weight: 120
url: /python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: This topic **shows** you how to AutoFit columns and rows while loading HTML in a Workbook using Aspose.Cells for Python via .NET.
keywords: AutoFit Columns and Rows while loading HTML in Workbook, AutoFit Columns and Rows for loading HTML.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

You can autofit columns and rows while loading your HTML file inside the Workbook object. Please set the [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) property to **true** for this purpose.

## **AutoFit Columns and Rows while loading HTML in Workbook**

The following sample code first loads the sample HTML into the Workbook without any load options and saves it in XLSX format. It then loads the sample HTML into the Workbook again, this time after setting the [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) property to **true**, and saves it in XLSX format. Please download both the output Excel files, i.e., [Output Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) and [Output Excel File With AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). The following screenshot shows the effect of the [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) property on both output Excel files.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
