+++
title = "Render One Pdf Page Per Excel Worksheet - Excel to Pdf Conversion" 
description = "" 
weight = 20365 
+++

Aspose.Cells for .NET : Render One Pdf Page Per Excel Worksheet - Excel to Pdf Conversion  

# Aspose.Cells for .NET : Render One Pdf Page Per Excel Worksheet - Excel to Pdf Conversion


When working with large Microsoft Excel files (for example a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for .NET.

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.

If hte `OnePagePerSheet` option is set to true, all the sheet content will be rendered to one PDF page. The paper size of `PageSetup` would be invalid, and the other settings of `PageSetup` will still take effect.

If your spreadsheet contains formulas, it is best to call `Workbook.CalculateFormula()` just before rendering the spreadsheet to PDF. This ensures that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

