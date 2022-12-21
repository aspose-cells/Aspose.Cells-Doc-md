---
title: ハイパーリンクを Cells に追加
type: docs
weight: 60
url: /ja/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET を使用すると、ユーザーが Microsoft Excel で実行できるほぼすべてのタスクをアプリケーションから実行できます。この記事では、VSTO と Aspose.Cells for .NET を使用してワークシートのセルにハイパーリンクを追加する方法を比較します。

{{% /alert %}}

## **Cells へのハイパーリンクの追加**

スプレッドシートのセルにハイパーリンクを追加するには、次の手順を実行します。

1. ワークシートを設定します。
 1. Application オブジェクトをインスタンス化します。
 (VSTO のみ。)
 1. ワークブックを追加します。
 1. 最初のシートを取得します。
 1. ハイパーリンクを追加するセルにテキストを追加します。
1. ハイパーリンクを追加します。
1. ドキュメントを保存します。

これらの手順は、以下のコード例に示されています。最初の例は、使用方法を示しています[VSTO](/cells/ja/net/add-hyperlinks-to-cells/)セルにハイパーリンクを追加するには、C# または Visual Basic を使用します。以下の例は、以下を使用して同じことを行う方法を示しています。[Aspose.Cells for .NET](/cells/ja/net/add-hyperlinks-to-cells/)、再び C# または Visual Basic を使用します。

コード サンプルは、最初のワークシートのセル A1 にハイパーリンクを含む Excel ファイルを生成します。

![todo:画像_代替_文章](add-hyperlinks-to-cells_1.png)

**ハイパーリンクがセル A1 に追加されます。**

### **VSTO を使用して Cells にハイパーリンクを追加する**

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

### **Aspose.Cells for .NET で Cells にハイパーリンクを追加する**

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
