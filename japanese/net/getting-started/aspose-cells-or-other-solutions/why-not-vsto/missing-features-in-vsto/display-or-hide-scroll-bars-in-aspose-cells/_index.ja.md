---
title: Aspose.Cells でスクロール バーを表示または非表示にする
type: docs
weight: 70
url: /ja/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

スクロール バーは、ファイルの内容をナビゲートするためによく使用されます。通常、スクロール バーには次の 2 種類があります。

- 垂直スクロール バー
- 水平スクロール バー

Microsoft Excel には、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロール バーも用意されています。 Aspose.Cells を使用すると、開発者は Excel ファイルで両方のタイプのスクロール バーの表示を制御できます。

{{% /alert %}}

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。スクロール バーの表示を制御するには、[**ワークブック設定**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings)クラス'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティ。[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)はブール型のプロパティです。つまり、これらのプロパティは格納のみ可能です。**真実**また**間違い**値。

以下は、Excel ファイル book1.xls を開き、両方のスクロール バーを非表示にしてから、変更したファイルを output.xls として保存する完全なコードです。

以下のスクリーンショットは、両方のスクロール バーを含む Book1.xls ファイルを示しています。変更されたファイルは output.xls ファイルとして保存されます。これも以下に示します。

**Book1.xls: 変更前の Excel ファイル**

![todo:画像_代替_文章](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls：修正後のExcelファイル**

![todo:画像_代替_文章](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
