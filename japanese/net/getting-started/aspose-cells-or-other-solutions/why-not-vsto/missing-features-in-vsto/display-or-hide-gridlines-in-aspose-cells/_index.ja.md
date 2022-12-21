---
title: Aspose.Cells でグリッド線を表示または非表示にする
type: docs
weight: 50
url: /ja/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

すべての Excel ワークシートには、既定でグリッド線があります。セルの輪郭を描くのに役立ち、特定のセルにデータを簡単に入力できます。グリッド線を使用すると、ワークシートをセルのコレクションとして表示でき、各セルを簡単に識別できます。

{{% /alert %}}

## **グリッド線の可視性の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。グリッド線の可視性を制御するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)財産。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

の使用を示す完全な例を以下に示します。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)のプロパティ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスを使用して、Excel ファイルの最初のワークシートのグリッド線を非表示にします。

下のスクリーンショットでは、Book1.xls ファイルに Sheet1、Sheet2、Sheet3 の 3 つのワークシートが含まれていることがわかります。すべてのワークシートにはグリッド線があります。

**Book1.xls: 変更前のワークシート ビュー** 

![todo:画像_代替_文章](display-or-hide-gridlines-in-aspose-cells_1.png)

Workbook クラスを使用して Book1.xls ファイルが開かれ、最初のワークシートのグリッド線が非表示になります。変更されたファイルは、output.xls として保存されます。

**Output.xls: 修正後のワークシート** 

![todo:画像_代替_文章](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
