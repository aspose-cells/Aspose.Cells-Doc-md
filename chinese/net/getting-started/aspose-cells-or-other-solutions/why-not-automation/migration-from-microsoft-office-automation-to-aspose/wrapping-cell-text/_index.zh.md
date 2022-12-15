---
title: 环绕 Cell 文本
type: docs
weight: 130
url: /zh/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

环绕文本使其更易于阅读：带有环绕文本的单元格会扩展以适合文本，这样文本就不会显示在其他单元格之上。

使用 Aspose.Cells for .NET，开发人员可以在其应用程序中执行用户可以使用 Microsoft Excel 执行的大部分任务，包括在单元格中换行文本。本文解释了如何使用 VSTO 和 Aspose.Cells 并比较了任务。Aspose.Cells 针对高效编码进行了优化，并且在没有 Microsoft 自动化的情况下工作。

{{% /alert %}}

## **环绕 Cell 文本**

要创建一个包含两个单元格的工作表，一个包含环绕文本，一个不包含：

1. 设置工作表：
 1. 创建工作簿。
 1. 访问第一个工作表。
1. 添加文字：
 1. 向单元格 A1 添加文本。
 1. 将换行文本添加到单元格 A5。
1. 保存电子表格。

下面的代码示例显示了如何使用[VSTO](/cells/zh/net/wrapping-cell-text/)使用 C# 或 Visual Basic。代码示例显示如何使用[Aspose.Cells for .NET](/cells/zh/net/wrapping-cell-text/)紧接着再次使用 C# 或 Visual Basic。

运行代码会生成一个包含两个单元格的电子表格，一个包含未换行的文本，另一个包含：

|<p>**使用 VSTO 输出环绕单元格文本** </p><p>![待办事项：图像_替代_文本](wrapping-cell-text_1.png)</p>|<p>**输出环绕单元格文本 Aspose.Cells for .NET** </p><p>![待办事项：图像_替代_文本](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **使用 VSTO 包装 Cell 文本**

**C#**

{{< highlight "csharp" >}}

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

### **包装 Cell 文本使用 Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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
