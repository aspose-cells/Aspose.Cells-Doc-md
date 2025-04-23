---
title: 在VSTO和Aspose.Cells中隐藏和取消隐藏工作簿中的工作表
type: docs
weight: 140
url: /zh/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

本文比较了使用VSTO（使用C# 或Visual Basic）隐藏和取消隐藏工作表，与使用Aspose.Cells（再次使用C# 或Visual Basic）执行同一任务。Aspose.Cells让您无需安装Microsoft Excel即可工作。

隐藏工作表的步骤是：

1. 打开文件。
1. 获取工作表。
1. 隐藏工作表。
1. 保存文件。
   要再次取消隐藏工作表，只需切换被隐藏工作表的可见性。

下面的代码示例首先展示了如何隐藏工作表。第一组示例展示了使用VSTO，在C#中使用Aspose.Cells，与使用Aspose.Cells的过程进行了比较。

第二组代码示例展示了在VSTO或Aspose.Cells中用于取消隐藏工作表的代码行。
## **隐藏工作表**
以下是VSTO和Aspose.Cells的代码示例，说明如何在工作簿中隐藏工作表。
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
以下是VSTO和Aspose.Cells的代码示例，说明如何在工作簿中取消隐藏工作表。
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
{{< app/cells/assistant language="csharp" >}}
