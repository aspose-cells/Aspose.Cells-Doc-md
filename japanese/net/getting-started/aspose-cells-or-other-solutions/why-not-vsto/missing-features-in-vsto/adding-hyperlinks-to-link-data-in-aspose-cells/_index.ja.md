---
title: Aspose.Cells のリンク データにハイパーリンクを追加する
type: docs
weight: 10
url: /ja/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

ハイパーリンクは、2 つのエンティティ間のリンクを作成するために使用されます。特に Web サイトでは、誰もがハイパーリンクの使用に慣れています。

Aspose.Cells を使用すると、開発者は Microsoft Excel ファイルにさまざまな種類のハイパーリンクを作成できます。このトピックでは、Aspose.Cells でサポートされているハイパーリンクの種類と、それらを Excel ファイルで使用する方法について説明します。

{{% /alert %}}

## **ハイパーリンクの追加**

Aspose.Cells を使用して、3 種類のハイパーリンクをセルに追加できます。

- [URL へのリンクの追加](#adding-link-to-a-url).
- [同じファイル内の別のセルへのリンクを追加する](#adding-a-link-to-a-cell-in-the-same-file).
- [外部ファイルへのリンクの追加](#adding-a-link-to-an-external-file).

Aspose.Cells を使用すると、開発者は API または[デザイナー スプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)(ハイパーリンクが手動で作成され、他のスプレッドシートにインポートするために Aspose.Cells が使用されるスプレッドシート)。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、さまざまなハイパーリンクを Excel ファイルに追加するためのさまざまなメソッドが用意されています。

### **URL へのリンクの追加**

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**ハイパーリンク**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクション。 Hyperlinks コレクションの各アイテムは、ハイパーリンクを表します。 Hyperlinks コレクションの Add メソッドを呼び出して、URL にハイパーリンクを追加します。 Add メソッドは、次のパラメーターを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数
- URL、URL アドレス。

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **同じファイルに Cell へのリンクを追加する**

Hyperlink コレクションの Add メソッドを呼び出すことで、同じ Excel ファイル内のセルにハイパーリンクを追加できます。 Add メソッドは、内部ハイパーリンクと外部ハイパーリンクの両方に対して機能します。オーバーロードされたメソッドの 1 つのバージョンは、次のパラメーターを取ります。

- Cell name,ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲット セルのアドレス。

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **外部ファイルへのリンクの追加**

Hyperlinks コレクションの Add メソッドを呼び出すことにより、外部の Excel ファイルにハイパーリンクを追加することができます。 Add メソッドは、次のパラメーターを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲットのアドレス、外部 Excel ファイル。

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
