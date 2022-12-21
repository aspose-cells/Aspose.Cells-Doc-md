---
title: ポジション サイズとデザイナー チャートの操作
type: docs
weight: 45
url: /ja/net/manipulate-position-size-and-designer-chart/
---
## **チャートの位置とサイズ**
ワークシート内の新規または既存のグラフの位置またはサイズを変更したい場合があります。 Aspose.Cells は[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)これを達成するためのプロパティ。そのサブプロパティを使用して、チャートのサイズを変更できます**身長**と**幅**または新しいもので再配置します**X** と**Y** 座標。
### **チャートの位置とサイズの制御**
グラフの位置 (X、Y 座標) またはサイズ (高さ、幅) を変更するには、次のプロパティを使用します。

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

次の例では、上記の API の使用法を説明します。最初のワークシートにグラフを含む既存のワークブックを読み込みます。次に、Aspose.Cells を使用してチャートのサイズと位置を変更します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **デザイナー チャートの操作**
デザイナー テンプレート ファイルでグラフを操作または変更する必要がある場合があります。 Aspose.Cells は、デザイナー チャートのコンテンツと要素の操作を完全にサポートします。データ、グラフの内容、背景画像、および書式設定を正確に保持できます。
### **テンプレート ファイルでデザイナー チャートを操作する**
テンプレート ファイルでデザイナー チャートを操作するには、チャート関連の API を使用します。たとえば、Worksheet.Charts プロパティを使用して、テンプレート ファイル内の既存のチャート コレクションを取得できます。
#### **チャートの作成**
次の例は、ピラミッド チャートを作成する方法を示しています。このチャートは後で操作します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **チャートの操作**
次の例は、既存のグラフを操作する方法を示しています。この例では、上で作成したチャートを変更します。生成された出力では、1 つのデータ ポイントの日付ラベルが「英国、30K」に設定されていることに注意してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Designer テンプレートでの折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータ シリーズを追加し、線の色を変更します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

