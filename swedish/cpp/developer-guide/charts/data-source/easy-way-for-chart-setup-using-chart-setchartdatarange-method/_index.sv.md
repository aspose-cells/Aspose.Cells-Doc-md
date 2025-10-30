---
title: Enkel metod för diagramuppsättning med hjälp av Chart.SetChartDataRange metoden i C++
linktitle: Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange metoden
description: Lär dig hur du enkelt konfigurerar diagram med hjälp av Chart.SetChartDataRange metoden i Aspose.Cells for C++. Vår guide visar hur du specificerar dataintervall för ditt diagram, vilket gör att du kan skapa professionella och exakta diagram med minimal ansträngning.
keywords: Aspose.Cells for C++, diagram, SetChartDataRange metoden, dataintervall, professionell, exakt, diagram.
type: docs
weight: 190
url: /sv/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu [**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/)-metoden för att enkelt ställa in diagram. Genom att använda denna metod behöver du inte längre lägga till serie och kategoriaxel data separat.

{{% /alert %}}

Följande exempelkod förklarar användningen av [**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/) metoden för att lätt sätta upp diagram.

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
