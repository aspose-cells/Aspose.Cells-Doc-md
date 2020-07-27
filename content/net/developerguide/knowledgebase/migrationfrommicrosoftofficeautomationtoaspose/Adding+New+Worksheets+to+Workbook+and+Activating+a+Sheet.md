+++
title = "Adding New Worksheets to Workbook and Activating a Sheet" 
description = "" 
weight = 16733 
+++

Aspose.Cells for .NET : Adding New Worksheets to Workbook and Activating a Sheet  

# Aspose.Cells for .NET : Adding New Worksheets to Workbook and Activating a Sheet


When working with a template file, sometimes, there's a need to add extra worksheets into the workbook to collect data. The new cells will be filled with data at specified positions and locations in each worksheet.

Similarly, you may need a specific worksheet to be active and viewed first when the file is opened in Microsoft Excel. An "active sheet" is the sheet that you're working on in a workbook. The name on the tab of the active sheet is bold by default.

Adding worksheets and setting which sheet is active are common and simple tasks that developers need to know how to perform. In this article, we carry out these tasks using [VSTO](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftofficeautomationtoaspose/adding+new+worksheets+to+workbook+and+activating+a+sheet) and [Aspose.Cells for .NET](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftofficeautomationtoaspose/adding+new+worksheets+to+workbook+and+activating+a+sheet).

### Adding Worksheets and Activating a Sheet

For the purposes of this migration tip:

1.  Add new worksheets to an existing Microsoft Excel file.
2.  Fill data into the cells of each new worksheet.
3.  Activate a sheet in the workbook.
4.  Save as Microsoft Excel file.

Below, are parallel code snippets for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB), that show how to achieve these tasks.

#### VSTO

**C#**

{{< code lang="c#" >}}
.......

using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;
.......

//Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.
string myPath = @"d:\test\My_Book1.xls";

//Open the excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value);

//Declare a Worksheet object.
Excel.Worksheet newWorksheet;

//Add 5 new worksheets to the workbook and fill some data
//into the cells.
for (int i = 1; i < 6; i++)
{

//Add a worksheet to the workbook.
newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.
newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.
Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.
cells.set_Item(i, i,"New_Sheet" + i.ToString());
}

//Activate the first worksheet by default.
((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.
excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.
excelApp.Quit();
 
{{< /code >}}

**VB**

{{< code lang="vb" >}}
.......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime
Imports Excel = Microsoft.Office.Interop.Excel
Imports Office = Microsoft.Office.Core
Imports System.Reflection
.......

'Instantiate the Application object.
Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.
Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.
Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data
'into the cells.
Dim i As Integer
For i = 1 To 5 Step 1

'Add a worksheet to the workbook.
newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.
newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.
Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.
cells.Item(i, i) = "New_Sheet" & i.ToString()
Next

'Activate the first worksheet by default.
CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.
excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.
excelApp.Quit()
 
{{< /code >}}

#### Aspose.Cells for .NET

**C#**

{{< code lang="c#" >}}
.......

using Aspose.Cells;

.......

//Instantiate an instance of license and set the license file
//through its path
Aspose.Cells.License license = new Aspose.Cells.License();
license.SetLicense("Aspose.Cells.lic");

//Specify the template excel file path.
string myPath =@"d:\test\My_Book1.xls";

//Instantiate a new Workbook.
//Open the excel file.
Workbook workbook = new Workbook(myPath);

//Declare a Worksheet object.
Worksheet newWorksheet;

//Add 5 new worksheets to the workbook and fill some data
//into the cells.
for (int i = 0; i < 5; i++)
{

//Add a worksheet to the workbook.
newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.
newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.
Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.
cells[i, i].PutValue("New_Sheet" + (i+1).ToString());
}

//Activate the first worksheet by default.
workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.
workbook.Save(@"d:\test\out_My_Book1.xls");
 
{{< /code >}}

**VB**

{{< code lang="vb" >}}
.......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file
'through its path
Dim license As Aspose.Cells.License = New Aspose.Cells.License
license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.
Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.
'Open the excel file.
Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.
Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data
'into the cells.
Dim i As Integer
For i = 0 To 4 Step 1

'Add a worksheet to the workbook.
newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.
newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.
Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.
cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())
Next

'Activate the first worksheet by default.
workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.
workbook.Save("c:\test\out_My_Book1.xls")
 
{{< /code >}}

