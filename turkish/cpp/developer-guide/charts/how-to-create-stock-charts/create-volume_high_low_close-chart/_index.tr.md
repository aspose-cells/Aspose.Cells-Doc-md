---
title: C++ kullanarak Hacim Yüksek Düşük Kapanış (VHLC) Stok Grafiği Oluşturma
linktitle: Hacim Yüksek Düşük Kapanış(VYDK) Hisse Senedi Grafiği Oluşturma
description: Aspose.Cells for C++ kullanarak hacim yüksek düşük kapanış stok grafiği nasıl oluşturulur onu gösteriyoruz. Adım adım rehberimiz, hisse senedi verilerini, hacim, yüksek, düşük ve kapanış fiyatlarını grafiğe yansıtmanıza yardımcı olacak.
keywords: Aspose.Cells for C++, Hacim Yüksek Düşük Kapanış Stok Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.
type: docs
weight: 183
url: /tr/cpp/create-volume-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
 Üçüncü stok grafiğimiz Hacim Yüksek Düşük Kapanış grafiği. Yine, verilerin doğru sırada olması gerektiğini tekrar etmek önemlidir. Verilerinizi yeniden düzenlemeniz gerekiyorsa, grafiği kurmadan önce yapmalısınız. Bu grafik, ilk (kategori) sütunundan hemen sonra bir hacim sütunu içerir ve grafikler bu hacmi gösteren bir ana eksende, fiyatlar ise ikincil eksende yer alır.

![todo:image_alt_text](data.png)
## **Hacim-Yüksek-Düşük-Kapanış (VYDK) hisse senedi grafiği**

![todo:image_alt_text](sample.png)
## **Örnek Kod**
Aşağıdaki örnek kod [örnek Excel dosyasını](Volume-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

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

