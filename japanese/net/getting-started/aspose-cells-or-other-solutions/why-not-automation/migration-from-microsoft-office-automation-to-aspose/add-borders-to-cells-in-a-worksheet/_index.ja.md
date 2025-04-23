---
title: ワークシートのセルにボーダーを追加する
type: docs
weight: 50
url: /ja/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NETを使用すると、Microsoft Excelでユーザーが実行できるほぼすべてのタスクをアプリケーションで実行できます。Aspose.Cellsは高性能で堅牢であり、Microsoft Automationに依存せずに動作する利点があります。この記事では、Aspose.Cells for .NETを使用してワークシートのセルにボーダーを追加する方法をVSTOと比較して説明します。

{{% /alert %}}

## **セルにボーダーを追加する**

スプレッドシートのセルに境界線を追加するには、以下の手順を実行してください:

1. ワークシートを設定します:
   1. アプリケーションオブジェクトをインスタンス化します。
      （VSTOの場合に限る。）
   1. ワークブックを追加する
   1. 最初のシートを取得する
   1. ボーダーを追加するセルにテキストを追加します。
1. 境界線を追加する:
   1. 範囲を定義する
   1. 範囲にボーダースタイルを適用します。
      設定したい各範囲とボーダースタイルごとに繰り返します。この例では、ヘアライン、細線、中線、太線が適用されています。
1. 終了:
   1. セルの入っている列を自動調整してテキストをきれいに合わせます。
   1. ドキュメントを保存する

これらの手順は、以下のコードで示されています。最初のコード例は[C#またはVisual Basic](/cells/ja/net/add-borders-to-cells-in-a-worksheet/)を使用してVSTOを実装する方法を示しています。VSTOの例の後に、[Aspose.Cells for .NETを使用した](/cells/ja/net/add-borders-to-cells-in-a-worksheet/)同じ手順を実行する方法を示す例があります。こちらもC#またはVisual Basicを使用しています。Aspose.Cellsのコードサンプルは、効率的なコーディングに最適化されているため、長くありません。

コードは、最初のシート上のいくつかのセルに異なる境界線を持つExcelファイルを生成します。

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**適用されたボーダーを持つセル。**

### **VSTOを使用してボーダーを追加する**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

### **Aspose.Cells for .NETを使用してボーダーを追加する**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
