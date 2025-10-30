---
title: C++ ile Excel Grafiklerinin Legend ını Yönetme
linktitle: Açıklama
description: Microsoft Excel de grafik legendlarını etkin ve özelleştirmek için Aspose.Cells for C++ i nasıl kullanacağınızı öğrenin. Kapsamlı kılavuzumuz, legendların işlevselliğini, nasıl erişilip değiştirildiğini ve legendlar ile görselleştirmeyi ve veri anlayışını nasıl geliştireceğinizi açıklamaktadır.
keywords: Aspose.Cells for C++, Grafik Legendları, Microsoft Excel, Görselleştirme, Veri Anlayışı.
type: docs
weight: 50
url: /tr/cpp/chart-legend/
---

## **Açıklama Seçenekleri**
Aspose.Cells ayrıca çalışma zamanında grafik legendını yönetmenize imkan tanır. [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) nesnesi ile legendı taşıyabilir, güncelleyebilir ve biçimlendirebilirsiniz.

|![todo:image_alt_text](chart_legend.png)|

## **Grafiğin Açıklamasını Ayarlama**
Aspose.Cells ile bir grafiğin legendını yönetmek çok basittir [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

Aşağıdaki kod parçacığı, legend yönetimini nasıl yapacağınızı göstermektedir:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
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

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gelişmiş Konular**
- [Grafik lejant giriş dolgu metnini hiçbir şeye ayarlayın using Aspose.Cells](/cells/tr/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
