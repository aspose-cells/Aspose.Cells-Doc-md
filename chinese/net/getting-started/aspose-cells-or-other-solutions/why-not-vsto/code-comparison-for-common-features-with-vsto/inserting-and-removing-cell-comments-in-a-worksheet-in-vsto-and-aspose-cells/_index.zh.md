---
title: 在VSTO和Aspose.Cells中插入和移除工作表中的单元格注释
type: docs
weight: 150
url: /zh/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---

要向单元格添加注释：

1. 打开一个现有的Excel文件。
1. 向单元格添加评论。
1. 保存文件。

要删除注释，该过程类似，唯一不同之处在于注释被移除。

下面的代码示例首先说明了如何添加评论，然后说明了如何使用VSTO或Aspose.Cells for .NET移除评论。
## **插入注释**
这些代码片段展示了如何首先使用VSTO（C＃）向单元格添加评论，然后再使用Aspose.Cells for .NET（C#）。
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

 Excel.Application excelApp = Application;

//Specify the template excel file path.

  string myPath = "Book1.xls";

//Open the excel file.

 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Get the A1 cell.

 Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

 rng1.AddComment("This is my comment");

//Save the file.

  excelApp.ActiveWorkbook.Save();

//Quit the Application.

  excelApp.Quit();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Specify the template excel file path.

string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

 Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

 int commentIndex = workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

 Comment comment = workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

 comment.Note = "This is my comment";

//Save As the excel file.

 workbook.Save("Book1.xls");

{{< /highlight >}}
## **移除评论**
要从单元格移除评论，请使用VSTO（C＃）和Aspose.Cells for .NET（C#）的以下代码行。
### **VSTO**
{{< highlight csharp >}}

 //Remove the comment.

  rng1.Comment.Delete();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //removing comments

 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
