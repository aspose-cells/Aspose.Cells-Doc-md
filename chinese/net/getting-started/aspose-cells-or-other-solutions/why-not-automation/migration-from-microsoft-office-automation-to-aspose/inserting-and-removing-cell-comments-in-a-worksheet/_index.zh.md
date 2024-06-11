---
title: 在工作表中插入和移除单元格批注
type: docs
weight: 30
url: /zh/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

通常，批注用于向工作表中的单元格添加附加信息。我们时不时地使用它们，并在不再需要它们时将它们删除。如果您需要记录特定值或帮助记住公式的作用，批注非常有用。当您将鼠标指针移动到具有批注的单元格上时，批注将在一个小框中弹出。

在本文中，我们比较了如何使用VSTO和Aspose.Cells for .NET向单元格添加和删除注释。Aspose.Cells for .NET与Microsoft Excel文件独立工作，并提供了强大的工具来创建和操作电子表格。

{{% /alert %}}

## **在单元格上添加和移除批注**

要向单元格添加注释：

1. 打开一个现有的Excel文件。
1. 向单元格添加评论。
1. 保存文件。

要删除注释，该过程类似，唯一不同之处在于注释被移除。

下面的代码示例首先说明如何使用VSTO或Aspose.Cells for .NET来[添加注释](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)，然后说明如何[删除注释](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)。

## **插入注释**

这些代码片段展示了如何首先使用[VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C#，VB），然后使用[Aspose.Cells for .NET](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C#，VB）向单元格添加注释。

### **使用 VSTO 插入批注**

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

### **使用Aspose.Cells for .NET插入注释**

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

## **移除评论**

要从单元格中移除批注，使用以下代码行来[从 VSTO](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/)（C#、VB）和[Aspose.Cells](/cells/zh/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET（C#、VB）移除批注。

### **使用 VSTO 移除批注**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **使用Aspose.Cells for .NET删除注释**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
