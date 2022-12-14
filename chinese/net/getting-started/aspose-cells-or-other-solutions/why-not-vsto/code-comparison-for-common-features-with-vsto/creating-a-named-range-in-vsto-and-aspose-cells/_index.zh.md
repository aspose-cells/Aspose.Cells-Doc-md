---
title: 在 VSTO 和 Aspose.Cells 中创建命名范围
type: docs
weight: 90
url: /zh/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
要创建命名范围：

1. 设置工作表：
1. 实例化一个 Application 对象。（仅限 VSTO。）
 1. 添加工作簿。
 1. 拿到第一张纸。
1. 创建命名范围：
 1. 定义一个范围。
 1. 命名范围。
 1. 保存文件。

下面的代码示例显示如何使用 VSTO 和 C# 执行这些步骤。下面的代码示例显示如何使用 Aspose.Cells for .NET 和 C# 执行相同的操作。
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

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

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

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

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/下载)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\)。压缩）
