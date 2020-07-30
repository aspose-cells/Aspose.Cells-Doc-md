---
title : "Convert XLS File with Images or Charts to PDF" 
description : "" 
weight : 20360 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/convert+xls+file+with+images+or+charts+to+pdf/
---

# Aspose.Cells for .NET : Convert XLS File with Images or Charts to PDF


Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for .NET can work independently to convert a spreadsheet to PDF: Aspose.PDF for .NET is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

## Sample Code

If the spreadsheet contains formulas, it is best to call the [Workbook.CalculateFormula](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

