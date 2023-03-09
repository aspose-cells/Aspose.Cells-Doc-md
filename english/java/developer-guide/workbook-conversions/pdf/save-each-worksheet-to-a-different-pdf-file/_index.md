---
title: Save Each Worksheet to a Different PDF File
type: docs
weight: 50
url: /java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells supports converting spreadsheet files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF document and you do not need to use Aspose.PDF for Java for the conversion any longer. The conversion does not require to create / use any temporary file(s) too as the whole process can be done in the memory.

{{% /alert %}}

If you need to save each worksheet in your template Excel file to generate different PDF files. This can be achieved easily. You may try to  set one sheet index to **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** option at a time to render to PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call the [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) method just before rendering the spreadsheet to PDF. This ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
