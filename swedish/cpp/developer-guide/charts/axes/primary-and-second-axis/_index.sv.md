---
title: Primär och sekundär axel med C++
linktitle: Primär och sekundär axel
description: Lär dig hur du förstår och arbetar med primära och sekundära axlar i Aspose.Cells for C++. Vår guide hjälper dig att förstå skillnaderna mellan primära och sekundära axlar, och hur du konfigurerar och använder dem effektivt i dina diagram.
keywords: Aspose.Cells for C++, primära axlar, sekundära axlar, förståelse, skillnader, konfiguration, användning.
type: docs
weight: 190
url: /sv/cpp/primary-and-second-axis/
---

## **Möjliga användningsscenario**
När siffrorna i ett diagram varierar kraftigt mellan data serier eller när du har blandade typer av data (pris och volym), plotta en eller flera data serier på en sekundär vertikal (värde) axel. Skalan för den sekundära vertikala axeln visar värdena för de associerade data serierna. En sekundär axel fungerar bra i ett diagram som visar en kombination av stapel- och linjediagram.

## **Hantera primär- och sekundäraxel som i Microsoft Excel**
Se följande kodexempel som skapar en ny Excel-fil och placerar diagramvärden i det första arket. 
Sedan lägger vi till ett diagram och visar den sekundära axeln.

![todo:image_alt_text](excel.png)

## **Exempelkod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
