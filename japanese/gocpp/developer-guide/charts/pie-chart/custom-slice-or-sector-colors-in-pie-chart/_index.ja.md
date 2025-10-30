---
title: Golangを使用したC++によるパイチャートのカスタムスライスまたはセクターの色
linktitle: 円グラフのカスタムスライスまたはセクターの色
description: Aspose.Cells for C++を使って、円グラフ内のスライスやセクターの色をカスタマイズする方法を学びましょう。各スライスやセクターにユニークな色を割り当てて、視覚的魅力とデータ表現を向上させることを示します。
keywords: Aspose.Cells for C++、円グラフ、スライスのカスタム色、セクターのカスタム色、視覚的魅力、データ表現。
type: docs
weight: 60
url: /ja/go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

この記事では、円グラフのスライス/セクターにカスタムカラーを追加する方法について説明します。標準では、円グラフはMicrosoft Excelのデフォルトテンプレートを使用します。他の色を使用するには、チャート内の色を再定義してください。

{{% /alert %}}

円グラフの個々のスライスやセクターにカスタムカラーを設定するには：

1. [**Series**](https://reference.aspose.com/cells/go-cpp/series/)オブジェクトの[**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/)にアクセスします。
1. [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/)プロパティを使用して、お好きな色を割り当てます。

この記事では次のような方法も説明しています:

- チャートのカテゴリデータ。
- セルにリンクされたチャートタイトル。
- チャートタイトルのフォント設定。
- 凡例の位置。

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/)はパイチャートに特有のものではなく、すべての種類のチャートに使用することができます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}
