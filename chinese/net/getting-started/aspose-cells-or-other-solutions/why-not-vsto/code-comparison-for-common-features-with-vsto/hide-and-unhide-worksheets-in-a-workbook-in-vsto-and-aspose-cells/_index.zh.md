---
title: 在 VSTO 和 Aspose.Cells 的工作簿中隐藏和取消隐藏工作表
type: docs
weight: 140
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
本文比较了使用 VSTO（使用 C# 或 Visual Basic）隐藏和取消隐藏工作表与使用 Aspose.Cells（再次使用 C# 或 Visual Basic）执行相同的任务。 Aspose.Cells 让您无需安装 Microsoft Excel 即可工作。

隐藏工作表的步骤是：

1. 打开一个文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。
要再次取消隐藏工作表，只需打开隐藏工作表的可见性即可。

下面的代码示例首先展示了如何隐藏工作表。第一个示例显示了 VSTO 的过程，使用 C#，与使用 Aspose.Cells 相比，再次使用 C#。

第二组代码示例显示用于在 VSTO 或 Aspose.Cells 中取消隐藏工作表的行。
## **隐藏工作表**
下面是 VSTO 和 Aspose.Cells 的代码示例，说明如何在工作簿中隐藏工作表。
### **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **取消隐藏工作表**
下面是 VSTO 和 Aspose.Cells 的代码示例，说明如何取消隐藏工作簿中的工作表。
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/下载)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\)。压缩）
