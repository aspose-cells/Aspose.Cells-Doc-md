---
title: 创建命名范围
type: docs
weight: 70
url: /zh/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET 允许开发人员执行用户可以通过其应用程序在 Microsoft Excel 中执行的大部分任务。本文解释了如何以编程方式应用命名范围。

命名范围是一项 Excel 功能，可让您为 Excel 电子表格中的一个单元格或一系列单元格指定名称。然后，您可以在公式中使用该名称来引用单元格（或区域）。合理命名的范围使公式更易于理解。

命名范围在其范围内必须是唯一的，因此不要对工作表中的多个范围使用相同的名称。描述性范围名称有助于避免这种情况：例如，OrderSubTotal 比 SubTotal 更具描述性，而且不太可能在工作表上重复。

{{% /alert %}}

## **创建命名范围**

要创建命名范围：

1. 设置工作表：
 1.实例化一个Application对象。
 （仅限 VSTO。）
 1. 添加工作簿。
 1. 拿到第一张纸。
1. 创建命名范围：
 1. 定义一个范围。
 1. 命名范围。
1. 保存文件。

下面的代码示例显示了如何使用[VSTO](/cells/zh/net/creating-a-named-range/)使用 C# 或 Visual Basic。下面的代码示例展示了如何使用[Aspose.Cells for .NET](/cells/zh/net/creating-a-named-range/), 再次使用 C# 或 Visual Basic。
### **使用 VSTO 创建命名范围**

**C#**

{{< highlight "csharp" >}}

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

### **使用 Aspose.Cells for .NET 创建命名范围**

**C#**

{{< highlight "csharp" >}}

 .......

使用 Aspose.Cells；

.......


//实例化一个工作簿对象

工作簿workbook = new Workbook();

//访问Excel文件中的第一个工作表

工作表worksheet = workbook.Worksheets[0];

//创建命名范围

范围 range = worksheet.Cells.CreateRange("A1", "B4");

//设置命名范围的名称

range.Name = "测试范围";

对于 (int 行 = 0; 行< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
