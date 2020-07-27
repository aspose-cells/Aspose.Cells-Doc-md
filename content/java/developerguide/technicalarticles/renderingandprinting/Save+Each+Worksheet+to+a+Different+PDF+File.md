+++
title = "Save Each Worksheet to a Different PDF File" 
description = "" 
weight = 16364 
+++

Aspose.Cells for Java : Save Each Worksheet to a Different PDF File  

# Aspose.Cells for Java : Save Each Worksheet to a Different PDF File


Aspose.Cells supports converting spreadsheet files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF document and you do not need to use Aspose.PDF for Java for the conversion any longer. The conversion does not require to create / use any temporary file(s) too as the whole process can be done in the memory.

If you need to save each worksheet in your template Excel file to generate different PDF files. This can be achieved easily. You may try to hide sheets in the file and make one sheet visible at a time based on which you would render PDFs.


If the spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula()) method just before rendering the spreadsheet to PDF. This ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

