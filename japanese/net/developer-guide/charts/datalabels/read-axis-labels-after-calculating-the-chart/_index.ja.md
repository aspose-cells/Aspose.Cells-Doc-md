---
title: チャートの計算後に軸ラベルを読む
description: Aspose.Cells for .NETの計算後に軸ラベルを読む方法を学びます。当社のガイドでは、軸ラベルにアクセスして取得する方法、それらのフォーマットおよび配置を含む軸ラベルを表示する方法を示します。
keywords: Aspose.Cells for .NET、チャート、軸ラベル、計算、読み取り、アクセス、取得、フォーマット、配置。
type: docs
weight: 90
url: /ja/net/read-axis-labels-after-calculating-the-chart/
---

## **可能な使用シナリオ**

軸ラベルの値を計算した後に、[**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)メソッドを使用してチャートの軸ラベルを読み取ることができます。この目的のためには、リストは[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/)メソッドを使用してください。

## **チャートを計算した後に軸ラベルを読み取る**

次のサンプルコードは、[サンプルExcelファイル](ReadAxisLabels.xlsx)を読み込み、最初のワークシートのチャートのカテゴリ軸ラベルを読み取ります。その後、軸ラベルの値をコンソールに出力します。参考のために、以下に示すサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

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
