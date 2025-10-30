---
title: Verwaltung der Achsen von Excel Diagrammen mit C++
description: Lernen Sie, wie man die Diagramachse in Aspose.Cells for C++ konfiguriert. Unser Leitfaden zeigt, wie man die primären und sekundären Achsen anpasst, deren Bereiche festlegt und deren Eigenschaften modifiziert, um Ihre Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagramachsen, Konfiguration, primäre Achsen, sekundäre Achsen, Bereich, Eigenschaften.
linktitle: Achsen
type: docs
weight: 50
url: /de/cpp/chart-axes/
---

{{% alert color="primary" %}}

In Excel-Diagrammen gibt es 3 Arten von Achsen:
1. Horizontale (Kategorien-) Achse: X-Achse
1. Vertikale (Wert-) Achse: Y-Achse
1. Tiefe (Serien-) Achse: Z-Achse

{{% /alert %}}

## **Achsenoptionen**
Aspose.Cells ermöglicht auch die Verwaltung der Diagramachse zur Laufzeit. Mit dem [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) Objekt können Sie alle Optionen der Achse wie in Excel ändern.

|![todo:image_alt_text](chart_axes.png)|

## **X- und Y-Achsen verwalten**

In Excel-Diagrammen sind horizontale und vertikale Achsen die beiden beliebtesten Achsen.

Das folgende Codebeispiel zeigt, wie man die Optionen der X- und Y-Achsen festlegt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Fortgeschrittene Themen**
- [Ändern der Richtung der Markierungstexte](/cells/de/cpp/change-tick-label-direction/)
- [Bestimmen Sie, welche Achse im Diagramm existiert](/cells/de/cpp/determine-which-axis-exists-in-the-chart/)
- [Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel](/cells/de/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms](/cells/de/cpp/read-axis-labels-after-calculating-the-chart/)
- [Wie man die Kategorieachse im Excel-Diagramm einstellt](/cells/de/cpp/how-to-set-category-axis/)
{{< app/cells/assistant language="cpp" >}}
