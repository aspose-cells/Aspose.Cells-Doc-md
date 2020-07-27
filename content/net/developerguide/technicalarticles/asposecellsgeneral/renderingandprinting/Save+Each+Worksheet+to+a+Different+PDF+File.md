+++
title = "Save Each Worksheet to a Different PDF File" 
description = "" 
weight = 20368 
+++

Aspose.Cells for .NET : Save Each Worksheet to a Different PDF File  

# Aspose.Cells for .NET : Save Each Worksheet to a Different PDF File


Aspose.Cells supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for .NET can work independently to convert a spreadsheet to PDF and you do not need to use Aspose.PDF for .NET for the conversion. The conversion does not require the software to create or use any temporary files as the whole process can be done in memory.

## Save Each Worksheet to a Different PDF File

If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to hide sheets in the file and make one sheet visible at a time to render to PDF.

If your spreadsheet contains formulas, it is best to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

