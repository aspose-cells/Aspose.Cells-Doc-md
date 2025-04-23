---
title: チャートシリーズのポイントのXおよびY値のタイプを検索する
description: Aspose.Cells for .NETを使用して、チャートシリーズのポイントのXおよびY値のタイプを判断する方法を学びます。当社のガイドでは、異なるデータ値のタイプを説明し、チャートでそれらをアクセスおよび操作する方法を示します。
keywords: Aspose.Cells for .NET、チャート、X値、Y値、データタイプ、アクセス、操作、チャートシリーズ。
type: docs
weight: 150
url: /ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**
時々、シリーズ内のチャートポイントのXおよびY値のタイプを知りたいことがあります。Aspose.Cellsでは、この目的のためにChartPoint.XValueTypeおよびChartPoint.YValueTypeプロパティを提供しています。これらのプロパティを効果的に使用するには、Chart.Calculate()メソッドを呼び出す必要があります。
## **チャートシリーズのX値とY値のタイプを検索する**
次のサンプルコードは、[サンプルExcelファイル](64716905.xlsx)を読み込み、最初のワークシート内の最初のチャートにアクセスします。その後、Chart.Calculate()メソッドを呼び出し、最初のチャートポイントのXおよびY値のタイプを検索し、それらをコンソールに出力します。参考のために、以下に示すコンソール出力をご覧ください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **コンソール出力**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
