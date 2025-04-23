---
title: 円グラフのカスタムスライスまたはセクターの色
description: Aspose.Cells for .NETを使用して、円グラフのスライスやセクターの色をカスタマイズする方法を学んでください。私たちのガイドでは、各スライス、セクター、またはレジョンに一意の色を割り当て、視覚的魅力とデータ表現を向上させる方法を示します。
keywords: Aspose.Cells for .NET、円グラフ、カスタムスライスの色、カスタムセクターの色、視覚的魅力、データ表現
type: docs
weight: 60
url: /ja/net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタムカラーを追加する方法について説明します。標準では、円グラフはMicrosoft Excelのデフォルトテンプレートを使用します。他の色を使用するには、チャート内の色を再定義してください。

{{% /alert %}}

円グラフの個々のスライスやセクターにカスタムカラーを設定するには：

1. [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクトの[**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint)にアクセスします。
1. [**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)プロパティを使用して、お好きな色を割り当てます。

この記事では次のような方法も説明しています:

- チャートのカテゴリデータ。
- セルにリンクされたチャートタイトル。
- チャートタイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)はパイチャートに特有のものではなく、すべての種類のチャートに使用することができます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
