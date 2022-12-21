---
title: チャート シリーズのポイントの X 値と Y 値のタイプを見つける
type: docs
weight: 110
url: /ja/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **考えられる使用シナリオ**

系列のチャート ポイントの X 値と Y 値のタイプを知りたい場合があります。 Aspose.Cells提供[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)と[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)この目的で使用できるプロパティ。お電話になりますのでご了承ください[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) メソッドを使用してから、これらのプロパティを効果的に使用してください。

## **チャート シリーズのポイントの X 値と Y 値のタイプを見つける**

次のサンプル コードは、[サンプル Excel ファイル](64716920.xlsx)最初のワークシート内の最初のグラフにアクセスします。次に、[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()メソッドを呼び出し、最初のチャート ポイントの X 値と Y 値のタイプを見つけて、コンソールに出力します。参考として、以下に示すコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
