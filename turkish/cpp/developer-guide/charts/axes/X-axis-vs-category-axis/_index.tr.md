---
title: X Ekseni ve Kategori Ekseni C++ ile
linktitle: X Ekseni ve Kategori Ekseni Arasındaki Fark
description: Aspose.Cells for C++ te X ekseni ile Kategori ekseni arasındaki farkları öğrenin. Kılavuzumuz, kullanım ve özelliklerindeki farkları anlamanıza ve ihtiyaçlarınıza göre yapılandırmanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, X ekseni, Kategori ekseni, fark, kullanım, özellikler, yapılandırma.
type: docs
weight: 180
url: /tr/cpp/X-axis-vs-category-axis/
---

## **Olası Kullanım Senaryoları**
Farklı türde X ekseni bulunmaktadır. Y ekseni Bir Değer tipi ekseni iken X ekseni Kategori tipi eksen veya Değer tipi eksen olabilir. Değer eksenini kullanarak, veri sürekli değişen sayısal veri olarak işlenir ve işaretçi, numerik değerine göre değişen bir noktaya yerleştirilir. Kategori ekseni kullanarak, veri, sayısal olmayan metin etiketlerinden oluşan bir dizi olarak işlenir ve işaretçi, dizideki konumuna göre eksen boyunca bir noktaya yerleştirilir. Aşağıdaki örnek, Değer ve Kategori Eksenleri arasındaki farkı açıklar.
Örnek verilerimiz [örnek Tablo dosyasında](sample.png) gösterilmektedir. İlk sütun, Kategori veya Değer olarak işleme alınabilen X ekseni verilerimizi içerir. Sayıların eşit aralıklarla dağılmadığına veya hatta sayısal sırayla görünmediğine dikkat edin.

![todo:image_alt_text](sample.png)

## **X ve Kategori eksenini Microsoft Excel gibi ele alın**
İlk grafik XY (Dağılım) grafiği olup X değerleri Eksen olarak kullanılır; ikinci grafik ise çizgi grafik olup X, Kategori Eksenidir.

![todo:image_alt_text](compare.png)

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in charts
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(3);
    worksheet.GetCells().Get(u"A4").PutValue(2.5);
    worksheet.GetCells().Get(u"A5").PutValue(3.5);
    worksheet.GetCells().Get(u"B1").PutValue(u"Cats");
    worksheet.GetCells().Get(u"C1").PutValue(u"Dogs");
    worksheet.GetCells().Get(u"D1").PutValue(u"Fishes");
    worksheet.GetCells().Get(u"B2").PutValue(7);
    worksheet.GetCells().Get(u"B3").PutValue(6);
    worksheet.GetCells().Get(u"B4").PutValue(5);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(5);
    worksheet.GetCells().Get(u"C4").PutValue(4);
    worksheet.GetCells().Get(u"C5").PutValue(3);
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(7);
    worksheet.GetCells().Get(u"D4").PutValue(3);
    worksheet.GetCells().Get(u"D5").PutValue(2);

    // Create Line Chart: X as Category Axis
    int pieIdx = worksheet.GetCharts().Add(ChartType::LineWithDataMarkers, 6, 15, 20, 21);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$5");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Create XY (Scatter) Chart: X as Value Axis
    pieIdx = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);

    // Retrieve the Chart object
    chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set X values for series
    chart.GetNSeries().Get(0).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(1).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(2).SetXValues(u"{1,3,2.5,3.5}");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"XAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
