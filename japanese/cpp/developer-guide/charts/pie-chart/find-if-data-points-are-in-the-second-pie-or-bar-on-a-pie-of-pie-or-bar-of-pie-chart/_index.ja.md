---
title: C++を使用して、ピース・オブ・ピースやバード・オブ・ピースの円グラフでデータポイントが第2の円または棒にあるかどうかを見つける方法
linktitle: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける
description: Aspose.Cells for C++を使って、円グラフの第2の円または棒にデータポイントがあるかどうかを見つける方法を学びましょう。ガイドは、合成チャートのセカンダリの円や棒を識別およびアクセスし、データを効果的に分析・操作する方法を示します。
keywords: Aspose.Cells for C++、ピース・オブ・ピースチャート、バー・オブ・ピースチャート、セカンダリの円、セカンダリの棒、データ分析、データ操作。
type: docs
weight: 180
url: /ja/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用して、シリーズのデータポイントが『ピース・オブ・ピース』や『バード・オブ・ピース』の円グラフの第2の円または棒にあるかどうかを判定できます。詳細は[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/)プロパティを使用してください。

以下のサンプルコードで作成されたコンソール出力を参照してください。サンプルコードで使用される[サンプルエクセルファイル](5115193.xlsx) を開くと、10未満のすべてのデータポイントが *バーオブパイ* チャートの内部にあることが、コンソール出力にも示されています。

## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**
以下のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートでデータポイントが第2パイまたは棒にあるかどうかを見つける方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**
上記のサンプルコードと[サンプルExcelファイル](5115193.xlsx)を実行した後に生成されたコンソール出力をご覧ください。[IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/)が**false**の場合、そのデータポイントは円の内部にあり、**true**の場合は棒の内部にあります。

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
