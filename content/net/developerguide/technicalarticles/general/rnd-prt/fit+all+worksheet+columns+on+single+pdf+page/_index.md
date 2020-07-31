---
title : "Fit All Worksheet Columns on Single PDF Page" 
description : "" 
weight : 20371 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/fit+all+worksheet+columns+on+single+pdf+page/
---

# Aspose.Cells for .NET : Fit All Worksheet Columns on Single PDF Page


Sometimes you want to generate a PDF file that fits all a worksheet's columns onto one page. The [PdfSaveOptions.AllColumnsInOnePagePerSheet](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property provides this feature in a very easy-to-use manner. Complex calculations such as the height and width of the output PDF are handled internally and are based on the data in the worksheet.

## Resources

Below are the input spreadsheet used in the example and output PDF generated for reference.

1.  [Excel File (Input)](http://www.aspose.com/docs/download/attachments/78610473/Sample-AllColumnsInOnePagePerSheet.xlsx)
2.  [PDF File (Output)](http://www.aspose.com/docs/download/attachments/78610473/Output-AllColumnsInOnePagePerSheet.pdf)

## Fit Worksheet Columns on Single PDF Page

[PdfSaveOptions.AllColumnsInOnePagePerSheet](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) ensures that all columns in a worksheet are rendered to a single PDF page, although rows may expand to several pages depending on the data in worksheet.

The sample code below shows how to use [PdfSaveOptions.AllColumnsInOnePagePerSheet](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property to render a large worksheet of 100 columns.

When a given worksheet has many columns, the rendered PDF file may show the content in a very small size. It is still readable when scaled up in a viewing application such as Acrobat Reader.

If your spreadsheet contains formulas, it is best to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

