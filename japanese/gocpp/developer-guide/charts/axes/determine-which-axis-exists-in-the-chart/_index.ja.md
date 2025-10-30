---
title: Golang経由でチャートの軸が存在するかどうかを判定
description: Aspose.Cells for C++で作成されたチャートにどの軸が存在するかを判定する方法を学びます。ガイドは、カテゴリー軸、値軸、セカンダリ軸などの異なる軸を識別してアクセスする方法を説明します。
keywords: Aspose.Cells for C++、チャート、軸、存在、カテゴリー、値、セカンダリ。
type: docs
weight: 140
url: /ja/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

時々、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。たとえば、彼はチャート内に二次値軸が存在するかどうかを知りたいとします。パイ、パイエクスプロード、パイピー、パイバー、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなど、ピザ、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなどのようないくつかのチャートには軸がありません。

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/)メソッドを提供します。

{{% /alert %}}

次のサンプルコードは、[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/)を使用してサンプルチャートにプライマリおよびセカンダリのカテゴリ軸と値軸が存在するかどうかを判断する例です。

## C++コード：チャートに軸が存在するか判定する方法

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## サンプルコードによって生成されたコンソール出力

コードのコンソール出力は以下に表示され、一次カテゴリおよび値軸に対してtrue、二次カテゴリおよび値軸に対してfalseを表示します。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
