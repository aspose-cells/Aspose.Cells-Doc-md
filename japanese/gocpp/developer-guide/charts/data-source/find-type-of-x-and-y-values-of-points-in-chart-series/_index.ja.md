---
title: GolangからC++を使ってチャートシリーズのポイントのX値とY値のタイプを見つける
linktitle: チャートシリーズのポイントのXおよびY値のタイプを検索する
description: Aspose.Cells for C++を使用して、チャートシリーズポイントのX値とY値の種類を判定する方法を学びます。ガイドでは、さまざまなデータ値のタイプと、それらにアクセスし操作する方法を説明します。
keywords: Aspose.Cells for C++, チャート作成, X値, Y値, データタイプ, アクセス, 操作, チャート系列。
type: docs
weight: 150
url: /ja/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**
時には、シリーズ内のチャートポイントのX値とY値のタイプを知りたい場合があります。Aspose.Cellsは `ChartPoint::get_XValueType` と `ChartPoint::get_YValueType` メソッドを提供しており、これらを利用できます。ただし、これらのプロパティを使用する前に `Chart::Calculate()` を呼び出す必要がある点に注意してください。

## **チャートシリーズのX値とY値のタイプを検索する**
次のサンプルコードは、[サンプルExcelファイル](64716905.xlsx)をロードし、最初のワークシートの最初のチャートにアクセスします。次に、`Chart::Calculate()` を呼び出し、最初のチャートポイントのX値とY値の種類を判定してコンソールに出力します。参考のため、以下の出力例を参照してください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **コンソール出力**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
