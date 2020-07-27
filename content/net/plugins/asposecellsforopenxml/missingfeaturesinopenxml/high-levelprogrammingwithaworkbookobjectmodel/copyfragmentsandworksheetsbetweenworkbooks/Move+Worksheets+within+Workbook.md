+++
title = "Move Worksheets within Workbook" 
description = "" 
weight = 24875 
+++

Aspose.Cells for .NET : Move Worksheets within Workbook  

# Aspose.Cells for .NET : Move Worksheets within Workbook


Aspose.Cells provides a method, Aspose.Cells.Worksheet.MoveTo(), used to move a worksheet to another location in the spreadsheet. The method takes the target worksheet index as a parameter.

The following example shows how to move a worksheet to another location within the workbook.

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Move Worksheet.xlsx";//Open an existing excel file.Workbook wb = new Workbook(FileName);//Create a Worksheets object with reference to//the sheets of the Workbook.WorksheetCollection sheets = wb.Worksheets;//Get the first worksheet.Worksheet worksheet = sheets\[0\];string test = worksheet.Name;//Move the first sheet to the third position in the workbook.worksheet.MoveTo(2);//Save the excel file.wb.Save(FileName);

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)

