---
title: Finden Sie den Typ der X und Y Werte von Punkten in Diagrammserien mit C++
linktitle: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
description: Erfahren Sie, wie Sie den Typ der X und Y Werte in Diagrammserienpunkten mit Aspose.Cells for C++ bestimmen. Unser Leitfaden erklärt die verschiedenen Datentypen und zeigt, wie Sie auf diese zugreifen und sie in Ihren Diagrammen verwenden.
keywords: Aspose.Cells for C++, Diagrammerstellung, X Werte, Y Werte, Datentypen, Zugriff, Arbeiten mit, Diagrammserien.
type: docs
weight: 150
url: /de/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie den Typ der X- und Y-Werte eines Diagrammpunkts in einer Serie wissen. Aspose.Cells bietet die Methoden `ChartPoint::get_XValueType` und `ChartPoint::get_YValueType` an, die hierfür verwendet werden können. Bitte beachten Sie, dass Sie die Methode `Chart::Calculate()` aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**
Der folgende Beispielcode lädt die [Beispieldatei](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Dann ruft er die `Chart::Calculate()`-Methode auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie in der Konsole aus. Siehe unten die Konsolenausgabe zur Referenz.

## **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
