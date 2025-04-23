---
title: X axel vs. Kategori axel med C++
linktitle: X axel vs. Kategori axel
description: Lär dig att särskilja mellan X axeln och kategorilänken i Aspose.Cells for C++. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, samt hur du konfigurerar dem efter dina behov.
keywords: Aspose.Cells for C++, X axel, kategorilänk, skillnad, användning, egenskaper, konfiguration.
type: docs
weight: 180
url: /sv/cpp/X-axis-vs-category-axis/
---

## **Möjliga användningsscenario**
Det finns olika typer av X-axlar. Medan Y-axeln är en Värde typ axel kan X-axeln vara en Kategori typ axel eller en Värde typ axel. Genom att använda en Värde-axel behandlas datan som kontinuerligt varierande numerisk data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Genom att använda en Kategori-axel behandlas datan som en följd av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i följden. Exemplet nedan illustrerar skillnaden mellan Värde- och Kategori-axlar.
Vår provdata visas i [provtabellfilen](sample.png) nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som Kategorier eller som Värden. Observera att siffrorna inte är jämnt fördelade, och de förekommer inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)

## **Hantera X- och Kategori-axeln som i Microsoft Excel**
Vi kommer visa denna data på två typer av diagram, det första är XY (Scatter) diagram med X som värdeaxel, det andra är linjediagram med X som kategorilänk.

![todo:image_alt_text](compare.png)

## **Exempelkod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in charts
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(3);
    worksheet.GetCells().Get(u"A4").PutValue(2.5);
    worksheet.GetCells().Get(u"A5").PutValue(3.5);
    worksheet.GetCells().Get(u"B1").PutValue(u"Cats");
    worksheet.GetCells().Get(u"C1").PutValue(u"Dogs");
    worksheet.GetCells().Get(u"D1").PutValue(u"Fishes");
    worksheet.GetCells().Get(u"B2").PutValue(7);
    worksheet.GetCells().Get(u"B3").PutValue(6);
    worksheet.GetCells().Get(u"B4").PutValue(5);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(5);
    worksheet.GetCells().Get(u"C4").PutValue(4);
    worksheet.GetCells().Get(u"C5").PutValue(3);
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(7);
    worksheet.GetCells().Get(u"D4").PutValue(3);
    worksheet.GetCells().Get(u"D5").PutValue(2);

    // Create Line Chart: X as Category Axis
    int pieIdx = worksheet.GetCharts().Add(ChartType::LineWithDataMarkers, 6, 15, 20, 21);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$5");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Create XY (Scatter) Chart: X as Value Axis
    pieIdx = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);

    // Retrieve the Chart object
    chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set X values for series
    chart.GetNSeries().Get(0).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(1).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(2).SetXValues(u"{1,3,2.5,3.5}");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"XAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
