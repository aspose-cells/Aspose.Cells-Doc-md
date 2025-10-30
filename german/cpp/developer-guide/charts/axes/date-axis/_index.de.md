---
title: Datum Achse mit C++
linktitle: Datumsachse
description: Lernen Sie, wie man die Datumsachse in Aspose.Cells for C++ verwaltet. Unser Leitfaden hilft Ihnen zu verstehen, wie man mit verschiedenen Datumsformaten, Zeitskalen und Tick Label Frequenzen arbeitet.
keywords: Aspose.Cells for C++, Datumsachse, verwalten, Datumsformate, Zeitskalen, Tick Label Frequenzen.
type: docs
weight: 200
url: /de/cpp/date-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein Diagramm aus Worksheet-Daten erstellen, die Daten verwenden, und die Daten auf der horizontalen (Kategorien-)Achse im Diagramm dargestellt werden, ändert Aspose.Cells die Kategorieachse automatisch in eine Datums- (Zeitmaß-)Achse.
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiswerten an, wie die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in aufeinanderfolgender Reihenfolge oder in den gleichen Basiswerten vorliegen.
Standardmäßig legt Aspose.Cells die Basiseinheiten für die Datumsachse anhand der kleinsten Differenz zwischen zwei Daten in den Arbeitsblattdaten fest. Wenn Sie z.B. Aktienkurse haben, bei denen die kleinste Differenz zwischen Daten sieben Tage beträgt, setzt Aspose.Cells die Grundeinheit auf Tage. Sie können die Grundeinheit jedoch auf Monate oder Jahre ändern, um die Entwicklung der Aktie über einen längeren Zeitraum zu sehen.

## **Behandeln Sie die Datumsachse wie Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und setzen den Typ des [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
auf [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) und setzen dann die Basiswerte auf Tage.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
