---
title: チャート内のコントロール
linktitle: チャート内の図形
type: docs
weight: 60
url: /ja/java/controls-in-charts/
---

{{% alert color="primary" %}}

時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。Aspose.Cellsを使用して、チャートにラベルを追加および操作できます。

クラス [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) は、ラベルコントロールをチャートに追加するための [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)) メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです:

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** – ラベルの幅（チャート領域の1/4000単位）。

メソッドは、ラベルのチャート内の重要なメンバーを詳細に示す [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) クラスのオブジェクトを返します。以下は、その重要なメンバーのいくつかです:

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) プロパティはラベルのキャプション文字列を指定します。
- [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) プロパティは塗りつぶしの色の属性を指定します。

次の例は、チャートにラベルを追加する方法を示しています。この例では、チャートが含まれるデザイナーファイルを使用します。このファイルを使用して、チャートにラベルを挿入します。

以下は、デザイナーファイルのスクリーンショットです。

**デザイナーチャート**

![todo:image_alt_text](controls-in-charts_1.png)

チャートにラベルを追加するための元のコードは以下のとおりです。コードを実行すると、次の出力が生成されます。

**チャートにラベルが追加されます**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **チャートにテキストボックスコントロールを追加**

レポートで重要な情報を強調表示する一つの方法は、テキストボックスを使用することです。たとえば、企業名を表示したり、最高の売上地域を示したりするためにテキストを入力します。 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) クラス には [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)) という名前のメソッドがあり、これを使用してチャートにテキストボックスコントロールを追加します。以下は、このメソッドに使用されるパラメータのリストです：

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** – チャートエリアの左上隅からのテキストボックスの垂直オフセット（1/4000ユニット）。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは、[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)クラスのオブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)クラスは、チャート内のテキストボックスを表します。

次の例は、チャートにテキストボックスを追加する方法を示しています。この例では、前のデザイナーファイルを使用しています。このファイルを使用して、チャートにテキストボックスを挿入してチャートのタイトルを表示します。

以下は、チャートにテキストボックスを追加するための元のコードです。コードを実行すると、以下の出力が生成されます。

**チャートにテキストボックスが追加されています**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) クラスは、画像オブジェクトをチャートに追加するために使用される[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int))メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは、[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)クラスのオブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)クラスは、チャート内の画像オブジェクトを表します。

以下の例は、チャートに画像を追加する方法を示しています。この例では、前のデザイナーファイルを使用して、チャート内に画像を挿入しています。

以下は、チャートに画像を追加するための元のコードです。コードを実行すると、以下の出力が生成されます。

**画像がチャートに挿入されます**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用して、チャートシートにチェックボックスを挿入できます。次の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_5.jpg)

以下のコードスニペットによって生成された[出力ファイル](InsertCheckboxInChartSheet_out.xlsx)を参照のために添付します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
