---
title: 円グラフのカスタムスライスまたはセクターの色
description: Aspose.Cells for Python via .NETを使って、円グラフにおけるスライスやセクターの色のカスタマイズ方法を学びましょう。ガイドでは、各スライスやセクターにユニークな色を割り当て、視覚的魅力とデータの表現力を向上させる方法を示します。
keywords: Aspose.Cells for Python via .NET、円グラフ、カスタムスライスカラー、カスタムセクターカラー、視覚的魅力、データ表現。
type: docs
weight: 60
url: /ja/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタムカラーを追加する方法について説明します。標準では、円グラフはMicrosoft Excelのデフォルトテンプレートを使用します。他の色を使用するには、チャート内の色を再定義してください。

{{% /alert %}}

円グラフの個々のスライスやセクターにカスタムカラーを設定するには：

1. [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)オブジェクトの[**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint)にアクセスします。
1. [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color)プロパティを使用して、お好きな色を割り当てます。

この記事では次のような方法も説明しています:

- チャートのカテゴリデータ。
- セルにリンクされたチャートタイトル。
- チャートタイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color)はパイチャートに特有のものではなく、すべての種類のチャートに使用することができます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
