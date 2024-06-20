---
title: リーダーライン付きの円グラフの作成
description: Microsoft ExcelでAspose.Cells for .NETを使用してリーダーライン付きの円グラフを作成する方法を学びます。当ガイドでは、データポイントを凡例に接続し、全体のクラリティを高めるためにリーダーラインを追加する方法を示します。
keywords: Aspose.Cells for .NET、円グラフ、リーダーライン、Microsoft Excel、データの視覚化、グラフのカスタマイズ
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for .NET APIを使用してゼロからリーダーライン付きの円グラフを作成する方法について説明します。Excelでは、「リーダーラインを表示」オプションがデフォルトで設定されているため、Excelで円グラフを作成するとリーダーラインが表示されます。ただし、Aspose.CellsのAPIを使用して同様のチャートを作成する場合は、明示的に[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)プロパティを設定する必要があります。

{{% /alert %}}

リーダーライン付き円グラフを作成するためにAspose.Cells for .NET APIの使用を示すために、まず新しい [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を作成し、シリーズデータソースとして機能するデータを入力します。データが整ったら、グラフのコレクションにタイプ [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)の[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)を追加し、所望のグラフビューを得るために異なる側面を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

これまでに円グラフを作成し、異なる側面を設定しました。これからは、チャートのリーダーラインをオンにします。リーダーラインを表示するには、データラベルを少し移動する必要があります。

次のコードは、リーダーラインをオンにし、チャートを更新し、それからデータラベルの位置を計算して適切に移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最後に、次のコードでチャートを画像形式で保存し、ワークブックをXLSX形式で保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**作成された円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高度なトピック**
- [円グラフでのカスタムスライスまたはセクターの色](/cells/ja/net/custom-slice-or-sector-colors-in-pie-chart/)
- [パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける](/cells/ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/net/creating-charts/)
- [グラフのカスタマイズ](/cells/ja/net/customizing-charts/)
- [グラフのデータ整形](/cells/ja/net/data-formatting-in-charts/)
- [グラフの外観設定](/cells/ja/net/setting-chart-appearance/)

