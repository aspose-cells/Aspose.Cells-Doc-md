---
title: Resampling Added Images - Excel to PDF Conversion with Golang via C++
linktitle: Resampling Added Images - Excel to PDF Conversion
type: docs
weight: 150
url: /go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Learn how to resample added images to reduce PDF size using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells supports resampling added images to reduce the output PDF file size and improve the performance somewhat.

{{% /alert %}}

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Using the [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) option minimizes the size of the output PDF but it may affect the image quality a bit.

{{% /alert %}} 

{{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}

