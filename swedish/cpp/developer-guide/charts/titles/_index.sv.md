---
title: Hantera titlar på Excel diagram med C++
linktitle: Titlar
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till och formatera diagram och axeltitlar i Microsoft Excel. Vår guide kommer att visa hur man ställer in olika typer av titlar, justerar deras utseende och ändrar axeltitlar för bättre datarepresentation och tydlighet.
keywords: Aspose.Cells for C++, Diagramtitlar, Axeltitlar, Microsoft Excel, Datarepresentation, Utseende.
type: docs
weight: 50
url: /sv/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

I Excel-diagram finns det 2 typer av titlar:
1. Diagramtitel 
1. Axeltitlar

{{% /alert %}}

## **Tillval för titlar**
Aspose.Cells tillåter dig också att hantera diagramtitlar i realtid. Med [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) objektet kan du ändra text, teffont och fyllnadsformat för titlar.

|![todo:image_alt_text](chart_title.png)|

## **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att ställa in titlar för ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells tillåter också utvecklare att ställa in diagram- och axeltitlar vid körning. Alla diagram och deras axlar innehåller en [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) egenskap som kan användas för att ställa in deras titlar, som visas i exemplet nedan.

Följande kodexempel visar hur man sätter titlar för diagram och axlar.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

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

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avancerade ämnen**
- [Läs diagramunderrubrik från ODS-fil](/cells/sv/cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="cpp" >}}
