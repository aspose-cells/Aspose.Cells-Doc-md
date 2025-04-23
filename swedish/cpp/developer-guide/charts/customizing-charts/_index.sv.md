---
title: Anpassa diagram med C++
linktitle: Anpassa diagram
description: Lär dig hur du anpassar diagram i Aspose.Cells for C++. Vår guide visar hur du ändrar diagramlayout, lägger till och formaterar dataserier, justerar axlar och tillämpar olika formateringsalternativ för att förbättra utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, diagram, anpassning, layouter, dataserier, axlar, formatering, utseende, användbarhet.
type: docs
weight: 40
url: /sv/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **Skapa Anpassade Diagram**

Hittills har vi när vi diskuterat diagram sett på standarddiagram som har sina standardinställningar. Vi definierar bara datakällan, ställer in några få egenskaper, och diagrammet skapas med dess standardformat. Men Aspose.Cells API:er stöder också att skapa anpassade diagram som tillåter utvecklare att skapa diagram med egna formateringsinställningar.

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells.

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av ett [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)-objekt medan ett [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-objekt fungerar som en samling av [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)-objekt. Vid skapandet av ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (insamlade i [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-objekt).

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar pip-, linje-, kolumn- och stapeldiagram, men fler diagram kommer att stödas i framtida versioner.

{{% /alert %}}
