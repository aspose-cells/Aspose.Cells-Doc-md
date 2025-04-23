---
title: Primäre und Sekundäre Achse mit C++
linktitle: Primäre und sekundäre Achse
description: Lernen Sie, wie Sie Primär und Sekundärachsen in Aspose.Cells for C++ verstehen und damit arbeiten. Unser Leitfaden hilft Ihnen, die Unterschiede zwischen primären und sekundären Achsen zu verstehen, sowie sie effektiv in Ihren Diagrammen zu konfigurieren und zu verwenden.
keywords: Aspose.Cells for C++, primäre Achsen, sekundäre Achsen, Verständnis, Unterschiede, Konfiguration, Nutzung.
type: docs
weight: 190
url: /de/cpp/primary-and-second-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn die Zahlen in einem Diagramm von Datenreihen zu Datenreihen stark variieren oder wenn verschiedene Arten von Daten (Preis und Volumen) vorliegen, platzieren Sie eine oder mehrere Datenreihen auf einer sekundären vertikalen (Wert-) Achse. Die Skala der sekundären vertikalen Achse zeigt die Werte für die zugehörigen Datenreihen an. Eine sekundäre Achse funktioniert gut in einem Diagramm, das eine Kombination aus Säulen- und Liniendiagrammen zeigt.

## **Behandeln Sie die primäre und sekundäre Achse wie in Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und zeigen die zweite Achse.

![todo:image_alt_text](excel.png)

## **Beispielcode**
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
