---
title: Excelグラフの軸の管理（C++）
description: Aspose.Cells for C++でグラフの軸設定方法を学びます。プライマリ軸およびセカンダリ軸の調整、範囲の設定、プロパティの変更など、グラフを改善する方法をガイドします。
keywords: Aspose.Cells for C++、グラフ軸、設定、プライマリ軸、セカンダリ軸、範囲、プロパティ
linktitle: 軸
type: docs
weight: 50
url: /ja/cpp/chart-axes/
---

{{% alert color="primary" %}}

Excelチャートには、3種類の軸があります。
1. 水平（カテゴリ）軸：X軸
2. 垂直（値）軸：Y軸
3. 深さ（系列）軸：Z軸

{{% /alert %}}

## **軸オプション**
Aspose.Cellsは実行時にグラフの軸を管理することも可能です。 [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/)オブジェクトを使用して、Excelと同様に軸のすべてのオプションを変更できます。

|![todo:image_alt_text](chart_axes.png)|

## **X軸とY軸を管理する**

Excelのグラフでは、水準軸と垂直軸の二つが最も一般的に使われています。

次のコードスニペットは、X軸とY軸のオプション設定方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## ** 高度なトピック**
- [目盛りラベル方向の変更](/cells/ja/cpp/change-tick-label-direction/)
- [チャートに存在する軸を特定する](/cells/ja/cpp/determine-which-axis-exists-in-the-chart/)
- [Microsoft Excelのようにチャートの軸の自動単位を処理する](/cells/ja/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [チャートを計算した後に軸ラベルを読み取る](/cells/ja/cpp/read-axis-labels-after-calculating-the-chart/)
- [Excelチャートでカテゴリ軸を設定する方法](/cells/ja/cpp/how-to-set-category-axis/)
