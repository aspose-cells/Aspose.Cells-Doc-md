---
title: 在工作簿中隐藏和取消隐藏工作表
type: docs
weight: 80
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

向客户展示工作簿或进行演示时，隐藏工作表可能非常有用。结构化的电子表格建模方法建议将数据、公式和图表等可视化内容保留在单独的工作表中。这种方法使布局保持干净简洁，使工作簿更易于导航。在展示结果时，您可能希望隐藏数据或公式工作表，避免干扰。

在 Microsoft Excel 中工作的用户可以轻松隐藏然后取消隐藏（显示）工作表。这些功能也适用于使用 Excel 电子表格进行编程的开发人员。从软件应用程序中处理电子表格有不同的方式。一种方法是使用 VSTO，另一种是 Aspose.Cells for .NET。

{{% /alert %}}

## **隐藏和取消隐藏工作表**

本文比较了使用 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 以及 C# 或 Visual Basic，隐藏和取消隐藏工作表与使用 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 执行相同任务的方式，同样使用 C# 或 Visual Basic。Aspose.Cells 让您可以在未安装 Microsoft Excel 的情况下工作。

隐藏工作表的步骤：

1. 打开文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。

要再次[取消隐藏](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)工作表，只需为隐藏的工作表切换显示状态。

以下代码示例首先展示了如何隐藏工作表。首先展示了使用 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 和 C# 或 Visual Basic 进行此过程，相比使用 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)，同样可以使用 C# 或 Visual Basic。

第二组代码示例展示了如何在 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 或 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 中使用的代码行来取消隐藏工作表。

## **隐藏工作表**

以下是用于VSTO和Aspose.Cells的代码示例，演示如何在工作簿中隐藏工作表。

### **使用 VSTO 隐藏工作表**

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



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **使用 Aspose.Cells for .NET 隐藏工作表**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **取消隐藏工作表**

以下是用于VSTO和Aspose.Cells的代码示例，演示如何在工作簿中取消隐藏工作表。

### **使用 VSTO 取消隐藏工作表**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **使用 Aspose.Cells for .NET 取消隐藏工作表**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
