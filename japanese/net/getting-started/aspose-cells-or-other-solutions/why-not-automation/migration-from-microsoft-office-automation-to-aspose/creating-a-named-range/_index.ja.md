---
title: 名前付き範囲の作成
type: docs
weight: 70
url: /ja/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET を使用すると、開発者は、ユーザーがアプリケーションを介して Microsoft Excel で実行できるほとんどのタスクを実行できます。この記事では、名前付き範囲をプログラムで適用する方法について説明します。

名前付き範囲は、Excel スプレッドシートのセルまたはセル範囲に名前を割り当てることができる Excel の機能です。その後、数式で名前を使用して、セル (または範囲) を参照できます。範囲に適切な名前を付けると、数式が理解しやすくなります。

名前付き範囲はそのスコープ内で一意である必要があるため、ワークシート内の複数の範囲に同じ名前を使用しないでください。わかりやすい範囲名は、これを回避するのに役立ちます。たとえば、OrderSubTotal は SubTotal よりも説明的であり、シート上で重複する可能性も低くなります。

{{% /alert %}}

## **名前付き範囲の作成**

名前付き範囲を作成するには:

1. ワークシートを設定します。
 1. Application オブジェクトをインスタンス化します。
 (VSTO のみ。)
 1. ワークブックを追加します。
 1. 最初のシートを取得します。
1. 名前付き範囲を作成します。
 1. 範囲を定義します。
 1. 範囲に名前を付けます。
1. ファイルを保存します。

以下のコード例は、これらの手順を使用して実行する方法を示しています。[VSTO](/cells/ja/net/creating-a-named-range/) C# または Visual Basic で。以下のコード例は、[Aspose.Cells for .NET](/cells/ja/net/creating-a-named-range/)、再び C# または Visual Basic を使用します。
### **VSTO で名前付き範囲を作成する**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET で名前付き範囲を作成する**

**C#**

{{< highlight "csharp" >}}

 .......

Aspose.Cells を使用。

.......


// Workbook オブジェクトのインスタンス化

ワークブック ワークブック = 新しいワークブック();

//Excel ファイルの最初のワークシートにアクセスする

ワークシート worksheet = workbook.Worksheets[0];

// 名前付き範囲の作成

範囲 range = worksheet.Cells.CreateRange("A1", "B4");

//名前付き範囲の名前を設定

range.Name = "Test_Range";

 for (int 行 = 0; 行< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
