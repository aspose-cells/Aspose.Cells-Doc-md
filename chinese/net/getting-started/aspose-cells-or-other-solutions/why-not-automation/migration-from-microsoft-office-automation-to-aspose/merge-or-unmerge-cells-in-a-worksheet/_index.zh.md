---
title: 合并或取消合并工作表中的单元格
type: docs
weight: 40
url: /zh/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

在处理工作表时，您经常需要在单元格中创建一个跨越工作表顶部的标题/标题。您可能正在创建发票，并且想要较少列用于总值或汇总值。当您要将两个或多个单元格合并为一个单元格时，合并这些单元格。我们使用 VSTO 和 Aspose.Cells for .NET 独立执行该任务。

{{% /alert %}}

## **描述**

打开现有的Excel文件，在工作簿的第一个工作表中合并一些单元格，并保存Excel文件。

## **合并单元格**

以下是 VSTO（C＃，VB）和 Aspose.Cells for .NET（C＃，VB）的并行代码片段。

### **1) VSTO**

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

## **取消合并单元格**

要取消合并单元格，使用以下代码行进行 [VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C＃，VB）和 [Aspose.Cells for .NET](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C＃，VB）。

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
