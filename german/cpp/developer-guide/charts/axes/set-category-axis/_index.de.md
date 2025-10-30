---
title: Wie man die Kategorieachse mit C++ setzt
linktitle: Wie man die Kategorieachse einstellt
description: Lernen Sie, wie Sie die Kategorieachse in Aspose.Cells for C++ setzen. Unser Leitfaden hilft Ihnen, die Definition des Kategorieachsenbereichs, die Anpassung ihrer Eigenschaften und die Formatierung ihrer Beschriftungen zu verstehen.
keywords: Aspose.Cells for C++, Kategorieachse, Einstellen, Bereich, Eigenschaften, Formatierung.
type: docs
weight: 205
url: /de/cpp/how-to-set-category-axis/
---

## **Mögliche Verwendungsszenarien**
Nachdem Sie ein Diagramm in einem Arbeitsblatt erstellt haben, können Sie die Kategorieachse dafür festlegen. In diesem Artikel zeigen wir Ihnen, wie Sie die Kategorieachse für ein Excel-Diagramm mit Aspose.Cells und Beispielcode einstellen.

## **Die Schritte im Beispielcode**

1. Erstellen Sie eine neue Arbeitsmappe.

2. Erstellen Sie ein neues Diagramm im ersten Arbeitsblatt.

3. Fügen Sie einige Werte in Zellen im ersten Arbeitsblatt ein.

4. Jetzt können Sie die Kategorieachse einstellen. Es gibt zwei Möglichkeiten: die Verwendung von Zellendaten oder die direkte Verwendung von Strings, beide im Beispielcode gezeigt.

5. Stellen Sie die Wertachse ein, speichern Sie die Arbeitsmappe, um das Ergebnis zu sehen.

## **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
