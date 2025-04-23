---
title: チャートにどの軸が存在するかを判断する
type: docs
weight: 130
url: /ja/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

ユーザーは、特定の軸がチャートに存在するかどうかを知る必要がある場合があります。たとえば、彼は、チャート内に2番目の値軸が存在するかどうかを知りたいと思っているかもしれません。円グラフ、パイエクスプロード、パイパイ、パイバー、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなどの一部のチャートには軸がありません。

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-)メソッドを提供します。

{{% /alert %}}

## チャートに存在する軸を判断する

次のスクリーンショットは、プライマリカテゴリと値軸のみを持つチャートを示しています。セカンダリカテゴリと値軸はありません。

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

次のサンプルコードは、[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-)の使用を示しています。サンプルチャートにプライマリおよびセカンダリカテゴリと値軸があるかどうかを判断します。コードのコンソール出力は、プライマリカテゴリと値軸に対してtrue、セカンダリカテゴリと値軸に対してfalseを表示します。

### チャート内に存在する軸を判断するためのJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### サンプルコードによって生成されたコンソール出力

上記サンプルコードのコンソール出力はこちらです。

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
