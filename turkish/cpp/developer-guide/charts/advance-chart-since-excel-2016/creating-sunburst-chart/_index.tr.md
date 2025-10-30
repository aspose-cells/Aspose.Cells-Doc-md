---
title: Nasıl Oluşturulur C++ ile Sunburst grafiği
description: Aspose.Cells for C++ te nasıl güneş patlaması grafiği oluşturulacağını öğrenin; bu grafik daire içinde verileri gösterir. Kılavuzumuz, grafiğinizin çeşitli özelliklerini ve biçimlendirmesini ayarlamanıza, veri etiketleri, efsaneler, renkler ve daha fazlasını içerecek şekilde yardımcı olacaktır.
keywords: Aspose.Cells for C++, güneş patlaması grafiği, oluşturma, özellikleri ayarlama, veri etiketleri, efsane, biçim, renk, daire, veri görselleştirme.
type: docs
weight: 162
url: /tr/cpp/creating-sunburst-chart/
---

## **Olası Kullanım Senaryoları**
Treemap grafikler, hiyerarşi içindeki oranları karşılaştırmak için iyidir, fakat treemap grafikler, en büyük kategoriler ile her veri noktası arasındaki hiyerarşik seviyeleri göstermek konusunda iyi değildir. Bir güneş patlaması grafiği, bunu göstermek için çok daha iyi görsel bir grafik. Güneş patlaması grafiği, hiyerarşik verileri göstermek için idealdir. Hiyerarşinin her seviyesi bir halka veya daire ile temsil edilir; en içteki daire en yüksek seviyededir. Hiyerarşik veri olmayan (bir seviye kategoriler) bir güneş patlaması grafiği, bir halka grafiğine benzese de, çok seviyeli kategorilerde, dış halkaların iç halkalara nasıl bağlandığını gösterir. Güneş patlaması grafiği, bir halkanın katılma parçalarını nasıl gösterdiğine dair en iyi sonucu verirken, başka bir hiyerarşik grafik türü olan treemap, göreceli büyüklükleri karşılaştırmak için idealdir.

![todo:image_alt_text](sample.png)
## **Güneş Patlaması Grafiği**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Güneş patlaması grafiğini göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](sunburst.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
