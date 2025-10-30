---
title: C++ ile Z Eksenine
linktitle: Z Ekseni
description: Aspose.Cells for C++ te Z ekseni ile çalışmayı öğrenin. Kılavuzumuz, Z eksenini yapılandırma ve özelleştirme, ölçek ve etiketler dahil olmak üzere, grafiklerinizi geliştirmek için nasıl yapılandırılacağı konusunda size yardımcı olacaktır.
keywords: Aspose.Cells for C++, Z ekseni, grafik çizimi, yapılandırma, özelleştirme, ölçek, etiketler.
type: docs
weight: 210
url: /tr/cpp/z-axis/
---

## **Olası Kullanım Senaryoları**
Derinlik (seri) ekseni olarak da bilinen Z ekseni gibi bazı 3 boyutlu grafikler için değişiklik yapabilirsiniz. İşaret aralığı, eksen etiketleri ve diğer işlemleri belirtebilirsiniz.

## **Birincil ve İkinci Ekseni Microsoft Excel gibi ele alın**
Lütfen aşağıdaki örnek kodu inceleyin; bu kod yeni bir Excel dosyası oluşturur ve ilk çalışma sayfasına grafik değerlerini yerleştirir. Daha sonra bir grafik ekler ve grafik türünü Column3D olarak ayarlar, bu sayede Z Eksenini (Derinlik Eksenini) görebilirsiniz. 

![todo:image_alt_text](excel.png)

## **Örnek Kod**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
