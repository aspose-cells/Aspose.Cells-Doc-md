---
title: 隐藏和取消隐藏工作簿中的工作表
type: docs
weight: 80
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

在向客户展示工作簿或进行演示时，将工作表隐藏在工作簿中会很有用。电子表格建模的结构化方法建议将数据、公式和可视化（例如图表）保存在单独的工作表上。这种方法使布局保持干净和简单，并使工作簿更易于导航。展示结果时，您可能希望隐藏数据或公式表以免分心。

使用 Microsoft Excel 的用户可以轻松隐藏然后取消隐藏（显示）工作表。使用 Excel 电子表格进行编程的开发人员可以使用相同的功能。在软件应用程序中使用电子表格的方式有多种。一种方法是使用VSTO，另一种是Aspose.Cells for .NET。

{{% /alert %}}

## **隐藏和取消隐藏工作表**

本文比较[隐藏](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)和[取消隐藏](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)工作表与[VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 使用 C# 或 Visual Basic 来执行相同的任务[Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)再次使用 C# 或 Visual Basic。 Aspose.Cells 让您无需安装 Microsoft Excel 即可工作。

隐藏工作表的步骤是：

1. 打开一个文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。

到[取消隐藏](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)再次打开工作表，只需打开隐藏工作表的可见性即可。

下面的代码示例首先展示了如何隐藏工作表。第一个样本显示了这个过程[VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)，与使用 C# 或 Visual Basic 相比[Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)再次使用 C# 或 Visual Basics。

第二组代码示例显示了用于取消隐藏工作表的行[VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)要么[Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/).

## **隐藏工作表**

下面是 VSTO 和 Aspose.Cells 的代码示例，说明如何在工作簿中隐藏工作表。

### **使用 VSTO 隐藏工作表**

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

{{< highlight "csharp" >}}



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

下面是 VSTO 和 Aspose.Cells 的代码示例，说明如何取消隐藏工作簿中的工作表。

### **使用 VSTO 取消隐藏工作表**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **使用 Aspose.Cells for .NET 取消隐藏工作表**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
