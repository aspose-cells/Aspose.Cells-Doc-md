---
title: ポジションサイズとデザイナーチャートの操作
description: Aspose.Cells for .NET Excel で位置、サイズ、デザイナー チャートを効果的に操作するための Aspose.Cells の使用方法を学びます。私たちのガイドでは、レイアウトと視覚化を改善するためにこれらのプロパティを調整する方法を説明します。
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /ja/net/manipulate-position-size-and-designer-chart/
---
##  **チャートの位置とサイズ**
場合によっては、ワークシート内の新規または既存のグラフの位置やサイズを変更したい場合があります。 Aspose.Cells は、[チャート.チャートオブジェクト](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)これを達成するためのプロパティ。そのサブプロパティを使用して、新しい値でグラフのサイズを変更できます。**身長**そして**幅**または新しいもので再配置します**X** と **Y**コーディネート。
###  **チャートの位置とサイズの制御**
グラフの位置 (X、Y 座標) またはサイズ (高さ、幅) を変更するには、次のプロパティを使用します。

1. [チャート.チャートオブジェクト.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [チャート.チャートオブジェクト.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [チャート.チャートオブジェクト.高さ](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

次の例では、上記の API の使用法を説明します。最初のワークシートにグラフを含む既存のワークブックを読み込みます。次に、Aspose.Cells を使用してグラフのサイズと位置を変更します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **デザイナー チャートの操作**
デザイナー テンプレート ファイル内のグラフを操作または変更する必要がある場合があります。 Aspose.Cells は、デザイナー チャートのコンテンツと要素の操作を完全にサポートしています。データ、グラフの内容、背景画像、書式設定を正確に保存できます。
###  **テンプレート ファイルでのデザイナー チャートの操作**
テンプレート ファイル内のデザイナー グラフを操作するには、API に関連するグラフを使用します。たとえば、Worksheet.Charts プロパティを使用して、テンプレート ファイル内の既存のグラフ コレクションを取得できます。
####  **チャートの作成**
次の例は、ピラミッド チャートを作成する方法を示しています。このチャートは後で操作します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **チャートの操作**
次の例は、既存のチャートを操作する方法を示しています。この例では、上で作成したチャートを変更します。生成された出力では、1 つのデータ ポイントの日付ラベルが「イギリス、30K」に設定されていることに注意してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **デザイナー テンプレートでの折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のグラフにいくつかのデータ系列を追加し、線の色を変更します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

