---
title: 在工作表中插入和删除 Cell 注释
type: docs
weight: 30
url: /zh/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

通常，注释用于向工作表中的单元格添加附加信息。我们时不时地使用它们，当我们不再需要它们时我们会删除它们。如果您需要记录特定值或帮助您记住公式的作用，则注释很有用。当您将鼠标指针移到有注释的单元格上时，注释会在一个小框中弹出。

在本文中，我们比较了如何使用 VSTO 和 Aspose.Cells for .NET 在单元格中添加和删除注释。Aspose.Cells for .NET 独立于 Office Automation 处理 Microsoft Excel 文件，并为您提供创建和操作电子表格的强大工具。

{{% /alert %}}

## **在 Cells 上添加和删除评论**

向单元格添加注释：

1. 打开现有的 Excel 文件。
1. 向单元格添加注释。
1. 保存文件。

要删除评论，过程类似，只是删除评论。

下面的代码示例首先说明了如何[添加评论](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)然后如何[删除评论](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)使用 VSTO 或 Aspose.Cells for .NET。

## **插入评论**

这些代码片段展示了如何首先使用[VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#, VB) 然后用[Aspose.Cells for .NET](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C#，VB）。

### **使用 VSTO 插入评论**

**C#**

{{< highlight "csharp" >}}

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

### **使用 Aspose.Cells for .NET 插入评论**

**C#**

{{< highlight "csharp" >}}

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

要从单元格中删除注释，请使用以下代码行[VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C#，VB）和[Aspose.Cells](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)for .NET（C#，越南语）。

### **使用 VSTO 删除评论**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **使用 Aspose.Cells for .NET 删除评论**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
