---
title: Save Each Worksheet to a Different PDF File with Golang via C++
linktitle: Save Each Worksheet to a Different PDF File
type: docs
weight: 130
url: /go-cpp/save-each-worksheet-to-a-different-pdf-file/
description: Learn how to save each worksheet in an Excel file to a separate PDF file using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for Go via C++ can work independently to convert a spreadsheet to PDF, and you do not need to use Aspose.PDF for C++ for the conversion. The conversion does not require creating or using any temporary files, as the whole process can be done in memory.

{{% /alert %}} 

## **Save Each Worksheet to a Different PDF File**
If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to set one sheet index in the **PdfSaveOptions.GetSheetSet()** option at a time to render to PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveEachWorksheetToADifferentPdfFile.go" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is recommended to call **Workbook.CalculateFormula()** just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated and that the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="go" >}}
