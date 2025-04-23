---
title: C++でサンバーストチャートを作成する方法
description: 円形にデータを表示するチャートであるAspose.Cells for C++のサンバーストチャートの作成方法を学びます。ガイドは、データラベル、凡例、色など、さまざまなプロパティやフォーマットの設定を支援します。
keywords: Aspose.Cells for C++、サンバーストチャート、作成、プロパティ設定、データラベル、凡例、フォーマット、カラー、円、データレンダリング。
type: docs
weight: 162
url: /ja/cpp/creating-sunburst-chart/
---

## **可能な使用シナリオ**
ツリーマップチャートは階層内の比率比較に適していますが、最大のカテゴリと各データポイント間の階層レベルの表示には優れていません。サンバーストチャートはそれを示すのに非常に適した視覚的なチャートです。サンバーストチャートは階層的なデータを表示するのに理想的です。階層の各レベルは一つのリングまたは円で表され、最も内側の円が階層のトップを示します。階層データのないサンバーストチャート（カテゴリレベル一つの場合）はドーナツチャートに似ています。しかし、複数のカテゴリレベルを持つサンバーストチャートは、外側のリングが内側のリングとどのように関連しているかを示します。サンバーストチャートは、一つのリングがどのようにその寄与部分に分解されているかを最も効果的に示す一方で、もう一つの階層チャートであるツリーマップは相対的なサイズを比較するのに最適です。

![todo:image_alt_text](sample.png)
## **サンバーストチャート**
以下のコードを実行すると、下記のサンバーストチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
下記のサンプルコードは、[サンプルExcelファイル](sunburst.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
