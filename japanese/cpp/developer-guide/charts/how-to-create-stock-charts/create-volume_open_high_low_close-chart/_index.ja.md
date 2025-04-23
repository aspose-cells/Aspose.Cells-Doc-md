---
title: C++を使用してVolume Open High Low Close（VOHLC）株価チャートを作成
description: Aspose.Cells for C++を使ったボリューム オープン ハイ ロー クローズ株価チャートの作成方法を学びましょう。私たちのガイドは、市場データをチャートにプロットし、分析と視覚化を改善する方法を示します。
keywords: Aspose.Cells for C++、出来高 オープン ハイ ロー クローズ株価チャート、市場データ、分析、ビジュアライゼーション。
type: docs
weight: 184
url: /ja/cpp/create-volume-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
次に紹介する株価チャートはボリュームオープンハイロークローズチャートです。データの順番を守ることが重要です。必要に応じてデータテーブルを並べ替えてください。このチャートには、最初の（カテゴリ）列の直後にボリュームの列があり、主要軸にこのボリュームを示す棒グラフを配置し、価格は副軸に移動しています。

![todo:image_alt_text](data.png)

## **出来高-オープン-高値-安値-終値（VOHLC）株価チャート**

![todo:image_alt_text](sample.png)

## **サンプルコード**
[サンプルExcelファイル](Volume-Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
