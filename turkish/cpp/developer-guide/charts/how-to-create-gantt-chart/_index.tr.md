---
title: C++ ile Gantt Grafiği Nasıl Oluşturulur?
linktitle: Gantt grafiği nasıl oluşturulur?
type: docs
weight: 72
url: /tr/cpp/how-to-create-gantt-chart/
description: Aspose.Cells for C++ API kullanarak Gantt grafiği nasıl oluşturulur öğrenin.
keywords: C++ ile Gantt grafiği oluşturma, Gantt grafiği ekleme, Gantt grafiği ekleme
---

## **Gantt grafiği nedir?**

Gantt grafiği, bir proje takvimini anlatan bir tür çubuk grafik türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik, süresine karşılık gelen bir çubukla temsil edilir. Gantt grafikleri ayrıca görevler arasındaki bağımlılıkları gösterir, böylece proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Bunlar, proje yönetiminde projeleri etkin şekilde planlamak, zamanlamak ve izlemek için yaygın olarak kullanılır.

## **Excel'de Gantt Grafiği Nasıl Oluşturulur?**

Excel'de Gantt grafiği oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1. Gantt grafiği için bazı veri ekleyin. 
<br>
<img src="00.png" width=50% />
1. Veriyi seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafik Ekle --> Katlı Çubuk Grafik seçeneklerini kullanın. Örneğimizde, B1:B7, ve ardından **Katlı Çubuk** grafiği ekleyin.
<br>
<img src="1.png" width=50% />

1. Grafiği seçin, **Veri Seç**->**Ekle**, **Seri adı** ve **Seri değerleri** aşağıdaki gibi ayarlayın.
<br>
<img src="2.png" width=50% />

1. Grafiği seçin, **Yatay (Kategori) Eksen Etiketleri** düzenleyin.
<br>
<img src="3.png" width=50% />

1. **Eksen Biçimlendir** seçeneğiyle Y Ekseni, **Kategorileri ters sırada** seçin.
1. **Mavi Seri**yi seçin ve **Dolgu->HIÇ BİLGİ DOLGU** olarak ayarlayın.
1. **Eksen Biçimlendir** seçeneğiyle X Ekseni, **Minimum ve Maksimum**(1/5/2019:43470, 1/30/2019:43494) ayarını yapın.
<br>
<img src="4.png" width=50% />

1. Grafik için **Veri Etiketleri Ekle**, şimdi bir Gantt grafiği elde edeceksiniz.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Çizelgesi Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayanarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri belirler. Son olarak, çalışma kitabını [çıkış XLSX formatında](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan Gantt çizelgesini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
