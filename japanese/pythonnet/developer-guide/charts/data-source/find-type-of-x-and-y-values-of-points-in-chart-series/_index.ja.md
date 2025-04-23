---
title: チャートシリーズのポイントのXおよびY値のタイプを検索する
description: Aspose.Cells for Python via .NET でチャートシリーズのX値とY値のタイプを識別する方法を学びましょう。ガイドでは、さまざまなデータ値の種類とそれらにアクセスして操作する方法を説明します。
keywords: Aspose.Cells for Python via .NET、グラフ作成、X値、Y値、データ型、アクセス、操作、チャートシリーズ。
type: docs
weight: 150
url: /ja/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**
時には、シリーズのチャートポイントのX値とY値のタイプを知りたい場合があります。Aspose.Cells for Python via .NET は [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) と [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) プロパティを提供し、この目的に使用できます。ただし、これらのプロパティを効果的に使用する前に [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) メソッド呼び出しが必要です。

## **チャートシリーズのX値とY値のタイプを検索する**
以下のサンプルコードは、[サンプルExcelファイル](64716905.xlsx) をロードし、最初のワークシートの最初のグラフにアクセスします。その後、[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) メソッドを呼び出し、最初のチャートポイントのX値とY値のタイプを判定し、コンソールに表示します。下のコンソール出力例を参照してください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **コンソール出力**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
