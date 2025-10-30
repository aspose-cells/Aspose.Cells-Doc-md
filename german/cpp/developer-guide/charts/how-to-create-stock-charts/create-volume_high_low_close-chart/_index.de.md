---
title: Erstellen Sie ein Volumen Hoch Tief Schluss (VHLC) Aktienchart mit C++
linktitle: Erstellen Sie ein Volumen High Low Close(VHLC) Aktiendiagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ ein Volumen Hoch Tief Schluss Aktienchart erstellen. Unser Leitfaden zeigt, wie Sie Börsendaten, einschließlich Volumen, Hoch , Tief und Schlusskursen, in ein Diagramm plotten, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for C++, Volumen Hoch Tief Schluss Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 183
url: /de/cpp/create-volume-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das dritte Aktien-Diagramm, das wir betrachten werden, ist das Volumen Hoch Tief Schluss Diagramm. Noch einmal ist es wichtig zu wiederholen, dass die Daten in der richtigen Reihenfolge vorliegen müssen. Wenn Sie Ihre Datentabelle neu anordnen müssen, sollten Sie dies tun, bevor Sie Ihr Diagramm erstellen. Dieses Diagramm enthält eine Spalte für das Volumen direkt nach der ersten (Kategorie-)Spalte, und die Diagramme enthalten ein Säulendiagramm auf der primären Achse, das dieses Volumen zeigt, während die Preise auf die sekundäre Achse verschoben werden.

![todo:image_alt_text](data.png)
## **Volume-High-Low-Close (VHLC) Aktiendiagramm**

![todo:image_alt_text](sample.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Volume-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


{{< app/cells/assistant language="cpp" >}}
