---
title: So erstellen Sie ein TreeMap Diagramm mit C++
description: Lernen Sie, wie man ein Treemap Diagramm in Aspose.Cells for C++ erstellt. Unser Leitfaden hilft Ihnen, die verschiedenen Eigenschaften und Formatierungsoptionen für Treemap Diagramme zu verstehen, einschließlich Farben, Beschriftungen und Datenrepräsentation.
keywords: Aspose.Cells for C++, Treemap Diagramm, erstellen, Eigenschaften, Formatierung, Farben, Beschriftungen, Datenrepräsentation, Kreisdiagramm, hierarchische Diagrammerstellung.
type: docs
weight: 161
url: /de/cpp/creating-treemap-chart/
---

## **Mögliche Verwendungsszenarien**
Ein Treemap-Chart bietet eine hierarchische Ansicht Ihrer Daten und macht es einfach, Muster zu erkennen, beispielsweise welche Artikel die Bestseller eines Ladens sind. Die Baumzweige werden durch Rechtecke dargestellt und jede Unterzweig wird als kleineres Rechteck angezeigt. Das Treemap-Chart zeigt Kategorien nach Farbe und Nähe an und kann problemlos viele Daten anzeigen, was bei anderen Diagrammtypen schwierig wäre.

![todo:image_alt_text](sample.png)
## **Treemap-Diagramm**
Nach Ausführung des folgenden Codes sehen Sie das Treemap-Diagramm wie unten gezeigt.

![todo:image_alt_text](result.png)
## **Beispielcode**
Der folgende Beispielscode lädt die [Beispieldatei Excel](treemap.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
