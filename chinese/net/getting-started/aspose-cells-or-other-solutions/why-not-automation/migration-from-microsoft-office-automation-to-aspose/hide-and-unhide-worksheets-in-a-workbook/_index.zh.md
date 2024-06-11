---
title: 在工作簿中隐藏和取消隐藏工作表
type: docs
weight: 80
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

向客户展示工作簿或进行演示时，隐藏工作表可能会很有用。结构化的电子表格建模方法建议将数据、公式和图表等可视化内容保存在不同的表中。这种方法保持布局清晰简单，并使工作簿更易于导航。在展示结果时，您可能希望隐藏数据或公式表，以避免分心。

使用Microsoft Excel的用户可以轻松隐藏然后取消隐藏（显示）工作表。对于使用Excel电子表格进行编程的开发人员也可以使用相同的功能。软件应用程序中处理电子表格的方法有所不同。一种方法是使用VSTO，另一种则是使用Aspose.Cells for .NET。

{{% /alert %}}

## **隐藏和取消隐藏工作表**

本文比较使用 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 和 C# 或 Visual Basic 隐藏工作表，并使用 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 同样是通过 C# 或 Visual Basic 执行相同任务的差异。Aspose.Cells 可让您在未安装 Microsoft Excel 的情况下使用。

隐藏工作表的步骤是：

1. 打开文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。

要再次[取消隐藏](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/)工作表，只需切换隐藏表的可见性。

下面的代码示例首先展示了如何隐藏工作表。第一组示例展示了使用 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 和 C# 或 Visual Basic 的过程，与使用 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 同样是通过 C# 或 Visual Basic 进行比较。

第二组代码示例展示了在 [VSTO](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 或 [Aspose.Cells](/cells/zh/net/hide-and-unhide-worksheets-in-a-workbook/) 中取消隐藏工作表所使用的代码行。

## **隐藏工作表**

以下是VSTO和Aspose.Cells的代码示例，说明如何在工作簿中隐藏工作表。

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


### **使用Aspose.Cells for .NET隐藏工作表**

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

以下是VSTO和Aspose.Cells的代码示例，说明如何在工作簿中取消隐藏工作表。

### **使用 VSTO 取消隐藏工作表**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **使用Aspose.Cells for .NET取消隐藏工作表**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
