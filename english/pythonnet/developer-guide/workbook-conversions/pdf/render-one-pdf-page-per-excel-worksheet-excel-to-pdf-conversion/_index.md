---
title: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion
type: docs
weight: 100
url: /python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Learn how to Render One PDF Page Per Excel Worksheet while converting Excel to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---

{{% alert color="primary" %}} 

When working with large Microsoft Excel files (for example a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

If the [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) option is set to **true**, all the sheet content will be rendered to one PDF page.

{{% /alert %}} {{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering the spreadsheet to PDF. This ensures that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
