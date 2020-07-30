---
title : "Get worksheet information" 
description : "" 
weight : 16849 
toc : false
type: docs
url: /net/plugins/openxml/codeinopenxml/get+worksheet+information/
---

# Aspose.Cells for .NET : Get worksheet information


## OpenXML Excel

string FilePath = @"..\\..\\..\\..\\Sample Files\\";string FileName = FilePath + "Get worksheet information.xlsx";GetSheetInfo(FileName);Console.ReadKey();}public static void GetSheetInfo(string fileName){// Open file as read-only.using (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false)){    S sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets;    // For each sheet, display the sheet information.    foreach (E sheet in sheets)    {        foreach (A attr in sheet.GetAttributes())        {            Console.WriteLine("{0}: {1}", attr.LocalName, attr.Value);        }    }}

## Aspose.Cells

string FilePath = @"..\\..\\..\\..\\Sample Files\\";string FileName = FilePath + "Get worksheet information.xlsx";GetSheetInfo(FileName);Console.ReadKey();}private static void GetSheetInfo(string fileName){//Instantiating a Workbook objectWorkbook workbook = new Workbook(fileName);//Loop through all Sheets in the workbookforeach (Worksheet Sheet in workbook.Worksheets){    //Get Name and Index of Sheet    Console.WriteLine("Sheet Name: {0}", Sheet.Name);    Console.WriteLine("Sheet Index: {0}", Sheet.Index);    //Loop through all custom properties    foreach (CustomProperty Property in Sheet.CustomProperties)    {        Console.WriteLine("{0}: {1}", Property.Name, Property.Value);    }}

## Download Sample Code

*   [CodePlex](https://asposeopenxml.codeplex.com/releases/view/616479)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
*   [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20(Aspose.Cells).zip/download)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20(Aspose.Cells).zip)

