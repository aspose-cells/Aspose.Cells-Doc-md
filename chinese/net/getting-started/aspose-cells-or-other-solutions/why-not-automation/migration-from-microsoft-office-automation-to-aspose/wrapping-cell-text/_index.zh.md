---
title: 单元格文本自动换行
type: docs
weight: 130
url: /zh/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

文本自动换行可以让阅读更容易：带有自动换行文本的单元格会根据文本大小自动调整大小，从而不会被其他单元格覆盖。

使用Aspose.Cells for .NET，开发人员可以在应用程序中执行大部分用户可以使用Microsoft Excel执行的任务，包括在单元格中换行文本。本文解释了如何进行此操作，并比较了使用VSTO和Aspose.Cells执行此任务的方式。Aspose.Cells经过优化，便于高效编码，可以在没有Microsoft Automation的情况下运行。

{{% /alert %}}

## **单元格文本自动换行**

要创建一个包含两个单元格的工作表，一个包含换行文本，一个不包含：

1. 设置工作表：
   1. 创建一个工作簿。
   1. 访问第一个工作表。
1. 添加文本：
   1. 向A1单元格添加文本。
   1. 向A5单元格添加包装文本。
1. 保存电子表格。

以下的代码示例展示了如何使用[VSTO](/cells/zh/net/wrapping-cell-text/)使用C#或Visual Basic执行这些步骤。代码示例展示了如何使用[Aspose.Cells for .NET](/cells/zh/net/wrapping-cell-text/)使用C#或Visual Basic执行相同操作。

运行代码将生成一个包含两个单元格的电子表格，一个包含未换行的文本，一个包含换行文本：

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **使用VSTO自动换行文本**

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

### **使用Aspose.Cells for .NET自动换行文本**

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
