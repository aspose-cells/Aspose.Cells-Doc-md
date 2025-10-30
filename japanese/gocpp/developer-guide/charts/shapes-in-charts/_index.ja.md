---
title: Go言語とC++によるチャート内のシェイプ
linktitle: チャート内の図形
description: Aspose.Cells for C++を使ってMicrosoft Excelでチャートのコントロールを追加しカスタマイズする方法を学びます。ガイドでは、チャート要素の操作、書式設定の調整、全体的な外観と使いやすさの向上を示します。
keywords: Aspose.Cells for C++、チャートコントロール、チャートのカスタマイズ、Microsoft Excel、チャート要素、書式設定。
type: docs
weight: 70
url: /ja/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段を提供します。
Aspose.Cellsを使用して、チャートにラベルを追加したり操作したりすることができます。

 [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) クラスは [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/) というメソッドを持ち、チャートにラベルコントロールを追加するために使用されます。以下は、そのメソッドに使用されるパラメータのリストです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/) オブジェクトを返します。[**Label**](https://reference.aspose.com/cells/go-cpp/label/) クラスはチャート内のラベルを表し、重要なメンバーをいくつか持ちます:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/)（プロパティ） – ラベルのキャプション文字列を指定します。
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **チャートにテキストボックスコントロールを追加**

レポートの重要な情報をハイライト表示する一つの方法は、テキストボックスを使用することです。例として、会社名を強調したり、売上が最も高い地域を示すためにテキストを入力します。[**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/)というメソッドは、チャートにテキストボックスコントロールを追加するために使用されます。以下は、そのメソッドに使用されるパラメータリストです。

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは[**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/)オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/)クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/)クラスは[**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/)というメソッドを提供し、これを使ってチャートに画像オブジェクトを追加します。以下は、そのメソッドに使用されるパラメータリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/)オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/go-cpp/picture/)クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用すると、[**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/)列挙型を使用して、チャートシートにチェックボックスを挿入することができます。以下の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/cpp/add-wordart-watermark-to-chart/)
