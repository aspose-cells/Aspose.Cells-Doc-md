---
title: Hur man skapar ett tornadodiagram med C++
linktitle: Skapa tornadodiagram
type: docs
weight: 73
url: /sv/cpp/create-tornado-chart/
description: Lär dig hur man skapar ett tornadodiagram med API Aspose.Cells for C++.
keywords: C++ skapa ett tornadodiagram, lägg till ett tornadodiagram, infoga ett tornadodiagram
---

## **Introduktion**
Ett tornado diagram, även känt som en tornado graf eller tornado diagram, är en typ av datavisualisering som ofta används för känslighetsanalys i Excel. Det hjälper dig att förstå effekten av förändrande variabler på ett visst resultat eller en viss effekt.

## **Hur man skapar ett tornado diagram i Excel**
Du kan skapa ett tornado diagram i Excel genom att följa dessa steg:
1. Välj datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplad stolpdiagram. Klicka på det.
<br>
<img src="1.png" width=70% />
2. Ändra Y-axeln: Högerklicka på y-axeln. Klicka på formatera axeln. I etiketter, klicka på etikettposition nedrullningsalternativ och välj Låg element.
<br>
<img src="2.png" width=70% />
3. Välj vilken som helst stapel och gå till formatering. Ange en lämplig luckbredd.
<br>
<img src="3.png" width=70% />
4. Låt oss ta bort minustecknet (-) från tornado diagrammet. Välj x-axeln. Gå till formatering. I axelalternativ, klicka på nummer. I kategori, välj anpassad. I formatkoden skriv ###0,###0. Klicka på lägg till.
<br>
<img src="4.png" width=70% />
5. Klicka på y-axeln och gå till axvalen. I axvalen, markera Kategorier i omvänd ordning.
<br>
<img src="5.png" width=70% />

## **Hur man lägger till ett tornado diagram i Aspose.Cells**
Vänligen se följande kodexempel. Den laddar den [exempelfil i Excel](sample.xlsx) som innehåller viss provdata. Sedan skapas det staplade stolpdiagrammet baserat på den initiala datan och relevanta egenskaper anges. Slutligen sparas arbetsboken till [utmatning XLSX-format](out.xlsx). Följande skärmdump visar tornado diagrammet skapat av Aspose.Cells i den resulterande Excelfilen.
<br>
<img src="6.png" width=70% />

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
