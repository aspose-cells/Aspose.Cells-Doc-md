---
title: Resample Images for Excel to PDF Conversion
type: docs
weight: 250
url: /java/resample-images-for-excel-to-pdf-conversion/
description: This article demonstrates reducing image sizes while converting Excel files to PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---

{{% alert color="primary" %}}

While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells supports re-sampling added images to reduce the output PDF file size and improve performance.

{{% /alert %}}

## **Resample Images for Excel to PDF Conversion**

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

Using the [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) option minimizes the size of the output PDF but it may affect the image quality a bit.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
