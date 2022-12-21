---
title: ワークシートの Cells に罫線を追加する
type: docs
weight: 50
url: /ja/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET を使用すると、ユーザーが Microsoft Excel で実行できるほぼすべてのタスクをアプリケーションから実行できます。 Aspose.Cells は高性能で堅牢であり、Microsoft 自動化とは独立して動作するという追加の利点があります。この記事では、VSTO と比較して、Aspose.Cells for .NET を使用してワークシートのセルに罫線を追加する方法を示します。

{{% /alert %}}

## **Cells に罫線を追加する**

スプレッドシートのセルに罫線を追加するには、次の手順を実行します。

1. ワークシートを設定します。
 1. Application オブジェクトをインスタンス化します。
 (VSTO のみ。)
 1. ワークブックを追加します。
 1. 最初のシートを取得します。
 1. 罫線を追加するセルにテキストを追加します。
1. 境界線を追加:
 1. 範囲を定義します。
 1. 境界線スタイルを範囲に適用します。
設定する各範囲と境界線スタイルごとに繰り返します。この例では、ヘアライン、細線、中線、太線を適用しています。
1. 終了：
 1. セルが入っている列をテキストに合わせて自動調整します。
 1. ドキュメントを保存します。

これらの手順を以下のコードに示します。最初のコード例は、使用してそれらを実装する方法を示しています[VSTO](/cells/ja/net/add-borders-to-cells-in-a-worksheet/)C# または Visual Basic で。 VSTO の例の後に、次を使用して同じ手順を実行する方法を示す例があります。[Aspose.Cells for .NET](/cells/ja/net/add-borders-to-cells-in-a-worksheet/)、再び C# または Visual Basic を使用します。 Aspose.Cells は効率的なコーディングのために最適化されているため、Aspose.Cells のコード サンプルはかなり短くなります。

このコードは、最初のシートに多数のセルを含む Excel ファイルを生成し、それぞれに異なる境界線があります。

![todo:画像_代替_文章](add-borders-to-cells-in-a-worksheet_1.png)

**Cells 縁取りあり。**

### **VSTO を使用して境界線を追加する**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET を使用してボーダーを追加する**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
