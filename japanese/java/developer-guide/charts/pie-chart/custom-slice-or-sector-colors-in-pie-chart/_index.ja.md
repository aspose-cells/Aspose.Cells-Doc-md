---
title: 円グラフのカスタムスライスまたはセクターの色
type: docs
weight: 30
url: /ja/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタムカラーを追加する方法について説明します。デフォルトでは、円グラフはMicrosoft Excelのデフォルトテンプレートを使用します。他の色を使用するには、チャート内の色を再定義することが可能です。

{{% /alert %}}

円グラフの個々のスライスまたはセクターにカスタムカラーを設定するには:

1. [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトの[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)にアクセスします。
1. [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)メソッドを使用して任意の色を割り当てます。

この記事では次の方法も説明されています:

- チャートのカテゴリデータ。
- セルにリンクされたチャートタイトル。
- チャートタイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)はパイチャートに特有のものではありませんが、すべての種類のチャートに使用できます。

{{% /alert %}}

パイチャートのカスタムスライスの色

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
