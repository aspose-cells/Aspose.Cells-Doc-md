---
title: Convert XLS File with Images or Charts to PDF
type: docs
weight: 50
url: /net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for .NET can work independently to convert a spreadsheet to PDF: Aspose.PDF for .NET is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% /alert %}} 
## **Sample Code**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Workbook.CalculateFormula](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
