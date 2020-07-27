+++
title = "Limit the Number of Pages Generated - Excel to PDF Conversion" 
description = "" 
weight = 20373 
+++

Aspose.Cells for .NET : Limit the Number of Pages Generated - Excel to PDF Conversion  

# Aspose.Cells for .NET : Limit the Number of Pages Generated - Excel to PDF Conversion


Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to the PDF file format.

## Limiting the Number of Pages Generated

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

If the spreadsheet contains formulas, it is best to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) just before rendering it to PDF. Doing ensures that formula dependent values are recalculated, and the correct values are rendered in the output file.

