---
title: Add Hyperlinks to Cells
type: docs
weight: 60
url: /net/add-hyperlinks-to-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for .NET allows you to perform almost any tasks through your application that a user can perform in Microsoft Excel. This article compares how to add a hyperlink to a cell in a worksheet using VSTO and Aspose.Cells for .NET.

{{% /alert %}}

## **Adding Hyperlinks to Cells**

To add hyperlinks to cells in a spreadsheet, take the following steps:

1. Set up the worksheet:
   1. Instantiate an Application object.
      (VSTO only.)
   1. Add a Workbook.
   1. Get the first sheet.
   1. Add text to the cells that you'll add a hyperlink to.
1. Add hyperlink.
1. Save the document.

These steps are shown in the code examples below. The first examples shows how to use [VSTO](/cells/net/add-hyperlinks-to-cells/) with either C# or Visual Basic to add a hyperlink to a cell. The examples that follow show how to do the same thing using [Aspose.Cells for .NET](/cells/net/add-hyperlinks-to-cells/), again using C# or Visual Basic.

The code samples generate an Excel file that has a hyperlink in cell A1 on the first worksheet.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**A hyperlink is added to cell A1.**

### **Adding Hyperlinks to Cells with VSTO**

**C#**

{{< highlight csharp >}}

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



{{< /highlight >}}

### **Adding Hyperlinks to Cells with Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
