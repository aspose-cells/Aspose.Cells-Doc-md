---
title: 名前付き範囲を作成する
type: docs
weight: 70
url: /ja/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NETを使用すると、開発者はアプリケーションを通じてMicrosoft Excelでユーザーが行うことのほとんどを実行することができます。この記事では、名前付き範囲をプログラムで適用する方法について説明します。

名前付き範囲は、Excelのスプレッドシートでセルや範囲に名前を割り当てる機能です。これにより、数式でセル（または範囲）を参照するためにその名前を使用できます。分かりやすい名前付き範囲を使用すると、数式が理解しやすくなります。

名前付き範囲はそのスコープ内で一意である必要がありますので、ワークシート内で複数の範囲に同じ名前を使わないでください。説明的な範囲名を使用することでこれを避けることができます。例えば、OrderSubTotalはSubTotalよりも記述的であり、またシート上で重複する可能性が低くなります。

{{% /alert %}}

## **名前付き範囲の作成**

名前付き範囲を作成するには:

1. ワークシートを設定します:
   1. アプリケーションオブジェクトをインスタンス化します。
      （VSTOの場合に限る。）
   1. ワークブックを追加する
   1. 最初のシートを取得する
1. 名前付き範囲を作成する:
   1. 範囲を定義する
   1. 範囲に名前を付ける
1. ファイルを保存します。

以下のコード例は、[VSTO](/cells/ja/net/creating-a-named-range/)を使用してこれらの手順を実行する方法をC#またはVisual Basicで示しています。次に、同じことを[C#またはVisual Basic](/cells/ja/net/creating-a-named-range/)を使用して[Aspose.Cells for .NET](/cells/ja/net/creating-a-named-range/)で行う方法を示すコード例が続きます。
### **VSTOを使用した名前付き範囲の作成**

**C#**

{{< highlight csharp >}}

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

### **Aspose.Cells for .NETを使用した名前付き範囲の作成**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
