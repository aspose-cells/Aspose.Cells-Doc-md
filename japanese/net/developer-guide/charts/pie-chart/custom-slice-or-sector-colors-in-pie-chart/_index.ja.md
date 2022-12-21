---
title: 円グラフのカスタム スライスまたはセクターの色
type: docs
weight: 60
url: /ja/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタム カラーを追加する方法について説明します。デフォルトでは、円グラフは Microsoft Excel デフォルト テンプレートを使用します。他の色を使用するには、チャートで色を再定義します。

{{% /alert %}}

円グラフの個々のスライスまたはセクターにカスタム カラーを設定するには:

1. アクセス[**シリーズ**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクトの[**チャートポイント**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. を使用して、選択した色を割り当てます。[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)財産。

この記事では、次の方法についても説明します。

- グラフのカテゴリ データ。
- セルにリンクされたチャート タイトル。
- グラフ タイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)円グラフに固有のものではありませんが、すべての種類のグラフに使用できます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
