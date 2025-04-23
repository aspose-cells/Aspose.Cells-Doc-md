---
title: チャートにどの軸が存在するかを判断する
description: Aspose.Cells for .NETを使用して作成したチャートに存在するさまざまな軸、カテゴリ、値、セカンダリの軸を識別してアクセスする方法を理解するためのガイドを学びます。
keywords: Aspose.Cells for .NET、チャート、軸、存在、カテゴリ、値、セカンダリ。
type: docs
weight: 140
url: /ja/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

時々、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。たとえば、彼はチャート内に二次値軸が存在するかどうかを知りたいとします。パイ、パイエクスプロード、パイピー、パイバー、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなど、ピザ、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなどのようないくつかのチャートには軸がありません。

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)メソッドを提供します。

{{% /alert %}}

次のサンプルコードは、[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) を使用してサンプルチャートに一次および二次カテゴリおよび値軸があるかどうかを判断する方法を示しています。

## チャート内に存在する軸を判断するC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## サンプルコードによって生成されたコンソール出力

コードのコンソール出力は以下に表示され、一次カテゴリおよび値軸に対してtrue、二次カテゴリおよび値軸に対してfalseを表示します。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
