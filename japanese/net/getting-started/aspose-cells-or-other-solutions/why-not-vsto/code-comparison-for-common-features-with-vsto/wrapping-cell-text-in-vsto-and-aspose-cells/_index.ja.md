---
title: VSTO の Cell テキストと Aspose.Cells の折り返し
type: docs
weight: 250
url: /ja/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
2 つのセル (折り返されたテキストのあるセルとないセル) を持つワークシートを作成するには:

1. ワークシートを設定します。
 1. ワークブックを作成します。
 1. 最初のワークシートにアクセスします。
1. テキストを追加：
 1. セル A1 にテキストを追加します。
 1. 折り返されたテキストをセル A5 に追加します。
1. スプレッドシートを保存します。
 The code samples below show how to perform these steps using VSTO with either C#. Aspose.Cells for .NET を使用して同じことを行う方法を示すコード サンプルは、C# のいずれかを使用してすぐ後に続きます。

コードを実行すると、2 つのセルを含むスプレッドシートが作成されます。

## **VSTO Excel を使用した出力**

![todo:画像_代替_文章](picture1.png)

## **Aspose.Cells for .NET を使用して出力**

![todo:画像_代替_文章](picture2.png)

## **VSTO**

{{< highlight "csharp" >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\)。ジップ）
