---
title: チャートの計算後に軸ラベルを読み取る
description: グラフの計算後に Aspose.Cells for Java の軸ラベルを読み取る方法を学習します。私たちのガイドでは、軸ラベルにアクセスして取得する方法 (書式設定や配置など) を説明します。
keywords: Aspose.Cells for Java, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /ja/java/read-axis-labels-after-calculating-the-chart/
---
##  **考えられる使用シナリオ**

を使用して値を計算した後、グラフの軸ラベルを読み取ることができます。[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--)方法。をご利用ください。[**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--)この目的のために、軸ラベルのリストを返すメソッドを使用します。

##  **チャートの計算後に軸ラベルを読み取る**

をロードする次のサンプルコードを参照してください。[サンプル Excel ファイル](64716829.xlsx)そして、最初のワークシートのグラフのカテゴリ軸ラベルを読み取ります。次に、軸ラベルの値をコンソールに出力します。参考として、以下に示すサンプル コードのコンソール出力を参照してください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

##  **コンソール出力**

{{< highlight "java" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
