---
title: チャートシリーズのポイントのXおよびY値のタイプを検索する
type: docs
weight: 110
url: /ja/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**

時々、チャートのシリーズ内のチャートポイントのXおよびY値のタイプを知りたい場合があります。Aspose.Cellsは、この目的に使用できる[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)および[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)プロパティを提供します。これらのプロパティを効果的に使用するには、[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--)メソッドを呼び出す必要があります。

## **チャートシリーズのX値とY値のタイプを検索する**

以下のサンプルコードでは、[sample Excel file](64716920.xlsx)を読み込み、最初のワークシート内の最初のチャートにアクセスします。その後、[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--)メソッドを呼び出して、最初のチャートポイントのXおよびY値のタイプを見つけ、それをコンソールに出力します。参考のために、以下に示すコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **コンソール出力**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
