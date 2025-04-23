---
title: Erstellen Sie ein Open Hoch Tief Schluss (OHLC) Aktienchart mit C++
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ ein Open Hoch Tief Schluss Aktienchart erstellen. Unser Leitfaden zeigt, wie Sie Börsendaten, einschließlich Eröffnungs , Hoch , Tief und Schlusskurse, in ein Diagramm plotten, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for C++, Open Hoch Tief Schluss Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 182
url: /de/cpp/create-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das Open-High-Low-Close (OHLC) Diagramm verwendet fünf Datenkategorien in dieser Reihenfolge: Kategorie, Öffnen, Hoch, Tief und Schlusskurs. Die Preisspanne in jeder Kategorie wird erneut durch eine vertikale Linie angezeigt, während die Spanne zwischen Öffnen und Schließen durch eine breitere, freischwebende Leiste angegeben wird. Wenn der Preis in der Kategorie steigt (Schlusskurs höher als Öffnungspreis), wird die Leiste mit einer Farbe gefüllt, während sie bei sinkenden Preisen mit einer anderen Farbe gefüllt wird. Dieser Diagrammtyp wird oft als Candlestick-Diagramm bezeichnet.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Verbesserungen der Sichtbarkeit im Diagramm**
Wir verwenden oft Farben anstelle von Schwarz-Weiß, um steigende und fallende Kurse anzuzeigen. Im ersten Satz von Kerzencharts unten zeigt Rot steigende und Grün fallende Kurse.

![todo:image_alt_text](sample2.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
