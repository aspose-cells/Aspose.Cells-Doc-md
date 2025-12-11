---
title: Limit the Number of Pages Generated - Excel to PDF Conversion with Golang via C++
linktitle: Limit the Number of Pages Generated
type: docs
weight: 180
url: /go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Learn how to limit the number of pages generated when converting Excel to PDF using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells has the ability to set a limit on the number of pages generated when converting an Excel spreadsheet to the PDF file format.

{{% /alert %}}

## **Limiting the Number of Pages Generated**

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) just before rendering it to PDF. Doing so ensures that formula‑dependent values are recalculated, and the correct values are rendered in the output file.

{{% /alert %}}