---
title: Fit All Worksheet Columns on Single PDF Page
type: docs
weight: 160
url: /python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Learn how to Fit All Worksheet Columns on Single PDF Page with Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---

{{% alert color="primary" %}}

Sometimes you want to generate a PDF file that fits all a worksheet's columns onto one page. The [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property provides this feature in a very easy-to-use manner. Complex calculations such as the height and width of the output PDF are handled internally and are based on the data in the worksheet.

{{% /alert %}}

## **Fit Worksheet Columns on Single PDF Page**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) ensures that all columns in a worksheet are rendered to a single PDF page, although rows may expand to several pages depending on the data in worksheet.

The sample code below shows how to use [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property to render a large worksheet of 100 columns.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

When a given worksheet has many columns, the rendered PDF file may show the content in a very small size. It is still readable when scaled up in a viewing application such as Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}