---
title: 创建命名范围
type: docs
weight: 70
url: /zh/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET 允许开发人员通过其应用程序执行大部分用户可以在 Microsoft Excel 中执行的任务。本文解释了如何以编程方式应用命名范围。

命名范围是 Excel 的一项功能，允许您为电子表格中的单元格或单元格范围指定名称。然后，您可以在公式中使用该名称引用单元格（或范围）。合理命名范围可使公式更易于理解。

命名范围在其范围内必须是唯一的，因此不要在工作表中多个范围使用相同的名称。描述性范围名称有助于避免这种情况：例如，OrderSubTotal 比 SubTotal 更具描述性，也不太可能在表格中重复。

{{% /alert %}}

## **创建命名范围**

要创建一个命名范围:

1. 设置工作表：
   1. 实例化一个 Application 对象。
      （仅限 VSTO。）
   1. 添加一个工作簿.
   1. 获取第一个工作表.
1. 创建一个命名范围:
   1. 定义一个范围.
   1. 给范围命名.
1. 保存文件。

以下代码示例展示了如何使用 [VSTO](/cells/zh/net/creating-a-named-range/) 和 C# 或 Visual Basic 执行这些步骤，同时还展示了如何使用 [Aspose.Cells for .NET](/cells/zh/net/creating-a-named-range/)，同样可以使用 C# 或 Visual Basic。
### **使用 VSTO 创建命名区域**

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

### **使用 Aspose.Cells for .NET 创建命名区域**

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
