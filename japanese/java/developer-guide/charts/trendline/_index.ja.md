---
title: チャートのトレンドラインの方程式テキストを取得する
linktitle: トレンドライン
type: docs
weight: 90
url: /ja/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、チャートのトレンドラインの方程式テキストを取得できます。Aspose.Cellsは、チャートのトレンドラインの方程式テキストを返す[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)プロパティを提供しています。このプロパティを利用するには、まず[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--)メソッドを呼び出す必要があります。

{{% /alert %}}

## **例**

以下のスクリーンショットは、トレンドライン付きのチャートとその方程式テキストが赤色で表示されています。以下のサンプルコードでは、[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)プロパティを使用してこのテキストを取得します。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### チャートトレンドラインの方程式テキストを取得するためのJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### サンプルコードによって生成される出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
