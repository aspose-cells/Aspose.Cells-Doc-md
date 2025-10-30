---
title: Volume High Low Close(VHLC) 株式チャートをC++で作成
linktitle: 出来高 高値 安値 終値（VHLC）株価チャートを作成する
description: Aspose.Cells for C++を使用して、出来高高低終値株価チャートの作成方法を学びましょう。私たちのガイドは、市場データをチャートにプロットし、分析と視覚化を改善する方法を示します。
keywords: Aspose.Cells for C++、出来高高低終値株価チャート、市場データ、分析、ビジュアライゼーション。
type: docs
weight: 183
url: /ja/cpp/create-volume-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
3番目の株価チャートは、出来高高低終値チャートです。繰り返しになりますが、データを正しい順序にすることが重要です。データテーブルを並べ替える必要がある場合は、チャートを設定する前に行ってください。このチャートには、最初の（カテゴリ）列の直後に出来高の列が含まれており、チャートにはこの出来高を示すプライマリ軸の列チャートが含まれます。価格はセカンダリ軸に移動します。

![todo:image_alt_text](data.png)
## **出来高-高値-安値-終値（VHLC）株価チャート**

![todo:image_alt_text](sample.png)
## **サンプルコード**
[サンプルExcelファイル](Volume-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


{{< app/cells/assistant language="cpp" >}}
