---
title: VSTOおよびAspose.Cellsでセルテキストを折り返す
type: docs
weight: 250
url: /ja/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

折り返しテキストおよび折り返しのないテキストを含むワークシートを作成するには:

1. ワークシートを設定します: 
   1. ワークブックを作成する。
   1. 最初のワークシートにアクセスします。
1. テキストを追加します: 
   1. セルA1にテキストを追加します。
   1. セルA5に折り返しテキストを追加します。
1. スプレッドシートを保存します。
   以下のコードサンプルは、VSTOを使用してこれらの手順をC#で実行する方法を示しています。同様のことをC#を使用して、Aspose.Cells for .NETを使用して行うコードサンプルが直後に続きます。

コードを実行すると、折り返されていないテキストを含むセルと折り返されたテキストを含むセルのあるスプレッドシートが作成されます。

## **VSTO Excelを使用した出力**

![todo:image_alt_text](picture1.png)

## **Aspose.Cells for .NETを使用した出力**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
