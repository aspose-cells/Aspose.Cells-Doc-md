---
title: セルにハイパーリンクを追加する
type: docs
weight: 60
url: /ja/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NETを使用すると、Microsoft Excelでユーザーが実行できるほとんどのタスクをアプリケーションを通じて実行できます。この記事では、VSTOとAspose.Cells for .NETを使用してワークシートのセルにハイパーリンクを追加する方法を比較しています。

{{% /alert %}}

## **セルへのハイパーリンクの追加**

スプレッドシートのセルにハイパーリンクを追加するには、以下の手順を実行してください:

1. ワークシートを設定します:
   1. アプリケーションオブジェクトをインスタンス化します。
      （VSTOの場合に限る。）
   1. ワークブックを追加する
   1. 最初のシートを取得する
   1. ハイパーリンクを追加するセルにテキストを追加する
1. ハイパーリンクを追加する
1. ドキュメントを保存する

これらの手順は以下のコード例で示されています。最初の例では、[VSTO](/cells/ja/net/add-hyperlinks-to-cells/)を使用してセルにハイパーリンクを追加する方法（C#またはVisual Basicのいずれか）が示されています。その後の例では、[Aspose.Cells for .NET](/cells/ja/net/add-hyperlinks-to-cells/)を使用して同じことを行う方法（C#またはVisual Basicのいずれか）が示されています。

コードサンプルは、最初のワークシートのセルA1にハイパーリンクを持つExcelファイルを生成します。

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**セルA1にハイパーリンクが追加されます。**

### **VSTOを使用したセルへのハイパーリンクの追加**

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

### **Aspose.Cells for .NETを使用したセルへのハイパーリンクの追加**

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
