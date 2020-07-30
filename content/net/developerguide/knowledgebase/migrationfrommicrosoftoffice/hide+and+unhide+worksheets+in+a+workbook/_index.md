---
title : "Hide and Unhide Worksheets in a Workbook" 
description : "" 
weight : 16740 
toc : false
type: docs
url: /net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook/
---

# Aspose.Cells for .NET : Hide and Unhide Worksheets in a Workbook


When presenting workbooks to customers, or doing a presentation, it can be useful to hide worksheets in a workbook. A structured approach to spreadsheet modelling suggests that data, formulas and visualizations such as charts are kept on separate sheets. This approach keeps the layout clean and simple and makes the workbook easier to navigate. When presenting results, you might want to hide the data or formula sheets from view to avoid distraction.

Users who work in Microsoft Excel, can easily hide and then unhide (show) worksheets. The same features are available to developers who program with Excel spreadsheets. There are different ways of working with spreadsheets from within software applications. One method is to use VSTO, another is Aspose.Cells for .NET.

### Hiding and Unhiding Worksheets

This article compares [hiding](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook) and [unhiding](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook) worksheets with [VSTO](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook), using either C# or Visual Basic, to performing the same task with [Aspose.Cells](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook), again using either C# or Visual Basic. Aspose.Cells lets you work without Microsoft Excel installed.

The steps to hide a worksheet are:

1.  Open a file.
2.  Get a worksheet.
3.  Hide the worksheet.
4.  Save the file.

To [unhide](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook) a worksheet again, simply toggle visibility on for the hidden sheet.

The code samples below first show how to hide a worksheet. The first samples show the process with [VSTO](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook), using either C# or Visual Basic, compared to using [Aspose.Cells](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook), again using either C# or Visual Basics.

The second set of code samples show the line used to unhide the worksheet in [VSTO](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook) or [Aspose.Cells](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftoffice/hide+and+unhide+worksheets+in+a+workbook).

### Hiding Worksheets

Below are code samples for VSTO and Aspose.Cells that illustrate how to hide a worksheet in a workbook.

#### Hiding Worksheets with VSTO 

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017465)**

{{< code lang="cs" >}}
 
.......
 
using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;
.......
 
//Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();
 
//Specify the template Excel file path.
string myPath=@"d:\test\MyBook.xls";
 
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
objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.
excelApp.ActiveWorkbook.Save();

//Quit the Application.
excelApp.Quit();
 
{{< /code >}}

#### Hiding Worksheets with Aspose.Cells for .NET

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017465)**

{{< code lang="cs" >}}
 
.......
 
using Aspose.Cells;
 
.......
 
//Instantiate a new Workbook.
Workbook workbook = new Workbook();

//Specify the template Excel file path.
string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.
workbook.Open(myPath);

//Get the first sheet.
Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.
objSheet.IsVisible = false;

//Save As the Excel file.
workbook.Save(@"d:\test\MyBook.xls");
 
{{< /code >}}

### Unhiding Worksheets

Below are code samples for VSTO and Aspose.Cells that illustrate how to unhide a worksheet in a workbook.

#### Unhiding a Worksheet with VSTO

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017465)**

{{< code lang="cs" >}}
 
//Unhide the worksheet.
objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;
 
{{< /code >}}

#### Unhiding a Worksheet with Aspose.Cells for .NET

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017465)**

{{< code lang="cs" >}}
 
//Unhide the worksheet.
objSheet.IsVisible = true;
 
{{< /code >}}

