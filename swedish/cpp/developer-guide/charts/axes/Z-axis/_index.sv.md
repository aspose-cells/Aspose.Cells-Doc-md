---
title: Z axel med C++
linktitle: Z axel
description: Lär dig att arbeta med Z axeln i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du konfigurerar och anpassar Z axeln, inklusive dess skala och etiketter, för att förbättra dina diagram.
keywords: Aspose.Cells for C++, Z axel, diagram, konfiguration, anpassning, skala, etiketter.
type: docs
weight: 210
url: /sv/cpp/z-axis/
---

## **Möjliga användningsscenario**
För vissa 3-D diagram som 3-D pelare, 3-D kon, eller 3-D pyramid som har en djup (serie) axel, även känd som Z-axeln, som du kan ändra. Du kan specificera intervallet mellan tickmarkeringar, axeletiketter och andra operationer.

## **Hantera primär- och sekundäraxel som i Microsoft Excel**
Se följande exempel på kod som skapar en ny Excel-fil och placerar diagrammets värden i det första kalkylbladet. Sedan lägger vi till ett diagram och ställer in diagramtypen till Column3D, och du kan se Z-axeln även kallad djupaxel. 

![todo:image_alt_text](excel.png)

## **Exempelkod**
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
