---
title: Go言語とC++を使ったチャートのトレンドラインの式テキスト取得
linktitle: トレンドライン
description: Microsoft Excelで作成されたチャートのトレンドラインの方程式テキストを取得するためにAspose.Cells for C++を使用する方法を学びます。当ガイドは、トレンドラインの方程式にアクセスし抽出して、さらなる分析や表示に役立てる方法を示します。
keywords: Aspose.Cells for C++、チャートトレンドライン、方程式テキスト、Microsoft Excel、データ分析、表示。
type: docs
weight: 110
url: /ja/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、チャートのトレンドラインの方程式テキストを取得できます。Aspose.Cellsは、チャートのトレンドラインの方程式テキストを返す[**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/)プロパティを提供しています。このプロパティを利用するには、まず[**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)メソッドを呼び出す必要があります。

{{% /alert %}}

以下のスクリーンショットは、トレンドライン付きのチャートと、その式テキストが赤色で表示されたものです。この式テキストは、以下のサンプルコードの [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) プロパティを使用して取得します。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++コードでチャートトレンドラインの方程式テキストを取得する方法

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
