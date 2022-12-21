---
title: Aspose.Cells で行の列ヘッダーを表示または非表示にする
type: docs
weight: 60
url: /ja/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Excel ファイル内のすべてのワークシートは、行と列に配置されたセルで構成されています。すべての行と列には、それらを識別し、個々のセルを識別するために使用される一意の値があります。たとえば、行には 1、2、3、4 などの番号が付けられ、列は A、B、C、D などのアルファベット順に並べられます。行と列の値はヘッダーに表示されます。開発者は、Aspose.Cells を使用して、これらの行と列のヘッダーの表示を制御できます。

{{% /alert %}}

## **ワークシートの表示の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。行ヘッダーと列ヘッダーの表示を制御するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)財産。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

の使用方法を示す完全な例を以下に示します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)ファイルの最初のワークシートの行ヘッダーと列ヘッダーを非表示にするプロパティ。

スクリーンショットは、入力ファイルである Book1.xls を示しています。これには、Sheet1、Sheet2、Sheet3 の 3 つのワークシートが含まれています。各ワークシートには、行と列のヘッダーが表示されています。

**Book1.xls: 修正前のワークシート**

![todo:画像_代替_文章](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls は、Workbook クラスの Open メソッドを呼び出して開かれ、最初のワークシートの行ヘッダーと列ヘッダーは非表示になります。変更されたファイルは、output.xls として保存されます。

**Output.xls: 修正後のワークシート** 

![todo:画像_代替_文章](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
