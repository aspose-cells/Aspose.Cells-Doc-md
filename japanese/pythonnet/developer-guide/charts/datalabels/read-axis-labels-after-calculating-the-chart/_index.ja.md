---
title: チャートの計算後に軸ラベルを読む
description: Aspose.Cells for Python via .NETでチャートの軸ラベルを計算した後に読み取る方法を学びます。ガイドでは、軸ラベルのアクセスと取得方法、その書式設定や位置調整について解説します。
keywords: Aspose.Cells for Python via .NET、グラフ、軸ラベル、計算、読み取り、アクセス、取得、書式設定、位置付け。
type: docs
weight: 90
url: /ja/python-net/read-axis-labels-after-calculating-the-chart/
---

## **可能な使用シナリオ**

軸ラベルの値を計算した後に、[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/)メソッドを使用してチャートの軸ラベルを読み取ることができます。この目的のためには、リストは[**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts)メソッドを使用してください。

## **チャートを計算した後に軸ラベルを読み取る**

次のサンプルコードは、[サンプルExcelファイル](ReadAxisLabels.xlsx)を読み込み、最初のワークシートのチャートのカテゴリ軸ラベルを読み取ります。その後、軸ラベルの値をコンソールに出力します。参考のために、以下に示すサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **コンソール出力**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
