---
title: Convert XLS with Images and Charts to PDF
type: docs
weight: 230
url: /java/convert-xls-with-images-and-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF: Aspose.PDF APIs are not required for the conversion.

{{% /alert %}} 

The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula\(\)) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}} 

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertXLSFileToPDF-ConvertXLSFileToPDF.java" >}}
