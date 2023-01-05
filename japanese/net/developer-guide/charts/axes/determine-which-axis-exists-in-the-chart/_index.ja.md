---
title: チャートに存在する軸を特定する
type: docs
weight: 140
url: /ja/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

場合によっては、特定の軸がチャートに存在するかどうかをユーザーが知る必要があります。たとえば、グラフ内に第 2 値軸が存在するかどうかを知りたいとします。 Pie、PieExploded、PiePie、PieBar、Pie3D、Pie3DExploded、Doughnut、DoughnutExploded などの一部のグラフには軸がありません。

Aspose.Cells提供[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)チャートに特定の軸があるかどうかを判断するメソッド。

{{% /alert %}}

次のサンプル コードは、[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)サンプル グラフにプライマリおよびセカンダリ カテゴリと値軸があるかどうかを判断します。

## C# グラフに存在する軸を決定するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## サンプル コードによって生成されたコンソール出力

コードのコンソール出力を以下に示します。これは、プライマリ カテゴリおよび値軸に対して true を表示し、セカンダリ カテゴリおよび値軸に対して false を表示します。

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
