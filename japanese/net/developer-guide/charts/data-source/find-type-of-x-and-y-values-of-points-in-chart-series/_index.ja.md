---
title: チャート系列のポイントの X 値と Y 値のタイプを検索する
description: Aspose.Cells for .NET を使用して、チャート シリーズ ポイントの X 値と Y 値のタイプを決定する方法を学びます。ガイドでは、さまざまなタイプのデータ値について説明し、チャート内でデータ値にアクセスして操作する方法を示します。
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **考えられる使用シナリオ**
場合によっては、一連のチャート ポイントの X 値と Y 値のタイプを知りたいことがあります。 Aspose.Cells は、この目的に使用できる ChartPoint.XValueType プロパティと ChartPoint.YValueType プロパティを提供します。これらのプロパティを効果的に使用するには、事前に Chart.Calculate() メソッドを呼び出す必要があることに注意してください。
##  **チャート系列のポイントの X 値と Y 値のタイプを検索する**
次のサンプルコードは、[サンプル Excel ファイル](64716905.xlsx)そして、最初のワークシート内の最初のグラフにアクセスします。次に、Chart.Calculate() メソッドを呼び出し、最初のチャート ポイントの X 値と Y 値のタイプを見つけて、コンソールに出力します。参考として、以下に示すコンソール出力を参照してください。
##  **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **コンソール出力**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
