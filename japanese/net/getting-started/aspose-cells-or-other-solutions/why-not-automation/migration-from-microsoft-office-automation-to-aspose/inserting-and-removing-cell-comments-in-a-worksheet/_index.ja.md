---
title: ワークシートにセルコメントを挿入および削除する
type: docs
weight: 30
url: /ja/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

一般的に、コメントはワークシート内のセルに追加情報を追加するために使用されます。必要なくなったら削除します。コメントは特定の値の文書化や、式の動作を覚えておくのに役立ちます。セル上にマウスポインタを移動させると、コメントが小さなボックスに表示されます。

この記事では、VSTOとAspose.Cells for .NETを使用して、セルにコメントを追加および削除する方法を比較します。Aspose.Cells for .NETは、オフィス自動化に依存せずにMicrosoft Excelファイルで動作し、スプレッドシートの作成と操作に強力なツールを提供します。

{{% /alert %}}

## **セルにコメントを追加および削除する**

セルにコメントを追加するには：

1. 既存のExcelファイルを開く。
1. セルにコメントを追加します。
1. ファイルを保存します。

コメントを削除するには、コメントを削除すること以外は、プロセスが似ています。

以下のコードサンプルは、VSTOまたはAspose.Cells for .NETを使用して、まず[コメントを追加](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)し、その後に[コメントを削除](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)する方法を示しています。

## **コメントの挿入**

これらのコードスニペットは、まず[VSTO](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#, VB)でセルにコメントを追加し、次に[Aspose.Cells for .NET](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#, VB)で同様の操作を行う方法を示しています。

### **VSTOでのコメントの挿入**

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

### **Aspose.Cells for .NETでのコメントの挿入**

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

## **コメントの削除**

セルからコメントを削除するには、.NET向けの[VSTO](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#, VB)と[Aspose.Cells](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#, VB)のコードを使用します。

### **VSTOでのコメントの削除**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Aspose.Cells for .NETでのコメントの削除**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
