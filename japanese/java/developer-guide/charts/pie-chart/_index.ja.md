---
title: リーダーライン付きの円グラフの作成
linktitle: 円グラフ
type: docs
weight: 170
url: /ja/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for Java APIを使用してリーダーライン付きの円グラフをゼロから作成する方法について説明します。Excelでは、「リーダーラインを表示」オプションがデフォルトで設定されているため、Excelで円グラフを作成するとリーダーラインが表示されます。ただし、Aspose.Cells APIを使用して同様のチャートを作成する場合は、明示的に[**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines)プロパティを設定する必要があります。

{{% /alert %}}

## **リーダーライン付き円グラフの作成**

リーダーライン付きの円グラフを作成するためにAspose.Cells for Java APIの使用を実証するために、まず新しい[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)を作成し、シリーズのデータソースとして機能するデータを入力します。データが用意されたら、チャートのビューを取得するために、[**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE)のタイプの[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)をチャートのコレクションに追加し、それぞれの様々な側面を設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**作成される円グラフ**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## 関連記事

- [グラフの作成とカスタマイズ](/cells/ja/java/creating-and-customizing-charts/)
- [グラフの書式設定](/cells/ja/java/chart-formatting/)
