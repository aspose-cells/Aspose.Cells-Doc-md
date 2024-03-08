---
title: チャートの計算後に軸ラベルを読み取る
description: グラフの計算後に Aspose.Cells for .NET の軸ラベルを読み取る方法を学習します。私たちのガイドでは、軸ラベルにアクセスして取得する方法 (書式設定や配置など) を説明します。
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /ja/net/read-axis-labels-after-calculating-the-chart/
---
##  **考えられる使用シナリオ**

を使用して値を計算した後、グラフの軸ラベルを読み取ることができます。[**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)方法。をご利用ください。[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/)この目的のために、軸ラベルのリストを返すメソッドを使用します。

##  **チャートの計算後に軸ラベルを読み取る**

をロードする次のサンプルコードを参照してください。[サンプル Excel ファイル](ReadAxisLabels.xlsx)そして、最初のワークシートのグラフのカテゴリ軸ラベルを読み取ります。次に、軸ラベルの値をコンソールに出力します。参考として、以下に示すサンプル コードのコンソール出力を参照してください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **コンソール出力**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
