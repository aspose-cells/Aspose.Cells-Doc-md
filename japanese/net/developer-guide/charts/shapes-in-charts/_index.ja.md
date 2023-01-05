---
title: チャートの形状
type: docs
weight: 70
url: /ja/net/controls-in-charts/
---
{{% alert color="primary" %}}

ラベル、テキスト ボックス、画像などの描画オブジェクトをグラフに挿入する必要がある場合があります。 Aspose.Cells は、実行時にチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートへのラベル コントロールの追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。
Aspose.Cells を使用すると、チャートにもラベルを追加して操作できます。

の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)、チャートにラベル コントロールを追加するために使用されます。以下は、メソッドに使用されるパラメーターのリストです。

- **上**– グラフ領域の 1/4000 単位での左上隅からのラベルの垂直オフセット。
- **左**– グラフ領域の 1/4000 単位での左上隅からのラベルの垂直オフセット。
- **身長**– グラフ エリアの 1/4000 単位のラベルの高さ。
- **幅** – グラフ領域の 1/4000 単位のラベルの幅。

メソッドは戻ります[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)物体。の[**ラベル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)クラスはチャートのラベルを表します。いくつかの重要なメンバーがあります。

- [**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(プロパティ) – ラベルのキャプション文字列を指定します。
- [**塗りつぶし**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (プロパティ) – 塗りつぶしの色の属性を指定します。

次の例は、チャートにラベルを追加する方法を示しています。この例では、デザイナー ファイル (**exp_piechart.xls**) にグラフが含まれています。このファイルを使用して、チャートにラベルを挿入します。以下は、チャートにラベルを追加するための元のコードです。コードを実行すると、次の出力が生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **TextBox コントロールをチャートに追加する**

レポートで重要な情報を強調する 1 つの方法は、テキスト ボックスを使用することです。たとえば、テキストを入力して会社名を強調表示したり、売上高が最も多い地域を示したりします。の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)、テキスト ボックス コントロールをチャートに追加するために使用されます。以下は、メソッドに使用されるパラメーター リストです。

- **上** – グラフ領域の 1/4000 単位での左上隅からのテキスト ボックスの垂直オフセット。
- **左** – グラフ領域の 1/4000 単位での左上隅からのテキスト ボックスの垂直オフセット。
- **身長**– テキスト ボックスの高さ (グラフ領域の 1/4000 単位)。
- **幅** – テキスト ボックスの幅 (グラフ領域の 1/4000 単位)。

メソッドは戻ります[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)物体。の[**テキストボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)クラスはチャート内のテキスト ボックスを表します。

次の例は、テキスト ボックスをグラフに追加する方法を示しています。この例では、以前のデザイナー ファイル (**exp_piechart.xls**) にグラフが含まれています。このファイルを使用して、テキスト ボックスをチャートに挿入し、チャート タイトルを表示します。以下は、チャートにテキスト ボックスを追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **チャートに画像を追加する**

Aspose.Cells を使用すると、画像をグラフに挿入できます。たとえば、図を追加して図やその内容を強調したり意味を持たせたり、ブランド イメージ ファイルを挿入したりします。

の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)、チャートに画像オブジェクトを追加するために使用されます。以下は、メソッドに使用されるパラメーター リストです。

- **上**– グラフ領域の 1/4000 単位での左上隅からのピクチャの垂直オフセット。
- **左**– グラフ領域の 1/4000 単位での左上隅からのピクチャの垂直オフセット。
- **ストリーム**– 画像データを含むストリーム オブジェクト。
- **幅スケール**– 画像幅のスケール、パーセント値。
- **高さスケール**– 画像の高さのスケール、パーセント値。

メソッドは[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。の[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)クラスは、チャート内の画像オブジェクトを表します。

次の例は、グラフに画像を追加する方法を示しています。この例では、以前のデザイナー ファイル (**exp_piechart.xls**) にグラフが含まれています。このファイルを使用して、画像をチャートに挿入します。以下は、チャートに画像を追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **チャートにチェックボックスを追加する**

 Aspose.Cells を使用すると、チャート シートにチェックボックスを挿入できます。[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype)列挙。次の例は、グラフ シートにチェックボックスを追加する方法を示しています。

次の図は、出力ファイルにチェックボックスがあるグラフ シートを示しています。

![todo:画像_代替_文章](controls-in-charts_1.jpg)

の[出力ファイル](101089316.xlsx)参照用に、次のコード スニペットによって生成されたコードを添付します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **先行トピック**
- [ワードアートの透かしをグラフに追加する](/cells/ja/net/add-wordart-watermark-to-chart/)
