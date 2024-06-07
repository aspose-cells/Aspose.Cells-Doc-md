---
title: 在VSTO和Aspose.Cells中包装单元格文本
type: docs
weight: 250
url: /zh/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

要创建一个包含两个单元格的工作表，一个包含换行文本，一个不包含：

1. 设置工作表： 
   1. 创建一个工作簿。
   1. 访问第一个工作表。
1. 添加文本： 
   1. 向A1单元格添加文本。
   1. 向A5单元格添加包装文本。
1. 保存电子表格。
   以下代码示例显示了如何使用VSTO执行这些步骤，使用C#。 立即在下方使用C#展示如何使用Aspose.Cells for .NET执行相同操作的代码示例。

运行代码将生成一个包含两个单元格的电子表格，一个包含未换行的文本，一个包含换行文本：

## **使用VSTO Excel输出**

![todo:image_alt_text](picture1.png)

## **使用Aspose.Cells for .NET输出**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
