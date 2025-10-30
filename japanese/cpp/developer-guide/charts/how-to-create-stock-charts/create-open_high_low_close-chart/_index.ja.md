---
title: Open High Low Close(OHLC)株式チャートをC++で作成
description: Aspose.Cells for C++を使った始値高値安値終値の株式チャートの作成方法を学びます。株式市場データ（始値、高値、安値、終値）をチャートにプロットし、分析と可視化を向上させます。
keywords: Aspose.Cells for C++、始値高値安値終値株式チャート、株式市場データ、分析、可視化。
type: docs
weight: 182
url: /ja/cpp/create-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
Open-High-Low-Close（OHLC）チャートは、カテゴリ、オープン、ハイ、ロー、クローズのデータを使用し、価格の範囲は垂直線で示され、オープンからクローズまでの範囲はより広い浮動バーで示されます。カテゴリ内で価格が上昇する場合（クローズがオープンより高い場合）、バーは1つの色で塗りつぶされ、価格が下落する場合は別の色で塗りつぶされます。この種のチャートは、ローソク足チャートと呼ばれることがよくあります。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **チャートの可視性の改善**
価格の上昇と下降を示すために黒白よりも色をよく使用します。下の最初のキャンドルスティックのセットでは、赤は上昇、緑は下降を示しています。

![todo:image_alt_text](sample2.png)

## **サンプルコード**
[サンプルExcelファイル](Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
