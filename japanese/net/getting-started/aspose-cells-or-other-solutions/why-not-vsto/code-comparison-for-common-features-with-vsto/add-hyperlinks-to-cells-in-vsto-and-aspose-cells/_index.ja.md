---
title: VSTOおよびAspose.Cellsでセルにハイパーリンクを追加する
type: docs
weight: 20
url: /ja/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

スプレッドシートのセルにハイパーリンクを追加するには、以下の手順を実行してください:

1. ワークシートを設定します: 
   1. Application オブジェクトをインスタンス化する。（VSTO のみ）
   1. ワークブックを追加する
   1. 最初のシートを取得する
   1. ハイパーリンクを追加するセルにテキストを追加する
1. ハイパーリンクを追加する
1. ドキュメントを保存する

これらの手順は以下のコード例で示されています。最初の例では、VSTOを使用してC#でセルにハイパーリンクを追加する方法が示されます。続く例では、同じことを行う方法がC#を使用して再度表示されますが、Aspose.Cells for .NETを使用します。

コードサンプルは、最初のワークシートのセルA1にハイパーリンクを持つExcelファイルを生成します。

![todo:image_alt_text](picture1.png)

ハイパーリンクがセルA1に追加されます。

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

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

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
