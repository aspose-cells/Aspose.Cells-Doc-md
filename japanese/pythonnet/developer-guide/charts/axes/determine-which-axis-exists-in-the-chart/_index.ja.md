---
title: チャートにどの軸が存在するかを判断する
description: Aspose.Cells for Python via .NETを使ったチャートの軸の存在の判断方法について学びます。ガイドでは、カテゴリー軸、値軸、二次軸など、さまざまな軸の識別とアクセス方法を理解できます。
keywords: Aspose.Cells for Python via .NET、チャート、軸、存在確認、カテゴリー、値、二次軸。
type: docs
weight: 140
url: /ja/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

時々、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。たとえば、彼はチャート内に二次値軸が存在するかどうかを知りたいとします。パイ、パイエクスプロード、パイピー、パイバー、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなど、ピザ、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなどのようないくつかのチャートには軸がありません。

Aspose.Cells for Python via .NETは、[**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis)メソッドを提供しており、チャートに特定の軸があるかどうかを判定できます。

{{% /alert %}}

次のサンプルコードは、[**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) を使用してサンプルチャートに一次および二次カテゴリおよび値軸があるかどうかを判断する方法を示しています。

## チャート内に存在する軸を判断するC#コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## サンプルコードによって生成されたコンソール出力

コードのコンソール出力は以下に表示され、一次カテゴリおよび値軸に対してtrue、二次カテゴリおよび値軸に対してfalseを表示します。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
