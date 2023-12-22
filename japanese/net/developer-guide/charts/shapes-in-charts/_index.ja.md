---
title: グラフの形状
description: Aspose.Cells for .NET を使用してコントロールを追加し、Microsoft Excel でグラフをカスタマイズする方法を学びます。このガイドでは、グラフ要素を操作し、書式を調整し、グラフの全体的な外観と使いやすさを向上させる方法を説明します。
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /ja/net/controls-in-charts/
---
{{% alert color="primary" %}}

ラベル、テキスト ボックス、画像などの描画オブジェクトをグラフに挿入する必要がある場合があります。 Aspose.Cells は、実行時にコントロールをチャートに追加できます。

{{% /alert %}}

##  **チャートへのラベル コントロールの追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。
Aspose.Cells を使用すると、チャートにもラベルを追加して操作できます。

の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは次の名前のメソッドを提供します[**グラフにラベルを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)、ラベル コントロールをグラフに追加するために使用されます。以下は、このメソッドに使用されるパラメーターのリストです。

- **上**– グラフ領域の 1/4000 単位での、左上隅からのラベルの垂直方向のオフセット。
- **左**– グラフ領域の 1/4000 単位での、左上隅からのラベルの垂直方向のオフセット。
- **身長**– ラベルの高さ (グラフ領域の 1/4000 単位)。
- **幅** – ラベルの幅（グラフ領域の 1/4000 単位）。

メソッドは戻ります[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)物体。の[**ラベル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)class はチャート内のラベルを表します。いくつかの重要なメンバーが含まれています。

- [**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(プロパティ) – ラベルのキャプション文字列を指定します。
- [**埋める**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (プロパティ) – 塗りつぶしの色の属性を指定します。

次の例は、グラフにラベルを追加する方法を示しています。この例では、グラフが含まれるデザイナー ファイル (**exp_piechart.xls**) を使用します。このファイルを使用して、グラフにラベルを挿入します。以下は、グラフにラベルを追加するための元のコードです。コードを実行すると、次の出力が生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **TextBox コントロールをグラフに追加する**

レポート内の重要な情報を強調表示する 1 つの方法は、テキスト ボックスを使用することです。たとえば、会社名を強調表示したり、売上高が最も高い地域を示すテキストを入力します。の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは次の名前のメソッドを提供します[**グラフにテキストボックスを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)、テキスト ボックス コントロールをグラフに追加するために使用されます。このメソッドに使用されるパラメータのリストは次のとおりです。

- **上** – グラフ領域の 1/4000 単位での、左上隅からのテキスト ボックスの垂直方向のオフセット。
- **左** – グラフ領域の 1/4000 単位での、左上隅からのテキスト ボックスの垂直方向のオフセット。
- **身長** – テキスト ボックスの高さ (グラフ領域の 1/4000 単位)。
- **幅** – テキスト ボックスの幅 (グラフ領域の 1/4000 単位)。

メソッドは戻ります[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)物体。の[**テキストボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)クラスはグラフ内のテキスト ボックスを表します。

次の例は、グラフにテキスト ボックスを追加する方法を示しています。この例では、グラフが含まれている前のデザイナー ファイル (**exp_piechart.xls**) を使用します。このファイルを使用してグラフにテキスト ボックスを挿入し、グラフのタイトルを表示します。以下は、グラフにテキスト ボックスを追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **チャートに画像を追加する**

Aspose.Cells を使用すると、グラフに画像を挿入できます。たとえば、図やその内容を強調したり意味を与えたりするために画像を追加したり、ブランド画像ファイルを挿入したりできます。

の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは次の名前のメソッドを提供します[**チャートに画像を追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)、チャートに画像オブジェクトを追加するために使用されます。このメソッドに使用されるパラメータのリストは次のとおりです。

- **上** – チャート領域の 1/4000 単位での、左上隅からの画像の垂直方向のオフセット。
- **左** – チャート領域の 1/4000 単位での、左上隅からの画像の垂直方向のオフセット。
- **ストリーム**– 画像データを含むストリーム オブジェクト。
- **幅スケール**– 画像の幅のスケール、パーセンテージ値。
- **身長スケール**– 画像の高さのスケール、パーセンテージ値。

メソッドは、[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。の[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)クラスはチャート内の画像オブジェクトを表します。

次の例は、グラフに画像を追加する方法を示しています。この例では、グラフが含まれている前のデザイナー ファイル (**exp_piechart.xls**) を利用します。このファイルを使用して、チャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **チャートにチェックボックスを追加する**

Aspose.Cells を使用すると、次を使用してグラフ シートにチェックボックスを挿入できます。[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype)列挙。次の例は、グラフ シートにチェックボックスを追加する方法を示しています。

次の図は、出力ファイル内のチェックボックスを含むグラフ シートを示しています。

![todo:image_alt_text](controls-in-charts_1.jpg)

の[出力ファイル](101089316.xlsx)次のコード スニペットによって生成されたコードを参考のために添付します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **アドバンストトピック**
- [グラフにワードアートの透かしを追加する](/cells/ja/net/add-wordart-watermark-to-chart/)
