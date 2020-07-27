+++
title = "Add Hyperlinks to Cells" 
description = "" 
weight = 16738 
+++

Aspose.Cells for .NET : Add Hyperlinks to Cells  

# Aspose.Cells for .NET : Add Hyperlinks to Cells


Aspose.Cells for .NET allows you to perform almost any tasks through your application that a user can perform in Microsoft Excel. This article compares how to add a hyperlink to a cell in a worksheet using VSTO and Aspose.Cells for .NET.

### Adding Hyperlinks to Cells

To add hyperlinks to cells in a spreadsheet, take the following steps:

1.  Set up the worksheet:
    1.  Instantiate an `Application` object.  
        (VSTO only.)
    2.  Add a `Workbook`.
    3.  Get the first sheet.
    4.  Add text to the cells that you'll add a hyperlink to.
2.  Add hyperlink.
3.  Save the document.

These steps are shown in the code examples below. The first examples shows how to use [VSTO](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftofficeautomationtoaspose/add+hyperlinks+to+cells) with either C# or Visual Basic to add a hyperlink to a cell. The examples that follow show how to do the same thing using [Aspose.Cells for .NET](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migrationfrommicrosoftofficeautomationtoaspose/add+hyperlinks+to+cells), again using C# or Visual Basic.

The code samples generate an Excel file that has a hyperlink in cell A1 on the first worksheet.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017461/5112103.png)  
**A hyperlink is added to cell A1.**

#### Adding Hyperlinks to Cells with VSTO

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017461)**

{{< code lang="cs" >}}
.......
 
using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;
.......

//Instantiate the Application object.
Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();
//Add a Workbook.
Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);
//Get the First sheet.
Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];
          
//Define a range object(A1).
Excel.Range _range;
_range = objSheet.get_Range("A1", "A1");
//Add a hyperlink to it.
objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.
objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 
//Quit the Application.
ExcelApp.Quit();
 
{{< /code >}}

#### Adding Hyperlinks to Cells with Aspose.Cells for .NET

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017461)**

{{< code lang="cs" >}}
.......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.
Workbook workbook = new Workbook();
//Get the First sheet.
Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.
Aspose.Cells.Cell cell = worksheet.Cells["A1"];
//Add a hyperlink to it.
int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");
worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";
worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.
workbook.Save("c:\\Hyperlink_test.xls");       
 
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Hyperlinks to Cells-001.png](https://docs2.aspose.com/cells/net/attachments/5017461/5112102.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Hyperlinks to Cells-002.png](https://docs2.aspose.com/cells/net/attachments/5017461/5112103.png) (image/png)  

