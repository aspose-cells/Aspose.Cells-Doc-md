--- 
title: 高値 安値 終値(HLC)株式チャートをC++で作成 
linktitle: HLC(高値 安値 終値)株価チャートの作成 
description: Aspose.Cells for C++を使った高値 安値 終値株価チャートの作成方法を学びます。株式市場のデータ（高値、安値、終値）をチャートにプロットし、分析と可視化を向上させます。 
keywords: Aspose.Cells for C++、HLC株式チャート、株式市場データ、分析、可視化。 
type: docs 
weight: 181 
url: /ja/cpp/create-high-low-close-stock-chart/ 
--- 

## **可能な使用シナリオ** 
HLC株価チャートは4つのデータ列を使用します。最初の列は通常、日付ですが、株名も使用できます。次の3列は、順に高値、安値、終値です。各カテゴリの価格範囲は、安値から高値までの垂直線で示され、終値はこの線の右側に伸びる印が表示されます。 

![todo:image_alt_text](sample.png) 
## **チャートの可視性の改善** 
時には、チャートを直感的に見やすくするために、マーカー（終値）の外観を修正したり、2次軸に表示したりすることがあります。 

![todo:image_alt_text](sample2.png) 
## **サンプルコード** 
次のサンプルコードは[sample Excel file](High-Low-Close.xlsx)をロードし、[output Excel file](out.xlsx)を生成します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
{{< app/cells/assistant language="cpp" >}}
