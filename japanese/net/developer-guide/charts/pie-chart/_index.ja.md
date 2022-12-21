---
title: 引出線付き円グラフの作成
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

この記事では、Aspose.Cells for .NET API を使用して、引出線付きの円グラフを最初から作成する方法について説明します。Excel では、[引出線を表示] オプションがデフォルトで設定されているため、Excel で円グラフを作成すると、引出線が表示されます。ただし、Aspose.Cells API を使用して同様のグラフを作成する場合は、明示的に[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)財産。

{{% /alert %}}

Aspose.Cells for .NET API を使用して引出線付きの円グラフを作成する方法を示すために、最初に新しい[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)系列データ ソースとして機能するデータを入力します。データが整ったら、[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)タイプの[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)チャートのコレクションに追加し、そのさまざまな側面を設定して、目的のチャート ビューを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

ここまでで、円グラフを作成し、さまざまな側面を設定しました。次に、チャートのリーダー ラインをオンにします。リーダー ラインを表示するには、データ ラベルを少し移動する必要があることに注意してください。

次のコードは、リーダー ラインをオンにし、グラフを更新してから、データ ラベルの位置を計算して、それに応じて移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最後に、次のコードは、グラフを画像形式で保存し、ワークブックを XLSX 形式で保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**結果の円グラフ**|
|:- |
|![todo:画像_代替_文章](creating-pie-chart-with-leader-lines_1.png)|

## **先行トピック**
- [円グラフのカスタム スライスまたはセクターの色](/cells/ja/net/custom-slice-or-sector-colors-in-pie-chart/)
- [円グラフまたは円グラフの棒グラフの 2 番目の円または棒にデータ ポイントがあるかどうかを調べる](/cells/ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/net/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/net/customizing-charts/)
- [チャートでのデータの書式設定](/cells/ja/net/data-formatting-in-charts/)
- [チャートの外観の設定](/cells/ja/net/setting-chart-appearance/)

