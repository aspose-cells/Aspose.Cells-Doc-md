##Merge or UnMerge Cells in a Worksheet
While working with worksheets, you often need to create a title / heading in a single cell that spans the top of your worksheet. You might be creating an invoice, and want a fewer columns for the total or summary values. When you want to make one cell from two or more cells, you merge the cells. We carry out the task using VSTO and Aspose.Cells for .NET independently.
## **Description**
Open an existing excel file, Merge some cells in the first worksheet in the workbook and save the excel file.
## **Merging Cells**
Following are the parallel code snippets for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB).
### **1) VSTO**
**C#**
.......
using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;
.......
//Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();
//Specify the template excel file path.
string myPath=@"d:\test\MyBook.xls";
//Open the excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value);
//Get the range of cells i.e.., A1:C1.
Excel.Range rng1 = excelApp.get_Range("A1", "C1");
//Merge the cells.
rng1.Merge(Missing.Value);
//Save the file.
excelApp.ActiveWorkbook.Save();
//Quit the Application.
excelApp.Quit();
### **2) Aspose.Cells for .NET**
**C#**
.......
using Aspose.Cells;
.......
//Instantiate a new Workbook.
Workbook workbook = new Workbook();
//Specify the template excel file path.
string myPath=@"d:\test\MyBook.xls";
//Open the excel file.
workbook.Open(myPath);
//Get the range of cells i.e.., A1:C1.
Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");
//Merge the cells.
rng1.Merge();
//Save the file.
workbook.Save(@"d:\test\MyBook.xls");
## **UnMerging the Cells**
To unmerge the cell(s), use the following lines of code for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB).
### **1) VSTO**
**C#**
//Get the A1 cell (Merged Cell).
Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);
//UnMerge the cell.
rng1.UnMerge();
### **2) Aspose.Cells for .NET**
**C#**
//Get the A1 cell (Merged Cell).
Cells rng1 = workbook.Worksheets[0].Cells;
//UnMerge the cell.
rng1.UnMerge(0, 0, 1, 3);
