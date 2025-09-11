---
title: Save Each Worksheet to a Different PDF File
type: docs
weight: 130
url: /python-net/save-each-worksheet-to-a-different-pdf-file/
description: Learn how to Save Each Worksheet to a Different PDF File with Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for Python via .NET can work independently to convert a spreadsheet to PDF and you do not need to use Aspose.PDF for .NET for the conversion. The conversion does not require the software to create or use any temporary files as the whole process can be done in memory.

{{% /alert %}} 
## **Save Each Worksheet to a Different PDF File**
If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to  set one sheet index to [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) option at a time to render to PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}