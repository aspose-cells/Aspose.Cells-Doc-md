---
title: So erstellen Sie ein Sunburst Diagramm mit C++
description: Erfahren Sie, wie man ein Sunburst Diagramm in Aspose.Cells for C++ erstellt, eine Grafik, die Daten in einem Kreis darstellt. Unser Leitfaden hilft Ihnen, verschiedene Eigenschaften und Formatierungen Ihrer Grafik festzulegen, einschließlich Datenbeschriftungen, Legenden, Farben und mehr.
keywords: Aspose.Cells for C++, Sunburst Diagramm, erstellen, Eigenschaften einstellen, Datenbeschriftungen, Legende, Format, Farbe, Kreis, Datenrendering.
type: docs
weight: 162
url: /de/cpp/creating-sunburst-chart/
---

## **Mögliche Verwendungsszenarien**
Treemaps sind gut zum Vergleichen von Anteilen innerhalb der Hierarchie, jedoch sind Treemap-Diagramme nicht ideal, um hierarchische Ebenen zwischen den größten Kategorien und jedem Datenpunkt darzustellen. Ein Sonnenburst-Diagramm ist hierfür eine deutlich bessere Visualisierung. Das Sonnenburst-Diagramm eignet sich perfekt zur Anzeige hierarchischer Daten. Jede Hierarchieebene wird durch einen Ring oder Kreis dargestellt, wobei der innerste Kreis die Spitze der Hierarchie ist. Ein Sonnenburst-Diagramm ohne hierarchische Daten (eine Ebene von Kategorien) ähnelt einem Donut-Diagramm. Ein Sonnenburst-Diagramm mit mehreren Ebenen zeigt, wie die äußeren Ringe zu den inneren Ringen in Beziehung stehen. Das Sonnenburst-Diagramm ist besonders effektiv, um zu zeigen, wie ein Ring in seine beitragenden Teile zerlegt ist, während ein anderes Hierarchiediagramm, das Treemap-Diagramm, ideal für den Vergleich relativer Größen ist.

![todo:image_alt_text](sample.png)
## **Sonnenstrahlendiagramm**
Nach Ausführen des unten stehenden Codes wird das Sonnenstrahlendiagramm wie unten gezeigt angezeigt.

![todo:image_alt_text](result.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](sunburst.xlsx) und erstellt die [Ausgabedatei Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
