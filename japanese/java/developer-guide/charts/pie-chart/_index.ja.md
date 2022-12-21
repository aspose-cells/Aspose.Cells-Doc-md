---
title: 引出線付き円グラフの作成
linktitle: 円グラフ
type: docs
weight: 170
url: /ja/java/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

この記事では、Aspose.Cells for Java API を使用して、引出線付きの円グラフを最初から作成する方法について説明します。Excel では、[引出線を表示] オプションがデフォルトで設定されているため、Excel で円グラフを作成すると、引出線が表示されます。ただし、Aspose.Cells API を使用して同様のグラフを作成する場合は、明示的に[**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines)財産。

{{% /alert %}}

## **引出線付き円グラフの作成**

 Aspose.Cells for Java API を使用して引出線付きの円グラフを作成する方法を示すために、最初に新しい円グラフを作成します。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)系列データ ソースとして機能するデータを入力します。データが整ったら、[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)タイプの[**パイ**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE)チャートのコレクションに追加し、さまざまな側面を設定して、目的のチャート ビューを取得します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**結果の円グラフ**

![todo:画像_代替_文章](creating-pie-chart-with-leader-lines_1.png)

## 関連記事

- [グラフの作成とカスタマイズ](/cells/ja/java/creating-and-customizing-charts/)
- [チャートの書式設定](/cells/ja/java/chart-formatting/)
