---
title: ワークシートでの Cell コメントの挿入と削除
type: docs
weight: 30
url: /ja/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

通常、コメントは、ワークシートのセルに追加情報を追加するために使用されます。私たちはそれらを時々使用し、必要がなくなったら削除します。コメントは、特定の値を文書化する必要がある場合や、式の機能を覚えるのに役立ちます。コメントのあるセルにマウス ポインターを移動すると、小さなボックスにコメントが表示されます。

この記事では、VSTO と Aspose.Cells for .NET を使用してセルにコメントを追加および削除する方法を比較します。

{{% /alert %}}

## **Cells のコメントの追加と削除**

セルにコメントを追加するには:

1. 既存の Excel ファイルを開きます。
1. セルにコメントを追加します。
1. ファイルを保存します。

コメントを削除する場合も、プロセスは似ていますが、コメントが削除される点が異なります。

以下のコード サンプルは、最初に次の方法を示しています。[コメントを追加](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)そして、どのように[コメントを削除する](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)VSTO または Aspose.Cells for .NET のいずれかを使用します。

## **コメントの挿入**

これらのコード スニペットは、最初にセルにコメントを追加する方法を示しています。[VSTO](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#、VB) と[Aspose.Cells for .NET](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#、VB)。

### **VSTO でコメントを挿入する**

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

### **Aspose.Cells for .NET でコメントを挿入する**

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

## **コメントの削除**

セルからコメントを削除するには、次のコード行を使用します[VSTO](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)(C#、VB) および[Aspose.Cells](/cells/ja/net/inserting-and-removing-cell-comments-in-a-worksheet/)for .NET (C#、VB).

### **VSTO でコメントを削除する**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Aspose.Cells for .NET でコメントを削除する**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
