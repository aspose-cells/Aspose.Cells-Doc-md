---
title: Hide and Unhide Worksheets in a Workbook in VSTO and Aspose.Cells
type: docs
weight: 140
url: /net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

This article compares hiding and unhiding worksheets with VSTO, using either C# or Visual Basic, to performing the same task with Aspose.Cells, again using either C# or Visual Basic. Aspose.Cells lets you work without Microsoft Excel installed.

The steps to hide a worksheet are:

1. Open a file.
1. Get a worksheet.
1. Hide the worksheet.
1. Save the file.
   To unhide a worksheet again, simply toggle visibility on for the hidden sheet.

The code samples below first show how to hide a worksheet. The first samples show the process with VSTO, using either C#, compared to using Aspose.Cells, again using either C#.

The second set of code samples show the line used to unhide the worksheet in VSTO or Aspose.Cells.
## **Hiding Worksheets**
Below are code samples for VSTO and Aspose.Cells that illustrate how to hide a worksheet in a workbook.
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **UnHiding Worksheet**
Below are code samples for VSTO and Aspose.Cells that illustrate how to unhide a worksheet in a workbook.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
