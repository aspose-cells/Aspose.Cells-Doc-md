--- 
title: Erstellen Sie ein Hoch Tief Schluss (HLC) Aktienchart mit C++ 
linktitle: Erstellen eines Hoch Tief Schluss(HLC) Aktiendiagramms 
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ ein Hoch Tief Schluss Aktienchart erstellen. Unser Schritt für Schritt Leitfaden zeigt, wie Sie Börsendaten, einschließlich der Hoch , Tief und Schlusskurse, in ein Diagramm plotten, um eine bessere Analyse und Visualisierung zu ermöglichen. 
keywords: Aspose.Cells for C++, Hoch Tief Schluss Aktienchart, Börsendaten, Analyse, Visualisierung. 
type: docs 
weight: 181 
url: /de/cpp/create-high-low-close-stock-chart/ 
--- 

## **Mögliche Verwendungsszenarien** 
Das Hoch-Tief-Schluss (HLC)-Aktiendiagramm verwendet vier Datenreihen. Die erste Reihe ist in der Regel eine Kategorie, üblicherweise ein Datum, aber auch Aktiennamen können verwendet werden. Die nächsten drei Reihen sind für die Hoch-, Tief- und Schlusskurse vorgesehen. Der Kursbereich für jede Kategorie wird durch eine vertikale Linie von Tief- zu Hochkurs angezeigt, und der Schlusskurs wird durch ein Tickzeichen angezeigt, das sich rechts von dieser Linie erstreckt. 

![todo:image_alt_text](sample.png) 
## **Verbesserungen der Sichtbarkeit im Diagramm** 
Manchmal können wir das Aussehen des Markers (Schlusskurs) anpassen oder ihn auf der sekundären Achse anzeigen, um das Diagramm übersichtlicher zu gestalten. 

![todo:image_alt_text](sample2.png) 
## **Beispielcode** 
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](High-Low-Close.xlsx) und generiert die [Ausgabe-Excel-Datei](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
