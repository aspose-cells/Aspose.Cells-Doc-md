---
title: Verwalten Sie die Legende der Excel Diagramme mit C++
linktitle: Legende
description: Erfahren Sie, wie Sie Aspose.Cells for C++ effektiv nutzen und Diagrammlegenden in Microsoft Excel anpassen. Unser umfassender Leitfaden erklärt die Funktion der Legende, wie man sie zugreift, ändert und die Visualisierung und Datenverständnis verbessert.
keywords: Aspose.Cells for C++, Diagrammlegenden, Microsoft Excel, Visualisierung, Datenverständnis.
type: docs
weight: 50
url: /de/cpp/chart-legend/
---

## **Legendenoptionen**
Aspose.Cells ermöglicht auch die Verwaltung der Legende eines Diagramms zur Laufzeit. Mit dem [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) Objekt kann die Legende verschoben, aktualisiert und formatiert werden.

|![todo:image_alt_text](chart_legend.png)|

## **Festlegen der Legende des Diagramms**
Die Verwaltung der Legende eines Diagramms mit Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) ist einfach.

Das folgende Code-Snippet zeigt, wie die Legende verwaltet wird:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

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

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Erweiterte Themen**
- [Setzen Sie den Text des Fülls des Diagrammlegendeneintrags auf keinen mithilfe von Aspose.Cells](/cells/de/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
