---
title: チャートに存在する軸を特定する
type: docs
weight: 130
url: /ja/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

場合によっては、特定の軸がチャートに存在するかどうかをユーザーが知る必要があります。たとえば、グラフ内に第 2 値軸が存在するかどうかを知りたいとします。 Pie、PieExploded、PiePie、PieBar、Pie3D、Pie3DExploded、Doughnut、DoughnutExploded などの一部のグラフには軸がありません。

Aspose.Cells提供[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) メソッドを使用して、チャートに特定の軸があるかどうかを判断します。

{{% /alert %}}

## チャートに存在する軸を特定する

次のスクリーンショットは、プライマリ カテゴリと値軸のみを含むグラフを示しています。セカンダリ カテゴリと値軸はありません。

![todo:画像_代替_文章](determine-which-axis-exists-in-the-chart_1.png)

次のサンプル コードは、[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)を使用して、サンプル グラフにプライマリおよびセカンダリ カテゴリと値軸があるかどうかを判断します。コードのコンソール出力を以下に示します。これは、プライマリ カテゴリおよび値軸に対して true を表示し、セカンダリ カテゴリおよび値軸に対して false を表示します。

### Java チャートに存在する軸を決定するコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### サンプル コードによって生成されたコンソール出力

上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
