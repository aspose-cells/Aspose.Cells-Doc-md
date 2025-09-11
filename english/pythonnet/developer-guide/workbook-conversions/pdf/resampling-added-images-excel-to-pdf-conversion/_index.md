---
title: Resample Added Images - Excel to PDF Conversion
type: docs
weight: 150
url: /python-net/resample-added-images-excel-to-pdf-conversion/
description: Learn how to resample added images when converting excel to pdf with Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---

{{% alert color="primary" %}}

While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells for Python via .NET supports resampling added images to reduce the output PDF file size and improve the performance somewhat.

{{% /alert %}}

Please see the following sample code that describes how to perform the task using the Aspose.Cells for Python via .NET API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Using the the [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) option minimizes the size of the output PDF but it may affect the image quality a bit.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}