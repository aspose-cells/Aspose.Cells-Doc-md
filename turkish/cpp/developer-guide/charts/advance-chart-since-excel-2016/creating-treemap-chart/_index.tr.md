---
title: C++ ile TreeMap grafiği nasıl oluşturulur
description: Aspose.Cells for C++ te Treemap grafiği oluşturmayı öğrenin. Kılavuzumuz, renkler, etiketler ve veri gösterimleri gibi Treemap grafiklerinin çeşitli özelliklerini ve biçimlendirme seçeneklerini anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, Treemap grafiği, oluşturma, özellikler, biçimlendirme, renkler, etiketler, veri gösterimi, dairesel grafik, hiyerarşik grafik.
type: docs
weight: 161
url: /tr/cpp/creating-treemap-chart/
---

## **Olası Kullanım Senaryoları**
Ağaç haritası grafiği verilerinizin hiyerarşik bir görünümünü sağlar ve hangi ürünlerin bir mağazanın en çok satanları olduğunu görmek gibi desenleri kolayca belirlemenize olanak tanır. Ağaç dalları dikdörtgenlerle temsil edilir ve her alt dal daha küçük bir dikdörtgen olarak gösterilir. Ağaç haritası grafikleri kategorileri renk ve yakınlıkla gösterir ve diğer grafik türleri ile zor olacak birçok veriyi kolayca gösterebilir.

![todo:image_alt_text](sample.png)
## **Ağaç Haritası Grafiği**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Ağaç Haritası grafiğini göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod [örnek Excel dosyasını](treemap.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
