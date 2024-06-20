---
title: Aspose.Cellsでデータをリンクするハイパーリンクの追加
type: docs
weight: 10
url: /ja/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。

Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}}

## **ハイパーリンクの追加**

Aspose.Cellsを使用してセルには3種類のハイパーリンクを追加することができます:

- [URLへのリンクの追加](#adding-link-to-a-url)。
- [同じファイル内の別のセルへのリンクの追加](#adding-a-link-to-a-cell-in-the-same-file)。
- [外部ファイルへのリンクの追加](#adding-a-link-to-an-external-file)。

Aspose.Cellsでは、開発者がAPIを使用するか、[デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)（ハイパーリンクが手動で作成され、Aspose.Cellsを使用して他のスプレッドシートにインポートされるスプレッドシート）を使用して、Excelファイルにハイパーリンクを追加できます。

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)が含まれ、Excelファイル内の各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、Excelファイルにさまざまなハイパーリンクを追加するための異なるメソッドが提供されています。

### **URLへのリンクの追加**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクションが含まれています。ハイパーリンクコレクション内の各アイテムはハイパーリンクを表します。Addメソッドを呼び出すことで、URLへのハイパーリンクを追加できます。Addメソッドには以下のパラメータが必要です:

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。

**C#**

{{< highlight csharp >}}

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

### **同じファイル内のセルへのリンクの追加**

ハイパーリンクコレクションのAddメソッドを呼び出すことで、同じExcelファイルのセルにハイパーリンクを追加することが可能です。オーバーロードされたメソッドのバージョンの1つは、次のパラメータを取ります:

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

**C#**

{{< highlight csharp >}}

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

外部Excelファイルにハイパーリンクを追加することが可能で、HyperlinksコレクションのAddメソッドを呼び出します。Addメソッドには以下のパラメータが必要です:

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。

**C#**

{{< highlight csharp >}}

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

## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
