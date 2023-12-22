---
title: チャートにどの軸が存在するかを決定する
description: Aspose.Cells for .NET を使用して作成されたグラフにどの軸が存在するかを確認する方法について説明します。このガイドは、カテゴリ、値、副軸など、グラフ内のさまざまな軸を識別してアクセスする方法を理解するのに役立ちます。
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /ja/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

場合によっては、ユーザーはチャートに特定の軸が存在するかどうかを知りたいことがあります。たとえば、グラフ内に 2 番目の値軸が存在するかどうかを知りたいと考えています。 Pie、PieExploded、PiePie、PieBar、Pie3D、Pie3DExploded、Doughnut、DoughnutExploded などの一部のグラフには軸がありません。

 Aspose.Cellsが提供します[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)チャートに特定の軸があるかどうかを判断するメソッド。

{{% /alert %}}

次のサンプル コードは、[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)サンプル グラフにプライマリ カテゴリとセカンダリ カテゴリおよび値軸があるかどうかを確認します。

##  C# グラフにどの軸が存在するかを決定するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## サンプルコードによって生成されたコンソール出力

コードのコンソール出力を以下に示します。この出力では、プライマリ カテゴリと値軸には true、セカンダリ カテゴリと値軸には false が表示されます。

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
