---
title: 向单元格添加超链接
type: docs
weight: 60
url: /zh/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您通过应用程序执行几乎在 Microsoft Excel 中用户可以执行的任何任务。本文比较了如何使用 VSTO 和 Aspose.Cells for .NET 在工作表中为单元格添加超链接。

{{% /alert %}}

## **向单元格添加超链接**

要向电子表格中的单元格添加超链接，请执行以下步骤：

1. 设置工作表：
   1. 实例化一个Application对象。
      （仅限VSTO。）
   1. 添加一个工作簿。
   1. 获取第一个工作表。
   1. 向要添加超链接的单元格中添加文本。
1. 添加超链接。
1. 保存文档。

下面的代码示例显示了这些步骤。首先的示例展示了如何使用 [VSTO](/cells/zh/net/add-hyperlinks-to-cells/) 以及 C# 或 Visual Basic 添加超链接到单元格。随后的示例展示了如何使用 [Aspose.Cells for .NET](/cells/zh/net/add-hyperlinks-to-cells/) 以及 C# 或 Visual Basic 执行相同的操作。

代码示例生成一个Excel文件，其中包含第一个工作表上单元格A1中的超链接。

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**向单元格A1添加了一个超链接。**

### **使用VSTO添加超链接到单元格**

**C#**

{{< highlight csharp >}}

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

### **使用 Aspose.Cells for .NET 为单元格添加超链接**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
