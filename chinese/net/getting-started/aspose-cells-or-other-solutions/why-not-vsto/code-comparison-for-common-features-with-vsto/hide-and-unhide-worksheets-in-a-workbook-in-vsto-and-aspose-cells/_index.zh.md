---
title: 在VSTO和Aspose.Cells中隐藏和显示工作表
type: docs
weight: 140
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

本文将隐藏和显示工作表在VSTO中使用C#或Visual Basic，以及在Aspose.Cells中使用C#或Visual Basic的任务进行了比较。 Aspose.Cells允许您无需安装Microsoft Excel即可工作。

隐藏工作表的步骤：

1. 打开文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。
   要再次取消隐藏工作表，请简单地为隐藏的工作表切换可见性。

以下代码示例首先显示了如何隐藏工作表。首先的示例展示了使用VSTO进行此过程，使用C#，与再次使用Aspose.Cells进行此过程相比，使用C#。

第二组代码示例显示了在VSTO或Aspose.Cells中用于取消隐藏工作表的行。
## **隐藏工作表**
以下是用于VSTO和Aspose.Cells的代码示例，演示如何在工作簿中隐藏工作表。
### **VSTO**
{{< highlight csharp >}}

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
{{< highlight csharp >}}

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
以下是用于VSTO和Aspose.Cells的代码示例，演示如何在工作簿中取消隐藏工作表。
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
