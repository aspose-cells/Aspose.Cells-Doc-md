---
title: C++を使ったExcelグラフの凡例管理
linktitle: 凡例
description: Microsoft Excelでのチャート凡例の効果的な利用とカスタマイズにAspose.Cells for C++を活用する方法について解説します。当ガイドは、凡例の機能、アクセス方法、編集方法、視覚化の向上やデータ理解のための改善方法について詳しく説明します。
keywords: Aspose.Cells for C++、チャート凡例、Microsoft Excel、視覚化、データ理解。
type: docs
weight: 50
url: /ja/cpp/chart-legend/
---

## **凡例オプション**
Aspose.Cellsを使えば、ランタイム中にチャートの凡例を管理できます。[凡例](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/)オブジェクトを使用すれば、凡例の移動、更新、フォーマットが可能です。

|![todo:image_alt_text](chart_legend.png)|

## **チャートの凡例の設定**
Aspose.Cellsの[凡例](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/)を使えば、凡例の管理は非常に簡単です。

凡例管理のためのコードスニペットは次のとおりです：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **上級トピック**
- [Aspose.Cellsを使用して、チャートの凡例エントリの塗りをなしに設定する方法を説明します。](/cells/ja/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
