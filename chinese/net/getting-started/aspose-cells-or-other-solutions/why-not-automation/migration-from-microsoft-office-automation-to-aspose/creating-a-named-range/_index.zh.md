---
title: 创建命名区域
type: docs
weight: 70
url: /zh/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET允许开发人员通过其应用程序执行大部分在Microsoft Excel中用户可以执行的任务。本文解释了如何通过编程方式应用命名范围。

命名区域是Excel的一个功能，可以让您为电子表格中的单元格或一组单元格指定一个名称。

在其作用域内，命名区域必须是唯一的，不要在工作表中使用相同的名称。

{{% /alert %}}

## **创建命名区域**

要创建一个命名范围:

1. 设置工作表：
   1. 实例化一个Application对象。
      （仅限VSTO。）
   1. 添加一个工作簿。
   1. 获取第一个工作表。
1. 创建一个命名范围:
   1. 定义一个范围。
   1. 给范围命名。
1. 保存文件。

下面的代码示例展示了如何使用[VSTO](/cells/zh/net/creating-a-named-range/)和C#或Visual Basic来执行这些步骤。接下来的代码示例展示了如何使用[Aspose.Cells for .NET](/cells/zh/net/creating-a-named-range/)，同样使用C#或Visual Basic来执行相同的操作。
### **使用 VSTO 创建命名范围**

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

### **使用Aspose.Cells for .NET创建命名范围**

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
