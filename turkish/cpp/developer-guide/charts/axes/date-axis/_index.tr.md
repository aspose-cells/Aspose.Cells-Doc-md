---
title: Tarih Eksenli C++ ile
linktitle: Tarih Ekseni
description: Aspose.Cells for C++ te tarih eksenini nasıl yöneteceğinizi öğrenin. Rehberimiz, çeşitli tarih biçimleri, zaman ölçekleri ve tik etiketi sıklıklarıyla nasıl çalışılacağını anlamanıza yardımcı olacak.
keywords: Aspose.Cells for C++, tarih ekseni, yönetim, tarih biçimleri, zaman ölçekleri, tik etiketi sıklıkları.
type: docs
weight: 200
url: /tr/cpp/date-axis/
---

## **Olası Kullanım Senaryoları**
Tarihleri kullanan çalışma sayfası verilerinden oluşturulan diyagramda, ve diyagramda yatay (kategori) eksen boyunca grafik çizildiğinde, Aspose.Cells otomatik olarak kategori eksenini bir tarih (zaman ölçeği) ekseni olarak değiştirir.
Tarih ekseni, çalışma sayfasındaki tarihleri belirli aralıklarda veya temel birimlerde, örneğin gün, ay veya yıl sayısını kronolojik sırada görüntüler, hatta çalışma sayfasındaki tarihler sıralı veya aynı temel birimlerde değilse bile.
Varsayılan olarak, Aspose.Cells, çalışma sayfasındaki en küçük iki tarih arasındaki farkı temel birimler olarak belirler. Örneğin, hisse senedi fiyatları verinizde en küçük fark yedi gün ise, Aspose.Cells temel birimi gün olarak ayarlar, ancak daha uzun bir süre boyunca hisse performansını görmek istiyorsanız temel birimi ay veya yıl yapabilirsiniz.

## **Microsoft Excel gibi Tarih Ekseni Yönetimi**
Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına yerleştiren örnek kodu aşağıda inceleyiniz. 
Ardından bir grafik ekleriz ve [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) tipini ayarlarız 
[**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) 'e ayarlar dikkate alınarak, base units için Days olarak ayarlarız.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
