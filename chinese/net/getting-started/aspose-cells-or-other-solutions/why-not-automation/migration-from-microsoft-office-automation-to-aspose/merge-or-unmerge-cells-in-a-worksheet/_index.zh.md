---
title: 在工作表中合并或取消合并 Cells
type: docs
weight: 40
url: /zh/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

使用工作表时，您通常需要在跨越工作表顶部的单个单元格中创建标题/标题。您可能正在创建发票，并希望总计值或汇总值的列数更少。当您想要从两个或多个单元格生成一个单元格时，您可以合并这些单元格。我们独立使用 VSTO 和 Aspose.Cells for .NET 执行任务。

{{% /alert %}}

## **描述**

打开现有的excel文件，合并工作簿中第一个工作表中的一些单元格并保存excel文件。

## **合并 Cells**

以下是 VSTO（C#，VB）和 Aspose.Cells for .NET（C#，VB）的并行代码片段。

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

rng1.Merge(Missing.Value);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **取消合并 Cells**

要取消合并单元格，请对 VSTO（C#，VB）和 Aspose.Cells for .NET（C#，VB）使用以下代码行。

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
