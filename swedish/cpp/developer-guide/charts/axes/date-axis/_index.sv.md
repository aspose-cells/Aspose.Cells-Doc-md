---
title: Datumaxel med C++
linktitle: Datumsaxel
description: Lär dig hur du hanterar datumaxeln i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du arbetar med olika datumformat, tidskalan och klicketikettfrekvenser.
keywords: Aspose.Cells for C++, datumaxel, hantera, datumformat, tidskala, klicketikettfrekvenser.
type: docs
weight: 200
url: /sv/cpp/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från arbetsbladets data som använder datum, och datumen plottas längs den horisontella (kategori) axeln i diagrammet, ändrar Aspose.Cells automatiskt kategoriaxeln till en datum (tids-skala)-axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.Cells grundläggande enheter för datumaxeln baserat på den minsta skillnaden mellan två datum i arbetsbladets data. Till exempel, om du har data för aktiekurser där den minsta skillnaden mellan datum är sju dagar, sätter Aspose.Cells grundenheten till dagar, men du kan ändra grund-enheten till månader eller år om du vill se aktiens utveckling över längre tid.

## **Hantera datumaxeln som Microsoft Excel**
Se följande kodexempel som skapar en ny Excel-fil och placerar diagramvärden i det första arket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
till [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) och ställer sedan in basenheterna till Dagar.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
