---
title: GolangからC++を使ってチャートの軸ラベルを計算後に読む
linktitle: チャートの計算後に軸ラベルを読む
description: チャートを計算した後にAspose.Cells for C++で軸ラベルを読む方法を学びます。フォーマットや位置調整を含め、軸ラベルにアクセスして取得する方法を示します。
keywords: Aspose.Cells for C++、チャート、軸ラベル、計算、読み取り、アクセス、取得、フォーマット、位置調整。
type: docs
weight: 90
url: /ja/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **可能な使用シナリオ**

軸ラベルの値を計算した後に、[**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/)メソッドを使用してチャートの軸ラベルを読み取ることができます。この目的のためには、リストは[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/)メソッドを使用してください。

## **チャートを計算した後に軸ラベルを読み取る**

次のサンプルコードは、[サンプルExcelファイル](ReadAxisLabels.xlsx)を読み込み、最初のワークシートのチャートのカテゴリ軸ラベルを読み取ります。その後、軸ラベルの値をコンソールに出力します。参考のために、以下に示すサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **コンソール出力**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
