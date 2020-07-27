+++
title = "Copy Worksheets between Workbooks" 
description = "" 
weight = 24873 
+++

Aspose.Cells for .NET : Copy Worksheets between Workbooks  

# Aspose.Cells for .NET : Copy Worksheets between Workbooks


Aspose.Cells provides a method, Aspose.Cells.Worksheet.Copy() used to copy data and formatting from a source worksheet to another worksheet within or between workbooks. The method takes the source worksheet object as a parameter.

The following example shows how to copy a worksheet from one workbook to another workbook.

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Copy Sheet between Workbook.xlsx";//Create a new Workbook.Workbook excelWorkbook0 = new Workbook();//Get the first worksheet in the book.Worksheet ws0 = excelWorkbook0.Worksheets\[0\];//Put some data into header rows (A1:A4)for (int i = 0; i < 5; i++){    ws0.Cells\[i, 0\].PutValue(string.Format("Header Row {0}", i));}//Put some detail data (A5:A999)for (int i = 5; i < 1000; i++){    ws0.Cells\[i, 0\].PutValue(string.Format("Detail Row {0}", i));}//Define a pagesetup object based on the first worksheet.PageSetup pagesetup = ws0.PageSetup;//The first five rows are repeated in each page...//It can be seen in print preview.pagesetup.PrintTitleRows = "$1:$5";//Create another Workbook.Workbook excelWorkbook1 = new Workbook();//Get the first worksheet in the book.Worksheet ws1 = excelWorkbook1.Worksheets\[0\];//Name the worksheet.ws1.Name = "MySheet";//Copy data from the first worksheet of the first workbook into the//first worksheet of the second workbook.ws1.Copy(ws0);//Save the excel file.excelWorkbook1.Save(FileName);

## Download Sample Code

*   [Codeplex](http://goo.gl/sbk9qP)
*   [Github](https://github.com/asposemarketplace/Aspose_for_OpenXML/releases/download/4/Copy.between.Workbooks.Aspose.Cells.zip)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

The following example shows how to copy a worksheet from one workbook to another workbook.

//Create a new Workbook.Workbook excelWorkbook0 = new Workbook();//Get the first worksheet in the book.Worksheet ws0 = excelWorkbook0.Worksheets\[0\];//Put some data into header rows (A1:A4)for (int i = 0; i < 5; i++){	ws0.Cells\[i, 0\].PutValue(string.Format("Header Row {0}", i));}//Put some detail data (A5:A999)for (int i = 5; i < 1000; i++){	ws0.Cells\[i, 0\].PutValue(string.Format("Detail Row {0}", i));}//Define a pagesetup object based on the first worksheet.PageSetup pagesetup = ws0.PageSetup;//The first five rows are repeated in each page...//It can be seen in print preview.pagesetup.PrintTitleRows = "$1:$5";//Create another Workbook.Workbook excelWorkbook1 = new Workbook();//Get the first worksheet in the book.Worksheet ws1 = excelWorkbook1.Worksheets\[0\];//Name the worksheet.ws1.Name = "MySheet";//Copy data from the first worksheet of the first workbook into the//first worksheet of the second workbook.ws1.Copy(ws0);//Save the excel file.excelWorkbook1.Save("copyworksheet.xls");

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

