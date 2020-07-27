+++
title = "Resampling Added Images - Excel to PDF Conversion" 
description = "" 
weight = 20370 
+++

Aspose.Cells for .NET : Resampling Added Images - Excel to PDF Conversion  

# Aspose.Cells for .NET : Resampling Added Images - Excel to PDF Conversion


While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells supports resampling added images to reduce the output PDF file size and improve the performance somewhat.

## Example

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

Using the the [SetImageResample](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/methods/setimageresample) option minimizes the size of the output PDF but it may affect the image quality a bit.

If your spreadsheet contains formulas, it is best to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

