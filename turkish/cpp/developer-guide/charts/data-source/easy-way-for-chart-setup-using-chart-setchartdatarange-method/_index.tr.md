---
title: C++ kullanarak Chart.SetChartDataRange yöntemiyle grafik kurulumu için kolay yol
linktitle: Chart.SetChartDataRange yöntemini kullanarak Kolay Grafik Kurulumu
description: Aspose.Cells for C++ kullanarak grafiklerin veri aralığını nasıl kolayca ayarlayacağınızı öğrenin. Kılavuzumuz, grafikleriniz için veri aralığını nasıl belirleyeceğinizi göstererek profesyonel ve doğru grafikler oluşturmanıza olanak tanır.
keywords: Aspose.Cells for C++, grafik çizimi, SetChartDataRange metodu, veri aralığı, profesyonel, doğru, grafikler.
type: docs
weight: 190
url: /tr/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells artık grafikleri kolayca kurmak için [**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/) yöntemi sağlar. Bu yöntemi kullanarak, artık seri ve kategori ekseni verilerini ayrı ayrı eklemeniz gerekmez.

{{% /alert %}}

Aşağıdaki örnek kod, [**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/) yönteminin kullanımını açıklamaktadır, böylece grafik kolayca kurulur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create new workbook
    Workbook workbook(FileFormatType::Xlsx);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for chart

    // Category Axis Values
    worksheet.GetCells().Get(u"A2").PutValue(u"C1");
    worksheet.GetCells().Get(u"A3").PutValue(u"C2");
    worksheet.GetCells().Get(u"A4").PutValue(u"C3");

    // First vertical series
    worksheet.GetCells().Get(u"B1").PutValue(u"T1");
    worksheet.GetCells().Get(u"B2").PutValue(6);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"B4").PutValue(2);

    // Second vertical series
    worksheet.GetCells().Get(u"C1").PutValue(u"T2");
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(2);
    worksheet.GetCells().Get(u"C4").PutValue(5);

    // Third vertical series
    worksheet.GetCells().Get(u"D1").PutValue(u"T3");
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(4);
    worksheet.GetCells().Get(u"D4").PutValue(2);

    // Create Column chart with easy way
    int32_t idx = worksheet.GetCharts().Add(ChartType::Column, 6, 5, 20, 13);
    Chart ch = worksheet.GetCharts().Get(idx);
    ch.SetChartDataRange(u"A1:D4", true);

    // Save the workbook
    U16String outputPath = u"..\\Data\\02_OutputDirectory\\output_out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
