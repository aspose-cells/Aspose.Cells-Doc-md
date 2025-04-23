---
title: 在工作表中合并或取消合并单元格
type: docs
weight: 40
url: /zh/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

在处理工作表时，您经常需要在跨越工作表顶部的单元格中创建标题/标题。您可能正在创建一份发票，并希望使用较少的列来显示总价或汇总值。当您想将两个或更多单元格合并为一个单元格时，您可以合并单元格。我们将使用VSTO和Aspose.Cells for .NET独立完成此任务。

{{% /alert %}}

## **描述**

打开现有的 Excel 文件，在工作簿的第一个工作表中合并一些单元格，然后保存 Excel 文件。

## **合并单元格**

以下是VSTO（C#，VB）和Aspose.Cells for .NET（C#，VB）的并行代码片段。

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

要取消合并单元格，请使用以下行的VSTO（C#，VB）和Aspose.Cells for .NET（C#，VB）的代码。

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
{{< app/cells/assistant language="csharp" >}}
