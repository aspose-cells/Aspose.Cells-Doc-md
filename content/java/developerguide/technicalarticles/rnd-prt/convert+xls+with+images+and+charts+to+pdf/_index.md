---
title : "Convert XLS with Images and Charts to PDF" 
description : "" 
weight : 16385 
toc : false
type: docs
url: /java/developerguide/technicalarticles/rnd-prt/convert+xls+with+images+and+charts+to+pdf/
---

# Aspose.Cells for Java : Convert XLS with Images and Charts to PDF


Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF: Aspose.PDF APIs are not required for the conversion.

The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

If the spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula()) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.


