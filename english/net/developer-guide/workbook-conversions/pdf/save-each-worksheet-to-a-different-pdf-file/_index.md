---
title: Save Each Worksheet to a Different PDF File
type: docs
weight: 130
url: /net/save-each-worksheet-to-a-different-pdf-file/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for .NET can work independently to convert a spreadsheet to PDF and you do not need to use Aspose.PDF for .NET for the conversion. The conversion does not require the software to create or use any temporary files as the whole process can be done in memory.

{{% /alert %}}
## **Save Each Worksheet to a Different PDF File**
If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to set one sheet index to the [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option at a time to render to PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
