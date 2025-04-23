---  
title: C++ ile Combo grafik nasıl oluşturulur?  
linktitle: Kombo Grafik Nasıl Oluşturulur  
description: Aspose.Cells for C++ kullanarak bir kombolu grafik nasıl oluşturulur öğrenin. Kapsamlı kılavuzumuz, farklı grafik türlerini daha etkili veri sunumu için birleştirme yöntemlerini gösterecektir.  
keywords: Aspose.Cells for C++, Kombolu Grafik, Grafik Türlerini Birleştirme, Veri Sunumu, Etkili Görselleştirme.  
type: docs  
weight: 73  
url: /tr/cpp/create-combo-chart/  
---  

## **Olası Kullanım Senaryoları**  
Excel'deki kombo grafikler, verinizi anlaşılır hale getirmek için iki veya daha fazla grafik türünü kolayca birleştirebileceğiniz bu seçeneği kullanmanızı sağlar. Kombo grafikler, verinizin fiyat ve hacim dahil olmak üzere birden çok türde değeri içerdiğinde yardımcı olur. Ayrıca, veri serilerinizin sayıları seriye göre geniş ölçüde değiştiğinde Kombo grafikler uygundur.  


![todo:image_alt_text](sample.png)  
## **Kombo grafik**  
Aşağıdaki kodu çalıştırdıktan sonra, aşağıda gösterildiği gibi Kombo grafiği göreceksiniz.  

![todo:image_alt_text](result.png)  
## **Örnek Kod**  
Aşağıdaki örnek kod [örnek Excel dosyasını](combo.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook
    Workbook workbook(u"combo.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a stock volume (VHLC) chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 15, 0, 34, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title
    chart.GetTitle().SetText(u"Combo Chart");

    // Set the Legend position to bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E12", true);

    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A12";

    // Set the Series[1], Series[2], and Series[3] to different Marker Styles
    for (int32_t j = 0; j < chart.GetNSeries().GetCount(); j++)
    {
        switch (j)
        {
            case 1:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Circle);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Pink());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 2:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Orange());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 3:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Square);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::LightBlue());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
        }
    }

    // Set the chart type for Series[0]
    chart.GetNSeries().Get(0).SetType(ChartType::Line);

    // Set style for the border of the first series
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Solid);

    // Set color for the first series
    chart.GetNSeries().Get(0).GetBorder().SetColor(Color::DarkBlue());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```  
