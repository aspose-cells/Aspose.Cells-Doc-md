---
title: Z Achse mit C++
linktitle: Z Achse
description: Lernen Sie, wie Sie mit der Z Achse in Aspose.Cells for C++ arbeiten. Unser Leitfaden hilft Ihnen, die Z Achse zu konfigurieren und anzupassen, einschließlich ihrer Skala und Beschriftungen, um Ihre Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Z Achse, Diagrammerstellung, Konfiguration, Anpassung, Skala, Beschriftungen.
type: docs
weight: 210
url: /de/cpp/z-axis/
---

## **Mögliche Verwendungsszenarien**
Für einige 3-D-Diagramme wie 3-D-Säulen, 3-D-Kegel oder 3-D-Pyramiden, die eine Tiefenachsen (Reihenachsen) haben, auch bekannt als Z-Achse, die Sie ändern können. Sie können das Intervall zwischen den Tickmarken, Achsenbeschriftungen und anderen Operationen festlegen.

## **Behandeln Sie die primäre und sekundäre Achse wie in Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. Dann fügen wir ein Diagramm hinzu und setzen den Diagrammtyp auf Column3D, dabei sehen Sie auch die Z-Achse, auch Tiefenachse genannt. 

![todo:image_alt_text](excel.png)

## **Beispielcode**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
