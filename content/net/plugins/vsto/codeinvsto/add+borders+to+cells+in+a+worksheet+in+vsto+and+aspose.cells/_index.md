---
title : "Add Borders to Cells in a Worksheet in VSTO and Aspose.Cells" 
description : "" 
weight : 16789 
toc : false
type: docs
url: /net/plugins/vsto/codeinvsto/add+borders+to+cells+in+a+worksheet+in+vsto+and+aspose.cells/
---

# Aspose.Cells for .NET : Add Borders to Cells in a Worksheet in VSTO and Aspose.Cells


To add borders to cells in a spreadsheet, take the following steps:

1.  Set up the worksheet:
    *   Instantiate an Application object(VSTO only)
    *   Add a Workbook
    *   Get the first sheet
    *   Add text to the cells that you'll add borders to
2.  Add borders:
    *   Define a range
    *   Apply a border style to the range
    *   Repeat for each range and each border style you want to set. This example applies hairlines, thin,medium and thick lines
3.  Finish:
    *   Autofit the column that the cells are in to fit the text neatly
    *   Save the document

These steps are shown in code below. The first code examples show how to implement them using VSTO with either C# or Visual Basic. After the VSTO examples are examples that show how to perform the same steps using Aspose.Cells for .NET, again using either C# or Visual Basic. The Aspose.Cells code samples are a lot shorter because Aspose.Cells is optimized for efficient coding.

The code generates an Excel file with a number of cells on the first sheet, each with a different border:

![image](download/thumbnails/5020861/497314934)

Cells with borders applied.

### VSTO

{{< code lang="cs" >}}
//Instantiate the Application object.
Excel.Application ExcelApp = Application;
//Add a Workbook.
Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);
//Get the First sheet.
Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).
objSheet.Cells[2, 1] = "Hair Lines";
objSheet.Cells[4, 1] = "Thin Lines";
objSheet.Cells[6, 1] = "Medium Lines";
objSheet.Cells[8, 1] = "Thick Lines";
//Define a range object(A2).
Excel.Range _range;
_range = objSheet.get_Range("A2", "A2");
//Get the borders collection.
Excel.Borders borders = _range.Borders;
//Set the hair lines style.
borders.LineStyle = Excel.XlLineStyle.xlContinuous;
borders.Weight = 1d;

//Define a range object(A4).
_range = objSheet.get_Range("A4", "A4");
//Get the borders collection.
borders = _range.Borders;
//Set the thin lines style.
borders.LineStyle = Excel.XlLineStyle.xlContinuous;
borders.Weight = 2d;

//Define a range object(A6).
_range = objSheet.get_Range("A6", "A6");
//Get the borders collection.
borders = _range.Borders;
//Set the medium lines style.
borders.LineStyle = Excel.XlLineStyle.xlContinuous;
borders.Weight = 3d;
//Define a range object(A8).
_range = objSheet.get_Range("A8", "A8");
//Get the borders collection.
borders = _range.Borders;
//Set the thick lines style.
borders.LineStyle = Excel.XlLineStyle.xlContinuous;
borders.Weight = 4d;

//Auto-fit Column A.
objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();

//Save the excel file.
objBook.SaveAs("ApplyBorders.xls",
            Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,
            Type.Missing,
            Type.Missing,
            Type.Missing,
            Type.Missing,
            Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,
            Type.Missing,
            Type.Missing,
            Type.Missing,
            Type.Missing,
            Type.Missing);

//Quit the Application.
ExcelApp.Quit();
{{< /code >}}

### Aspose.Cells

{{< code lang="cs" >}}
//Instantiate a new Workbook.
Workbook objBook = new Workbook();
//Get the First sheet.
Worksheet objSheet = objBook.Worksheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).
objSheet.Cells[1, 0].PutValue("Hair Lines");
objSheet.Cells[3, 0].PutValue("Thin Lines");
objSheet.Cells[5, 0].PutValue("Medium Lines");
objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).
 Aspose.Cells.Range _range;
 _range = objSheet.Cells.CreateRange("A2", "A2");
//Set the borders with hair lines style.
 _range.SetOutlineBorders(CellBorderType.Hair, Color.Black);

//Define a range object(A4).
_range = objSheet.Cells.CreateRange("A4", "A4");
//Set the borders with thin lines style.
_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).
_range = objSheet.Cells.CreateRange("A6", "A6");
//Set the borders with medium lines style.
_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).
_range = objSheet.Cells.CreateRange("A8", "A8");
//Set the borders with thick lines style.
_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);
//Auto-fit Column A.
objSheet.AutoFitColumn(0);
//Save the excel file.
objBook.Save("ApplyBorders.xls");

{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/1459770)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Borders.to.Cells.in.a.Worksheet.Aspose.Cells.zip)
*   [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20(Aspose.Cells).zip/download)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20(Aspose.Cells).zip)

