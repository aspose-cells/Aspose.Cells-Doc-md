---
title: 引き出し線付きの円グラフの作成
description: Aspose.Cells for .NET Excel で引出線付きの円グラフを作成するために Aspose.Cells for .NET を使用する方法を説明します。このガイドでは、データ ポイントを凡例に接続する引出線を追加し、グラフ全体の明瞭さを高める方法を説明します。
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

この記事では、Aspose.Cells for .NET API を使用して、引出し線付きの円グラフを最初から作成する方法について説明します。 Excel では、[引出し線を表示] オプションがデフォルトで設定されているため、Excel で円グラフを作成すると引出し線が表示されます。ただし、Aspose.Cells API を使用して同様のチャートを作成する場合、明示的に設定する必要があります。[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)財産。

{{% /alert %}}

 Aspose.Cells for .NET API を使用して引出線付きの円グラフを作成する方法を示すために、まず新しい[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)系列データ ソースとして機能するデータを入力します。データが整ったら、[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)タイプの[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)チャートのコレクションにアクセスし、そのさまざまな側面を設定して、目的のチャート ビューを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

これまで、円グラフを作成し、そのさまざまな側面を設定してきました。次に、チャートの引出線をオンにします。引出線を表示するには、データ ラベルを少し移動する必要があることに注意してください。

次のコードでは、引出線をオンにしてグラフを更新し、データ ラベルの位置を計算してそれに応じてデータ ラベルを移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最後に、次のコードはグラフを画像形式で保存し、ワークブックを XLSX 形式で保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**結果の円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **アドバンストトピック**
- [円グラフのカスタム スライスまたはセクターの色](/cells/ja/net/custom-slice-or-sector-colors-in-pie-chart/)
- [データ ポイントが円グラフまたは円グラフの 2 番目の円または棒にあるかどうかを確認する](/cells/ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/net/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/net/customizing-charts/)
- [グラフのデータの書式設定](/cells/ja/net/data-formatting-in-charts/)
- [チャートの外観の設定](/cells/ja/net/setting-chart-appearance/)

