---  
title: Save Specified Worksheets to PDF with Golang via C++  
linktitle: Save Specified Worksheets to PDF  
type: docs  
weight: 140  
url: /go-cpp/save-specified-worksheets-to-pdf/  
description: Export specific worksheets to PDF using Aspose.Cells with Golang via C++.  
---  

By default, Aspose.Cells saves all **visible** worksheets in a workbook to a PDF file. With the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/getsheetset/) option, you can save specified worksheets to a PDF file. For example, you can save the active worksheet to PDF, save all worksheets (both visible and hidden) to PDF, or save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you want to export only the active sheet to PDF, you can achieve this by passing [**SheetSet.GetActive()**](https://reference.aspose.com/cells/go-cpp/sheetset/sheetset_getactive/) to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/getsheetset/) option.

The sheet `Sheet2` is the active sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveSpecifiedWorksheetsToPdf.go" >}}

## **Save All Worksheets to PDF**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/go-cpp/sheetset/sheetset_getvisible/) indicates visible sheets in a workbook, and [**SheetSet.GetAll()**](https://reference.aspose.com/cells/go-cpp/sheetset/sheetset_getall/) indicates all sheets, including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to PDF, you can simply pass [**SheetSet.GetAll()**](https://reference.aspose.com/cells/go-cpp/sheetset/sheetset_getall/) to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/getsheetset/) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets, with hidden sheet `Sheet3`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveSpecifiedWorksheetsToPdf-1.go" >}}

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to PDF, you can achieve this by passing multiple sheet indices to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/getsheetset/) option.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveSpecifiedWorksheetsToPdf-2.go" >}}

## **Reorder Worksheets to PDF**

If you want to reorder sheets (e.g., in reverse order) to PDF without modifying the source file, you can achieve this by passing reordered sheet indices to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/getsheetset/) option.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveSpecifiedWorksheetsToPdf-3.go" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="go" >}}
