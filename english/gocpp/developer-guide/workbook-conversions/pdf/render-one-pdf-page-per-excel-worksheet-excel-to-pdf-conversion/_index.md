---  
title: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion with Golang via C++  
type: docs  
weight: 100  
url: /go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
description: Convert Excel worksheets into PDF format with one page for each worksheet using Aspose.Cells with Golang via C++.  
---  

{{% alert color="primary" %}}  

When working with large Microsoft Excel files (for example, a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for C++.  

{{% /alert %}}  

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}  

{{% alert color="primary" %}}  

If the [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) option is set to **true**, all the sheet content will be rendered to one PDF page.  

{{% /alert %}}  

{{% alert color="primary" %}}  

If your spreadsheet contains formulas, it is best to call [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) just before rendering the spreadsheet to PDF. This ensures that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.  

{{% /alert %}}