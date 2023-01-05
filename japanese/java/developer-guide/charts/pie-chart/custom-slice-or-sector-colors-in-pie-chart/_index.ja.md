---
title: 円グラフのカスタム スライスまたはセクターの色
type: docs
weight: 30
url: /ja/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタム カラーを追加する方法について説明します。デフォルトでは、円グラフは Microsoft Excel デフォルト テンプレートを使用します。他の色を使用するには、チャートの色を再定義することができます。

{{% /alert %}}

円グラフの個々のスライスまたはセクターのカスタム カラーを設定するには:

1. アクセス[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトの[**チャートポイント**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. を使用して、選択した色を割り当てます。[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)方法。

この記事では、次の設定方法についても説明します。

- グラフのカテゴリ データ。
- セルにリンクされたチャート タイトル。
- グラフ タイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)円グラフに固有のものではありませんが、すべての種類のグラフに使用できます。

{{% /alert %}}

**円グラフのカスタム スライスの色**

![todo:画像_代替_文章](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
