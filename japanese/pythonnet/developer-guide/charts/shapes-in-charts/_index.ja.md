---
title: チャート内の図形
description: Aspose.Cells for Python via .NETを使ってMicrosoft Excelでコントロールを追加し、チャートをカスタマイズする方法を学びましょう。ガイドでは、チャート要素の操作、書式設定、および全体的な見た目と使いやすさの向上方法を示します。
keywords: Aspose.Cells for Python via .NET、チャートコントロール、チャートのカスタマイズ、Microsoft Excel、チャート要素、書式設定。
type: docs
weight: 70
url: /ja/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

時々、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cells for Python via .NETは、実行時にこれらのコントロールをチャートに追加できます。

{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段を提供します。
Aspose.Cells for Python via .NETは、チャートにラベルを追加および操作することを可能にします。

クラスには [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart) という名前のメソッドを備えた [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラス があります。 このメソッドを使用してチャートにラベルコントロールを追加します。 このメソッドに使用されるパラメータのリストは以下の通りです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) オブジェクトを返します。 [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) クラス はチャート内のラベルを表します。 いくつかの重要なメンバを持っています：

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (プロパティ) - ラベルのキャプション文字列を指定します。
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **チャートにテキストボックスコントロールを追加**

レポートで重要な情報を強調表示する一つの方法は、テキストボックスを使用することです。たとえば、企業名を表示したり、最高の売上地域を示したりするためにテキストを入力します。 [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラス には [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart) という名前のメソッドがあり、これを使用してチャートにテキストボックスコントロールを追加します。以下は、このメソッドに使用されるパラメータのリストです：

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **チャートに画像を追加する**

Aspose.Cells for Python via .NETは、チャートに画像を挿入することも可能です。例として、強調や内容に意味を持たせるために画像を追加したり、ブランド画像ファイルを挿入したりできます。

[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラスは、画像オブジェクトをチャートに追加するために使用される[**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart)メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **チャートにチェックボックスを追加する**

Aspose.Cells for Python via .NETは、[**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype)列挙体を使用してチャートシートにチェックボックスを挿入できます。以下の例では、チャートシートにチェックボックスを追加する方法を示します。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/python-net/add-wordart-watermark-to-chart/)
