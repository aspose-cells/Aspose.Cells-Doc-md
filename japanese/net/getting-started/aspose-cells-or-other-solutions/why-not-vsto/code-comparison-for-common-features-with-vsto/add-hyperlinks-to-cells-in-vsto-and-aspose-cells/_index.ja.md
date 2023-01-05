---
title: ハイパーリンクを VSTO の Cells と Aspose.Cells に追加します。
type: docs
weight: 20
url: /ja/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
スプレッドシートのセルにハイパーリンクを追加するには、次の手順を実行します。

1. ワークシートを設定します。
 1. Application オブジェクトをインスタンス化します (VSTO のみ)。
 1. ワークブックを追加します。
 1. 最初のシートを取得します。
 1. ハイパーリンクを追加するセルにテキストを追加します。
1. ハイパーリンクを追加します。
1. ドキュメントを保存します。

これらの手順は、以下のコード例に示されています。最初の例は、VSTO を C# と共に使用してセルにハイパーリンクを追加する方法を示しています。次の例は、Aspose.Cells for .NET を使用して同じことを行う方法を示し、再び C# を使用します。

コード サンプルは、最初のワークシートのセル A1 にハイパーリンクを含む Excel ファイルを生成します。

![todo:画像_代替_文章](picture1.png)

ハイパーリンクがセル A1 に追加されます。

## **VSTO**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\)。ジップ）
