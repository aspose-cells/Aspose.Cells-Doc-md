---
title: Datenbeschriftungen in Excel Diagrammen mit C++ verwalten
linktitle: Datenbeschriftungen
type: docs
weight: 50
url: /de/cpp/insert-datalabels-to-chart/
description: Erfahren Sie, wie Sie Datenbeschriftungen in Excel Diagrammen effektiv verwalten können, indem Sie Aspose.Cells for C++ verwenden. Unser umfassender Leitfaden deckt verschiedene Verwaltungsaufgaben ab, einschließlich Hinzufügen, Entfernen und Ändern von Beschriftungen, um die Lesbarkeit und Benutzerfreundlichkeit des Diagramms zu verbessern.
keywords: Aspose.Cells for C++, Excel Diagramme, Datenbeschriftungen, Verwaltung, Lesbarkeit, Benutzerfreundlichkeit, Hinzufügen, Entfernen, Ändern.
---

{{% alert color="primary" %}}

Datenbeschriftungen sind ein wichtiger Bestandteil eines Diagramms. Wir können leicht den Wert, Prozentsatz usw. jeder Serie erkennen.

{{% /alert %}}

## **Datenbeschriftungen-Optionen**
Aspose.Cells ermöglicht auch die Verwaltung der Datenbeschriftungen eines Diagramms zur Laufzeit mit dem [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) Objekt. Es ist einfach, Datenbeschriftungen des Diagramms zu verschieben, zu aktualisieren und zu formatieren.

|![todo:image_alt_text](chart_datalabels.png)|

## **Verwalten der Datenbeschriftungen eines Diagramms**
Das Verwalten von Datenbeschriftungen des Diagramms mit Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) ist einfach.

Der folgende Codeausschnitt zeigt, wie DataLabels verwaltet werden können:

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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Fortgeschrittene Themen**
- [Hinzufügen von benutzerdefinierten Beschriftungen zu Datenpunkten in der Serie des Diagramms](/cells/de/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Textumbruch für Datenbeschriftungen des Diagramms deaktivieren](/cells/de/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Ändern der Größe der Datenbeschriftungsform des Diagramms, um den Text anzupassen](/cells/de/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Benutzerdefinierte Datenauswahl im Diagrammpunkt](/cells/de/cpp/rich-text-custom-data-label-of-chart-point/)
- [Festlegen des Formtyps von Datenbeschriftungen des Diagramms](/cells/de/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Anzeigen von Zellenbereichen als Datenbeschriftungen](/cells/de/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
