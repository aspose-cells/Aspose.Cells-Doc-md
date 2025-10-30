---
title: C++でチャートトレンドラインの方程式テキストを取得する方法
linktitle: トレンドライン
description: Microsoft Excelで作成されたチャートのトレンドラインの方程式テキストを取得するためにAspose.Cells for C++を使用する方法を学びます。当ガイドは、トレンドラインの方程式にアクセスし抽出して、さらなる分析や表示に役立てる方法を示します。
keywords: Aspose.Cells for C++、チャートトレンドライン、方程式テキスト、Microsoft Excel、データ分析、表示。
type: docs
weight: 110
url: /ja/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、チャートのトレンドラインの方程式テキストを取得できます。Aspose.Cellsは、チャートのトレンドラインの方程式テキストを返す[**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/)プロパティを提供しています。このプロパティを利用するには、まず[**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)メソッドを呼び出す必要があります。

{{% /alert %}}

以下のスクリーンショットは、トレンドライン付きのチャートと、その式テキストが赤色で表示されたものです。この式テキストは、以下のサンプルコードの [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) プロパティを使用して取得します。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++コードでチャートトレンドラインの方程式テキストを取得する方法

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
