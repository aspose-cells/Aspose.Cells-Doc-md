---
title: VSTO および Aspose.Cells で名前付き範囲を作成する
type: docs
weight: 90
url: /ja/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
名前付き範囲を作成するには:

1. ワークシートを設定します。
 1. Application オブジェクトをインスタンス化します (VSTO のみ)。
 1. ワークブックを追加します。
 1. 最初のシートを取得します。
1. 名前付き範囲を作成します。
 1. 範囲を定義します。
 1. 範囲に名前を付けます。
 1. ファイルを保存します。

The code examples below show how to perform these steps using VSTO with either C#. 次のコード例は、Aspose.Cells for .NET を使用して同じことを行う方法を示しています。
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

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

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

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

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\)。ジップ）
