---
title: Excel Grafiklerinde Veri Etiketlerini C++ ile Yönetin
linktitle: VeriEtiketleri
type: docs
weight: 50
url: /tr/cpp/insert-datalabels-to-chart/
description: Aspose.Cells for C++ kullanarak Excel grafiklerindeki veri etiketlerini nasıl etkin biçimde yöneteceğinizi öğrenin. Kapsamlı kılavuzumuz, etiketleri ekleme, kaldırma ve değiştirme gibi çeşitli yönetim görevlerini kapsar ve grafik okunabilirliğini ve kullanılabilirliğini artırmaya yardımcı olur.
keywords: Aspose.Cells for C++, Excel grafikler, veri etiketleri, yönetim, okunabilirlik, kullanılabilirlik, ekleme, kaldırma, değiştirme.
---

{{% alert color="primary" %}}

 VeriEtiketleri, bir grafikte önemli bir parça. Her serinin değerini, yüzdesini vb. kolayca bilebiliriz.

{{% /alert %}}

## **VeriEtiketleri Seçenekleri**
Aspose.Cells, ayrıca, [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) nesnesi ile çalışma sırasında grafiklerin veri etiketlerini yönetmenize olanak tanır. Veri etiketlerini taşımak, güncellemek ve biçimlendirmek oldukça basittir.

|![todo:image_alt_text](chart_datalabels.png)|

## **Grafiğin VeriEtiketlerini Yönetme**
Aspose.Cells ile grafik veri etiketlerini [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) ile yönetmek çok kolaydır.

Aşağıdaki kod parçacığı, Veri Etiketlerini nasıl yöneteceğinizi gösterir:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Grafiğin Serisinde Veri Noktalarına Özel Etiketler Ekleme](/cells/tr/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Grafiklerin Veri Etiketlerinde Metin Kırpmayı Devre Dışı Bırak](/cells/tr/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Veri Etiket Şeklini Metne Sığacak Şekilde Yeniden Boyutlandır](/cells/tr/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Grafik Noktasının Zengin Metin Özel Veri Etiketi](/cells/tr/cpp/rich-text-custom-data-label-of-chart-point/)
- [Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama](/cells/tr/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Veri Etiketleri Olarak Hücre Aralığını Gösterme](/cells/tr/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
