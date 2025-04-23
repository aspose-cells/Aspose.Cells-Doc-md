--- 
title: C++ kullanarak Yüksek Düşük Kapanış (HLC) Stok Grafiği Oluşturma 
linktitle: Yüksek Düşük Kapanış (HLC) Hisse Senedi Grafiği Oluştur 
description: Aspose.Cells for C++ kullanarak yüksek düşük kapanış stok grafiği nasıl oluşturulur onu gösteriyoruz. Adım adım kılavuzumuz, hisse senedi verilerini, yüksek, düşük ve kapanış fiyatlarını grafik üzerine yerleştirmenize yardımcı olacak. 
keywords: Aspose.Cells for C++, Yüksek Düşük Kapanış Stok Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme. 
type: docs 
weight: 181 
url: /tr/cpp/create-high-low-close-stock-chart/ 
--- 

## **Olası Kullanım Senaryoları** 
Yüksek-Düşük-Kapanış (HLC) hisse senedi grafiği dört veri sütununu kullanır. İlk sütun genellikle bir tarihtir, ancak hisse adları da kullanılabilir. Sıradaki üç sütun, sırasıyla yüksek, düşük ve kapanış fiyatları içindir. Her kategori için fiyat aralığı, düşükten yükseğe dikey bir çizgi ile gösterilir ve kapanış fiyatı, bu çizginin sağında uzayan bir işaret kullanılarak gösterilir. 

![todo:image_alt_text](sample.png) 
## **Grafikte görünürlük iyileştirmeleri** 
Grafik daha sezgisel görünmesi için bazen işaretin görünümünü değiştirebilir veya ikincil eksen üzerinde göstermesini sağlayabiliriz. 

![todo:image_alt_text](sample2.png) 
## **Örnek Kod** 
Aşağıdaki örnek kod, [örnek Excel dosyasını](High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

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
