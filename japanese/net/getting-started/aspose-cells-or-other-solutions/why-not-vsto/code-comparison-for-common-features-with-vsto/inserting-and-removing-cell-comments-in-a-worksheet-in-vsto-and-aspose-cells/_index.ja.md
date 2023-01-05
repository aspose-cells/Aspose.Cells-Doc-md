---
title: VSTO および Aspose.Cells のワークシートでの Cell コメントの挿入と削除
type: docs
weight: 150
url: /ja/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---
セルにコメントを追加するには:

1. 既存の Excel ファイルを開きます。
1. セルにコメントを追加します。
1. ファイルを保存します。

コメントを削除する場合も、プロセスは似ていますが、コメントが削除される点が異なります。

以下のコード サンプルは、最初にコメントを追加する方法を示し、次に VSTO または Aspose.Cells for .NET を使用してコメントを削除する方法を示しています。
## **コメントの挿入**
これらのコード スニペットは、最初に VSTO (C#) を使用して、次に Aspose.Cells for .NET (C#) を使用してセルにコメントを追加する方法を示しています。
### **VSTO**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

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
## **コメントの削除**
セルからコメントを削除するには、VSTO (C#) および Aspose.Cells for .NET (C#) の次のコード行を使用します。
### **VSTO**
{{< highlight "csharp" >}}

 //Remove the comment.

  rng1.Comment.Delete();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //removing comments

 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\)。ジップ）
