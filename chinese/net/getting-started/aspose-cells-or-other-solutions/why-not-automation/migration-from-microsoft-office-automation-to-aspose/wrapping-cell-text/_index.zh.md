---
title: 文本换行
type: docs
weight: 130
url: /zh/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

换行文本使阅读更加简单：包含换行文本的单元格会扩展以适应文本，这样文本就不会显示在其他单元格上。

使用 Aspose.Cells for .NET，开发人员可以在其应用程序中执行大部分用户可以在 Microsoft Excel 中执行的任务，包括在单元格中换行。本文解释了如何执行此任务，并比较了使用 VSTO 和 Aspose.Cells 进行任务。

{{% /alert %}}

## **文本换行的单元格**

要创建一个包含两个单元格的工作表，一个包含换行文本，一个不包含：

1. 设置工作表：
   1. 创建一个工作簿。
   1. 访问第一个工作表。
1. 添加文本：
   1. 添加文本到A1单元格。
   1. 在A5单元格中添加包裹文本。
1. 保存电子表格。

下面的代码示例显示了如何使用 [VSTO](/cells/zh/net/wrapping-cell-text/) 使用C#或Visual Basic执行这些步骤。紧随其后的代码示例显示了如何使用 [Aspose.Cells for .NET](/cells/zh/net/wrapping-cell-text/) 执行相同步骤，同样使用C#或Visual Basic。

运行该代码会生成一个电子表格，其中包括两个单元格，一个包含未换行的文本，另一个包含:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **使用VSTO进行文本换行**

**C#**

{{< highlight csharp >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

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

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **使用 Aspose.Cells for .NET 换行单元格文本**

**C#**

{{< highlight csharp >}}

 void WrappingCellText()

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

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
