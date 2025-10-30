---
title: C++ ile Excel Grafiklerinin Eksenlerini Yönetme
description: Aspose.Cells for C++ te grafik eksenlerini nasıl yapılandıracağınızı öğrenin. Rehberimiz, ana ve ikincil eksenleri ayarlama, aralıklarını belirleme ve özelliklerini değiştirme yollarını gösterecek.
keywords: Aspose.Cells for C++, grafik eksenleri, yapılandırma, ana eksenler, ikincil eksenler, aralık, özellikler.
linktitle: Eksenler
type: docs
weight: 50
url: /tr/cpp/chart-axes/
---

{{% alert color="primary" %}}

Excel grafiklerinde 3 çeşit eksen bulunmaktadır:
1. Yatay (Kategori) Eksen : X Eksen
1. Dikey (Değer) Eksen : Y Eksen
1. Derinlik (Seri) Eksen : Z Eksen

{{% /alert %}}

## **Eksen Seçenekleri**
Aspose.Cells ayrıca çalışma zamanında grafik eksenlerini yönetmenize olanak tanır. [Eksen](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) nesnesi kullanarak, Excel'deki gibi tüm Eksen seçeneklerini değiştirebilirsiniz.

|![todo:image_alt_text](chart_axes.png)|

## **X ve Y Eksenlerini Yönetme**

Excel grafiklerinde, yatay ve dikey eksenler en sık kullanılan iki eksendir.

Aşağıdaki kod parçacığı, X ve Y eksenlerinin ayarlarını nasıl yapacağınızı gösterir.

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
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Tick Etiketi Yönünü Değiştirme](/cells/tr/cpp/change-tick-label-direction/)
- [Grafikte Hangi Eksenin Var Olduğunu Belirleme](/cells/tr/cpp/determine-which-axis-exists-in-the-chart/)
- [Grafik Ekseni Otomatik Birimleri ile Başa Çık](/cells/tr/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma](/cells/tr/cpp/read-axis-labels-after-calculating-the-chart/)
- [Excel Grafikte Kategori Eksenini Nasıl Ayarlayacağınız](/cells/tr/cpp/how-to-set-category-axis/)
{{< app/cells/assistant language="cpp" >}}
