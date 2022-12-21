---
title: チャートのコントロール
linktitle: チャート内の形状
type: docs
weight: 60
url: /ja/java/controls-in-charts/
---
{{% alert color="primary" %}}

ラベル、テキスト ボックス、画像などの描画オブジェクトをチャートに挿入する必要がある場合があります。 Aspose.Cells は、実行時にチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートへのラベル コントロールの追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。 Aspose.Cells を使用すると、チャートにもラベルを追加して操作できます。

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)クラスは、という名前のメソッドを提供します[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int))、チャートにラベル コントロールを追加するために使用されます。以下は、メソッドに使用されるパラメーターのリストです。

- **上**– グラフ領域の 1/4000 単位での左上隅からのラベルの垂直オフセット。
- **左**– グラフ領域の 1/4000 単位での左上隅からのラベルの垂直オフセット。
- **身長**– グラフ エリアの 1/4000 単位のラベルの高さ。
- **幅** – グラフ エリアの 1/4000 単位のラベルの幅。

メソッドは、[**ラベル**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)クラス、ここで[**ラベル**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)クラスはチャートのラベルを表します。以下に詳述するように、いくつかの重要なメンバーがあります。

- [**文章**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)プロパティは、ラベルのキャプション文字列を指定します。
- [**塗りつぶし**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill)プロパティは、塗りつぶしの色属性を指定します。

次の例は、チャートにラベルを追加する方法を示しています。この例では、チャートを含むデザイナー ファイルを使用します。このファイルを使用して、チャートにラベルを挿入します。

以下は、デザイナー ファイルのスクリーンショットです。

**デザイナーチャート**

![todo:画像_代替_文章](controls-in-charts_1.png)

以下は、チャートにラベルを追加するための元のコードです。コードを実行すると、次の出力が生成されます。

**チャートにラベルが追加されます**

![todo:画像_代替_文章](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **TextBox コントロールをチャートに追加する**

レポートで重要な情報を強調する 1 つの方法は、テキスト ボックスを使用することです。たとえば、テキストを入力して会社名を強調表示したり、売上高が最も多い地域を示したりします。の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)クラスは、という名前のメソッドを提供します[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)) を使用して、テキスト ボックス コントロールをグラフに追加します。以下は、メソッドに使用されるパラメーター リストです。

- **上** – グラフ領域の 1/4000 単位での左上隅からのテキスト ボックスの垂直オフセット。
- **左** – グラフ領域の 1/4000 単位での左上隅からのテキスト ボックスの垂直オフセット。
- **身長**– テキスト ボックスの高さ (グラフ領域の 1/4000 単位)。
- **幅** – テキスト ボックスの幅 (グラフ領域の 1/4000 単位)。

メソッドは、[**テキストボックス**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)クラス[**テキストボックス**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)クラスはチャート内のテキスト ボックスを表します。

次の例は、テキスト ボックスをグラフに追加する方法を示しています。この例では、チャートを含む以前のデザイナー ファイルを使用します。このファイルを使用して、テキスト ボックスをチャートに挿入し、チャート タイトルを表示します。

以下は、チャートにテキスト ボックスを追加するための元のコードです。コードを実行すると、次の出力が生成されます。

**グラフにテキスト ボックスが追加されます**

![todo:画像_代替_文章](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **チャートに画像を追加する**

Aspose.Cells を使用すると、画像をグラフに挿入できます。たとえば、図を追加して図やその内容を強調したり意味を持たせたり、ブランド イメージ ファイルを挿入したりします。

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)クラスは、という名前のメソッドを提供します[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)) を使用して、画像オブジェクトをチャートに追加します。以下は、メソッドに使用されるパラメーター リストです。

- **上**– グラフ領域の 1/4000 単位での左上隅からのピクチャの垂直オフセット。
- **左**– グラフ領域の 1/4000 単位での左上隅からのピクチャの垂直オフセット。
- **ストリーム**– 画像データを含むストリーム オブジェクト。
- **幅スケール**– 画像幅のスケール、パーセント値。
- **高さスケール**– 画像の高さのスケール、パーセント値。

メソッドは、[**写真**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)クラス[**写真**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)クラスは、チャート内の画像オブジェクトを表します。

次の例は、グラフに画像を追加する方法を示しています。この例では、チャートを含む以前のデザイナー ファイルを使用しています。このファイルを使用して、画像をチャートに挿入します。

以下は、チャートに画像を追加するための元のコードです。コードを実行すると、次の出力が生成されます

**グラフに画像が挿入されます**

![todo:画像_代替_文章](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **チャートにチェックボックスを追加する**

Aspose.Cells を使用すると、チャート シートにチェックボックスを挿入できます。[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType)列挙。次の例は、グラフ シートにチェックボックスを追加する方法を示しています。

次の図は、出力ファイルにチェックボックスがあるグラフ シートを示しています。

![todo:画像_代替_文章](controls-in-charts_5.jpg)

の[出力ファイル](InsertCheckboxInChartSheet_out.xlsx)参照用に、次のコード スニペットによって生成されたコードを添付します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
