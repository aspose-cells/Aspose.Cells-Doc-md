---
title: チャート シリーズのポイントの X 値と Y 値のタイプを見つける
type: docs
weight: 150
url: /ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **考えられる使用シナリオ**
系列のチャート ポイントの X 値と Y 値のタイプを知りたい場合があります。 Aspose.Cells は、この目的で使用できる ChartPoint.XValueType および ChartPoint.YValueType プロパティを提供します。これらのプロパティを効果的に使用するには、Chart.Calculate() メソッドを呼び出す必要があることに注意してください。
## **チャート シリーズのポイントの X 値と Y 値のタイプを見つける**
次のサンプル コードは、[サンプル Excel ファイル](64716905.xlsx)最初のワークシート内の最初のグラフにアクセスします。次に、Chart.Calculate() メソッドを呼び出し、最初のチャート ポイントの X 値と Y 値のタイプを見つけて、コンソールに出力します。参考として、以下に示すコンソール出力を参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **コンソール出力**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
