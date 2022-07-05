---
title: Creating a Named Range
type: docs
weight: 70
url: /net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET lets developers perform most of the the tasks that users can perform in Microsoft Excel through their applications. This article explains how to apply a named range programmatically.

A named range is an Excel feature that lets you assign a name to a cell, or a range of cells, in an Excel spreadsheet. You can then use the name in formulas to refer to the cell (or range). Sensibly named ranges make formulas easier to understand.

A named range has to be unique within its scope so do not use the same name for several ranges in a worksheet. Descriptive range names help avoid this: for example, OrderSubTotal is more descriptive than SubTotal and also less likely to be duplicated on a sheet.

{{% /alert %}}

## **Creating a Named Range**

To create a named range:

1. Set up the worksheet:
   1. Instantiate an Application object.
      (VSTO only.)
   1. Add a Workbook.
   1. Get the first sheet.
1. Create a named range:
   1. Define a range.
   1. Name the range.
1. Save the file.

The code examples below show how to perform these steps using [VSTO](/cells/net/creating-a-named-range/) with either C# or Visual Basic. The code examples that follow show how to do the same thing using [Aspose.Cells for .NET](/cells/net/creating-a-named-range/), again with either C# or Visual Basic.
### **Creating a Named Range with VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Creating a Named Range with Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
