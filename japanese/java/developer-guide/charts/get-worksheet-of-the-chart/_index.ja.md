---
title: チャートのワークシートを取得
type: docs
weight: 80
url: /ja/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートの参照からワークシートにアクセスしたい場合があります。Aspose.Cellsは、チャートを含むワークシートの参照を返す[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)プロパティを提供しています。

{{% /alert %}}

## 例

以下の例は、[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)プロパティを使用する方法を示しています。コードはまずワークシートの名前を印刷し、次にワークシート上の最初のチャートにアクセスし、その後再度[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)プロパティを使用してワークシート名を印刷します。

### チャートのワークシートにアクセスするためのJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### サンプルコードによって生成されたコンソール出力

以下は、サンプルコードの結果によって生成されるコンソール出力です。ご覧の通り、同じワークシート名が2回表示されます。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
