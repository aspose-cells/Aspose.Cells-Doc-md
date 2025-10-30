---
title: C++ kullanarak Hacim Açık Yüksek Düşük Kapanış (VOHLC) Stok Grafiği Oluşturma
description: Aspose.Cells for C++ kullanarak hacim açık yüksek düşük kapanış stok grafiği nasıl oluşturulur onu gösteriyoruz. Adım adım kılavuzumuz, hisse senedi verilerini, hacim, açık, yüksek, düşük ve kapanış fiyatlarını grafik üzerine yerleştirmenize yardımcı olacak.
keywords: Aspose.Cells for C++, Hacim Açık Yüksek Düşük Kapanış Stok Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.
type: docs
weight: 184
url: /tr/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
 Dördüncü hisse senedi grafiğimiz Hacim Açık Yüksek Düşük Kapanış grafiği. Yine, verilerin doğru sırada olması gerektiğini tekrar etmek önemlidir. Verilerinizi yeniden düzenlemeniz gerekiyorsa, grafiği kurmadan önce yapmalısınız. Bu grafik, ilk (kategori) sütunundan hemen sonra bir hacim sütunu içerir ve grafikler bu hacmi gösteren bir ana eksende, fiyatlar ise ikincil eksende yer alır.

![todo:image_alt_text](data.png)

## **Hacim-Açılış-Yüksek-Düşük-Kapanış (VAYDK) hisse senedi grafiği**

![todo:image_alt_text](sample.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Volume-Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

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
{{< app/cells/assistant language="cpp" >}}
