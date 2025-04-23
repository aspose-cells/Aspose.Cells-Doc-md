---
title: Erstellen Sie ein Volumen Open High Low Close(VOHLC) Aktiendiagramm mit C++
description: Lernen Sie, wie man ein Volumen Open High Low Close Aktien Diagramm mit Aspose.Cells for C++ erstellt. Unser Leitfaden zeigt, wie man Börsendaten, einschließlich Volumen, Eröffnung, Hoch, Tief und Schlusskurse, auf einem Diagramm darstellt, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for C++, Volumen Open High Low Close Diagramm, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 184
url: /de/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das vierte Aktienchart, das wir uns ansehen werden, ist das Volume Open High Low Close-Chart. Hier ist es erneut wichtig zu wiederholen, dass die Daten in der richtigen Reihenfolge vorliegen müssen. Wenn Sie Ihre Datentabelle neu anordnen müssen, tun Sie dies vor dem Erstellen des Charts. Das Chart enthält eine Spalte für Volumen unmittelbar nach der ersten (Kategorie-)Spalte. Die Charts zeigen auf der primären Achse ein SäulenDiagramm für das Volumen, während die Preise auf die sekundäre Achse verschoben werden.

![todo:image_alt_text](data.png)

## **Volume-Open-High-Low-Close (VOHLC) Aktiendiagramm**

![todo:image_alt_text](sample.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Volume-Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
