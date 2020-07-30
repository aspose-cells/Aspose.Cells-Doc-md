---
title : "Resample Images for Excel to PDF Conversion" 
description : "" 
weight : 16387 
toc : false
type: docs
url: /java/developerguide/technicalarticles/rnd-prt/resample+images+for+excel+to+pdf+conversion/
---

# Aspose.Cells for Java : Resample Images for Excel to PDF Conversion


While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells supports re-sampling added images to reduce the output PDF file size and improve performance.

#### Resample Images for Excel to PDF Conversion

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.


Using the [PdfSaveOptions.setImageResample](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) option minimizes the size of the output PDF but it may affect the image quality a bit.

If your spreadsheet contains formulas, it is best to call [Workbook.calculateFormula()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula()) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

