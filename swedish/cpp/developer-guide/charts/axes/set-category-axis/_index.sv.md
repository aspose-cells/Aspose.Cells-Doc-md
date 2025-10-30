---
title: Hur man ställer in kategoriaxeln med C++
linktitle: Hur man ställer in kategori axeln
description: Lär dig hur du ställer in kategoriaxeln i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du definierar kategoriaxelns intervall, justerar dess egenskaper och formaterar dess etiketter.
keywords: Aspose.Cells for C++, kategori axel, inställning, intervall, egenskaper, formatering.
type: docs
weight: 205
url: /sv/cpp/how-to-set-category-axis/
---

## **Möjliga användningsscenario**
Efter att du har skapat ett diagram i ett arbetsblad kan du ställa in kategoriaxeln för det. I denna artikel visar vi hur du ställer in kategoriaxeln för ett Excel-diagram med hjälp av Aspose.Cells och exempel på kod.

## **Stegen i provkod**

1. Skapa en ny arbetsbok.

2. Skapa en ny diagram i den första arbetsbladet.

3. Lägg till några värden i celler i det första arbetsbladet.

4. Nu kan du ställa in kategoriaxeln. Det finns två sätt: med celldata eller med strängar direkt, båda visas i exempel-koden.

5. Ställ in värdeaxeln, spara arbetsboken för att se resultaten.

## **Exempelkod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
