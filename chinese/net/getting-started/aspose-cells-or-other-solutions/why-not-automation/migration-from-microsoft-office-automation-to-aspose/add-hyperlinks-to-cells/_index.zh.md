---
title: 添加超链接到 Cells
type: docs
weight: 60
url: /zh/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET 允许您通过您的应用程序执行用户可以在 Microsoft Excel 中执行的几乎任何任务。本文比较了如何使用VSTO和Aspose.Cells for .NET向工作表中的单元格添加超链接。

{{% /alert %}}

## **添加超链接到 Cells**

要向电子表格中的单元格添加超链接，请执行以下步骤：

1. 设置工作表：
 1.实例化一个Application对象。
 （仅限 VSTO。）
 1. 添加工作簿。
 1. 拿到第一张纸。
 1. 将文本添加到要添加超链接的单元格中。
1. 添加超链接。
1. 保存文档。

这些步骤显示在下面的代码示例中。第一个例子展示了如何使用[VSTO](/cells/zh/net/add-hyperlinks-to-cells/)使用 C# 或 Visual Basic 向单元格添加超链接。下面的例子展示了如何使用[Aspose.Cells for .NET](/cells/zh/net/add-hyperlinks-to-cells/)再次使用 C# 或 Visual Basic。

代码示例生成一个 Excel 文件，该文件在第一个工作表的单元格 A1 中有一个超链接。

![待办事项：图片_替代_文本](add-hyperlinks-to-cells_1.png)

**一个超链接被添加到单元格 A1。**

### **使用 VSTO 添加到 Cells 的超链接**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **使用 Aspose.Cells for .NET 添加到 Cells 的超链接**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
