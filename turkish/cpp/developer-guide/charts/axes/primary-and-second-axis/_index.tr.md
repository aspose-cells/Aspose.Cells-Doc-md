---
title: Birincil ve İkincil Eksen ile C++
linktitle: Birinci ve İkinci Eksen
description: Aspose.Cells for C++ te birincil ve ikincil eksenleri anlamayı ve bunlarla çalışma yollarını öğrenin. Rehberimiz, birincil ve ikincil eksenler arasındaki farkları anlamanıza ve bunları diyagramlarınızda etkin bir şekilde nasıl yapılandırıp kullanacağınızı anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, birincil eksenler, ikincil eksenler, anlama, farklar, yapılandırma, kullanım.
type: docs
weight: 190
url: /tr/cpp/primary-and-second-axis/
---

## **Olası Kullanım Senaryoları**
Bir grafikte veri serilerinden veri serilerine geniş bir değişkenlik olduğunda veya karışık tiplerde veri (fiyat ve hacim) olduğunda, bir veya daha fazla veri serisini ikincil dikey (değer) ekseninde grafiğe plotlayın. İkincil dikey eksenin ölçeği, ilişkili veri serileri için değerleri gösterir. İkincil bir eksen, sütun ve çizgi grafiklerinin bir kombinasyonunu gösteren bir grafikte iyi çalışır.

## **Birincil ve İkinci Ekseni Microsoft Excel gibi ele alın**
Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına yerleştiren örnek kodu aşağıda inceleyiniz. 
Ardından bir grafik ekleriz ve ikinci ekseni gösteririz.

![todo:image_alt_text](excel.png)

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
