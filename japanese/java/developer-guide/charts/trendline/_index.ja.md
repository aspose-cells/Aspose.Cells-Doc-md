---
title: チャート トレンドラインの数式テキストを取得する
linktitle: トレンドライン
type: docs
weight: 90
url: /ja/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、チャート トレンドラインの数式テキストを取得できます。Aspose.Cells は提供します[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)チャート トレンドラインの数式テキストを返すプロパティ。このプロパティを利用するには、最初に呼び出す必要があります[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()） 方法。

{{% /alert %}}

## **例**

次のスクリーンショットは、トレンドラインを含むチャートを示しており、その数式テキストは赤色で表示されています。このテキストを取得するには、[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)次のサンプル コードのプロパティ。

![todo:画像_代替_文章](get-equation-text-of-chart-trendline_1.png)

### Java チャート トレンドラインの数式テキストを取得するコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### サンプル コードによって生成される出力

これは、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
