---
title: 自动筛选数据
type: docs
weight: 120
url: /zh/net/auto-filter-data/
---

{{% alert color="primary" %}}

了解范围内的数据是什么，通常比查看无序数据的列更容易，可以更容易地对数据进行排序和过滤。排序可以将数据按升序或降序排列，从而更容易地找到特定的值。过滤数据，允许您仅显示特定的值。例如，帮助聚焦销售记录中的特定项目。

Microsoft Excel 用户可以对列应用自动筛选。自动筛选在列顶部添加了一个菜单，您可以从中对列数据进行排序或筛选。这一功能也可以提供给与 Excel 电子表格一起工作的开发人员，无论是通过 VSTO 还是 Aspose.Cells for .NET。

{{% /alert %}}

## **自动过滤数据**

应用自动筛选到一列:

1. 创建一个工作簿。
1. 获取工作表。
1. 添加示例数据.
1. 应用自动筛选.
1. 自动调整列以使显示更吸引人.
1. 保存电子表格。

本文中的代码示例显示如何使用 [VSTO](/cells/zh/net/auto-filter-data/) 或 [Apose.Cells](/cells/zh/net/auto-filter-data/) 以及 C# 或 Visual Basic 执行这些步骤。

### **使用 VSTO 进行数据自动过滤**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**使用 VSTO 应用了自动过滤** 

![todo:image_alt_text](auto-filter-data_1.png)

### **使用 Aspose.Cells for .NET 对数据进行自动筛选**

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**应用了带有Aspose.Cells for .NET的自动筛选** 

![todo:image_alt_text](auto-filter-data_2.png)
{{< app/cells/assistant language="csharp" >}}
