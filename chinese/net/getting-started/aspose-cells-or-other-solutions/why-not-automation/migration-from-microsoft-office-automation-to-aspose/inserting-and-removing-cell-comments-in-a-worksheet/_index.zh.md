---
title: 在工作表中插入和移除单元格注释
type: docs
weight: 30
url: /zh/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

通常，注释用于向工作表中的单元格添加额外信息。我们时常使用它们，当我们不再需要时会将其删除。如果您需要记录特定值或帮助您记住公式的功能，则注释非常有用。当您将鼠标指针移动到带有注释的单元格上时，会弹出一个小框，显示注释。

在本文中，我们比较了使用 VSTO 和 Aspose.Cells for .NET 如何向单元格添加和移除注释。Aspose.Cells for .NET 独立于 Office Automation 与 Microsoft Excel 文件一起工作，为您提供了创建和操作电子表格的强大工具。

{{% /alert %}}

## **在单元格中添加和删除注释**

要向单元格添加注释:

1. 打开现有的Excel文件。
1. 向单元格添加注释。
1. 保存文件。

要删除注释，过程类似，不同之处在于注释被移除。

以下代码示例首先演示如何使用 VSTO 或 Aspose.Cells for .NET [添加注释](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)，然后演示如何使用 VSTO 或 Aspose.Cells for .NET [删除注释](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)。

## **插入注释**

这些代码片段首先演示如何使用 [VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C＃，VB）向单元格添加注释，然后演示如何使用 [Aspose.Cells for .NET](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C＃，VB）。

### **在 VSTO 中插入注释**

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

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **在 Aspose.Cells for .NET 中插入注释**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **删除评论**

要从单元格中删除注释，请使用以下代码行进行 [VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C＃，VB）和 [Aspose.Cells](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET（C＃，VB）。

### **在 VSTO 中删除注释**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **在 Aspose.Cells for .NET 中删除注释**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
