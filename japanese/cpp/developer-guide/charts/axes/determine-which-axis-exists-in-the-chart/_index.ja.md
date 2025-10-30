---
title: C++を使用してチャートに存在する軸を判定する方法
description: Aspose.Cells for C++で作成されたチャートにどの軸が存在するかを判定する方法を学びます。ガイドは、カテゴリー軸、値軸、セカンダリ軸などの異なる軸を識別してアクセスする方法を説明します。
keywords: Aspose.Cells for C++、チャート、軸、存在、カテゴリー、値、セカンダリ。
type: docs
weight: 140
url: /ja/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

時々、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。たとえば、彼はチャート内に二次値軸が存在するかどうかを知りたいとします。パイ、パイエクスプロード、パイピー、パイバー、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなど、ピザ、パイ3D、パイ3Dエクスプロード、ドーナツ、ドーナツエクスプロードなどのようないくつかのチャートには軸がありません。

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/)メソッドを提供します。

{{% /alert %}}

次のサンプルコードは、[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/)を使用してサンプルチャートにプライマリおよびセカンダリのカテゴリ軸と値軸が存在するかどうかを判断する例です。

## C++コード：チャートに軸が存在するか判定する方法

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## サンプルコードによって生成されたコンソール出力

コードのコンソール出力は以下に表示され、一次カテゴリおよび値軸に対してtrue、二次カテゴリおよび値軸に対してfalseを表示します。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
