---
title: C++ kullanarak Açık Yüksek Düşük Kapanış (OHLC) Stok Grafiği Oluşturma
description: Aspose.Cells for C++ kullanarak açık yüksek düşük kapanış hisse senedi grafiği nasıl oluşturulur onu gösteriyoruz. Adım adım kılavuzumuz, hisse senedi verilerini, açık, yüksek, düşük ve kapanış fiyatlarını grafiğe yansıtmanıza yardımcı olacak.
keywords: Aspose.Cells for C++, Açık Yüksek Düşük Kapanış Hisse Senedi Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.
type: docs
weight: 182
url: /tr/cpp/create-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
Açık-Yüksek-Düşük-Kapalı (OHLC) grafiği beş veri sütununu kullanır: kategori, açılış, yüksek, düşük ve kapanış sırasıyla. Her kategori için fiyat aralığı yine dikey bir çizgi ile gösterilirken, açılış ve kapanış arasındaki aralık daha geniş bir kayan çubukla gösterilir; eğer fiyat kategoride artarsa (kapanış, açılıştan yüksekse), çubuk bir renkle doldurulur, fiyat azalırsa başka bir renkle doldurulur. Bu tür bir grafik sıklıkla mum grafik olarak adlandırılır.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Grafikte görünürlük iyileştirmeleri**
Fiyatların artış ve azalışını göstermek için sıkça renkler kullanırız, siyah-beyaz yerine. Aşağıdaki ilk mum çubuğu setinde kırmızı artışları, yeşil azalışları gösterir.

![todo:image_alt_text](sample2.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

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
