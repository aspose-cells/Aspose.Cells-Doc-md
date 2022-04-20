---
title: Convert XLS with Images and Charts to PDF
type: docs
weight: 230
url: /java/convert-xls-with-images-and-charts-to-pdf/
description: The Java code to convert Excel files with images and charts to PDF format by using the Aspose.Cells for Java API.
keywords: excel to pdf java, convert excel to pdf, convert excel to pdf java, convert excel with images to pdf java, convert excel with charts to pdf java, convert xls to pdf, convert xlsx to pdf, xls to pdf java, xlsx to pdf java, excel to pdf
---

{{% alert color="primary" %}}

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF: Aspose.PDF APIs are not required for the conversion.

{{% /alert %}}

The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call the [**Workbook.calculateFormula**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertXLSFileToPDF-ConvertXLSFileToPDF.java" >}}

## Related Articles

- [Convert Excel file to PDF format compatible with PDFA-1a](/cells/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Chart Rendering](/cells/java/chart-rendering/)
