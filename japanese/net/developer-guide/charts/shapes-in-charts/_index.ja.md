---
title: チャート内の図形
description: Microsoft ExcelでAspose.Cells for .NETを使用してコントロールを追加し、チャートをカスタマイズする方法を学びます。このガイドでは、チャート要素を操作し、書式を調整し、チャート全体の外観と使いやすさを向上させる方法を示します。
keywords: Aspose.Cells for .NET、チャートコントロール、チャートのカスタマイズ、Microsoft Excel、チャート要素、書式設定。
type: docs
weight: 70
url: /ja/net/controls-in-charts/
---

{{% alert color="primary" %}}

時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段を提供します。
Aspose.Cellsを使用して、チャートにラベルを追加したり操作したりすることができます。

クラスには [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart) という名前のメソッドを備えた [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) クラス があります。 このメソッドを使用してチャートにラベルコントロールを追加します。 このメソッドに使用されるパラメータのリストは以下の通りです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) オブジェクトを返します。 [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) クラス はチャート内のラベルを表します。 いくつかの重要なメンバを持っています：

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (プロパティ) - ラベルのキャプション文字列を指定します。
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **チャートにテキストボックスコントロールを追加**

レポートで重要な情報を強調表示する一つの方法は、テキストボックスを使用することです。たとえば、企業名を表示したり、最高の売上地域を示したりするためにテキストを入力します。 [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) クラス には [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart) という名前のメソッドがあり、これを使用してチャートにテキストボックスコントロールを追加します。以下は、このメソッドに使用されるパラメータのリストです：

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) クラスは、画像オブジェクトをチャートに追加するために使用される[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用すると、[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype)列挙型を使用して、チャートシートにチェックボックスを挿入することができます。以下の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
