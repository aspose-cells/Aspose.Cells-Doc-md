---
title: Limit the Number of Pages Generated - Excel to PDF Conversion
type: docs
weight: 180
url: /net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to the PDF file format.

{{% /alert %}}

## **Limiting the Number of Pages Generated**

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) just before rendering it to PDF. Doing ensures that formula dependent values are recalculated, and the correct values are rendered in the output file.

{{% /alert %}}
