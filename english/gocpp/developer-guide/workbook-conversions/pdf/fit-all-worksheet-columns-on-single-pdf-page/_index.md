---
title: Fit All Worksheet Columns on Single PDF Page with Golang via C++
linktitle: Fit All Worksheet Columns on Single PDF Page
type: docs
weight: 160
url: /go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Generate a PDF that fits all worksheet columns onto a single page using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes you want to generate a PDF file that fits all of a worksheet's columns onto one page. The [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) property provides this feature in a very easy‑to‑use manner. Complex calculations such as the height and width of the output PDF are handled internally and are based on the data in the worksheet.

{{% /alert %}}

## **Fit Worksheet Columns on Single PDF Page**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) ensures that all columns in a worksheet are rendered to a single PDF page, although rows may expand to several pages depending on the data in the worksheet.

The sample code below shows how to use [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) property to render a large worksheet of 100 columns.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

When a given worksheet has many columns, the rendered PDF file may show the content at a very small size. It is still readable when scaled up in a viewing application such as Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}