---
title: AutoFit Columns and Rows while loading HTML in Workbook with Golang via C++
linktitle: AutoFit Columns and Rows while loading HTML in Workbook
type: docs
weight: 120
url: /go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Learn how to autofit columns and rows while loading HTML into a Workbook using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

You can autofit columns and rows while loading your HTML file inside the Workbook object. Please set the [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) property to **true** for this purpose.

## **AutoFit Columns and Rows while loading HTML in Workbook**

The following sample code first loads the sample HTML into a Workbook without any load options and saves it in XLSX format. It then loads the sample HTML into a Workbook again, but this time after setting the [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) property to **true**, and saves it in XLSX format. Please download both output Excel files, i.e., [Output Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) and [Output Excel File With AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). The following screenshot shows the effect of the [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) property on both output Excel files.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}