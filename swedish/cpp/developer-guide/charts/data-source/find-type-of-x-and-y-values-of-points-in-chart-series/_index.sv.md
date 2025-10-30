---
title: Hitta Typ av X och Y värden för punkter i diagramserie med C++
linktitle: Hitta typ av X och Y värden för punkter i diagramserier
description: Lär dig hur du avgör typen av X och Y värden i diagramseriepunkter med Aspose.Cells for C++. Vår guide förklarar de olika datatyperna och visar hur du får åtkomst till och arbetar med dem i dina diagram.
keywords: Aspose.Cells for C++, diagram, X värden, Y värden, datatyper, åtkomst, arbeten, diagramserier.
type: docs
weight: 150
url: /sv/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**
Ibland vill du veta vilken typ av X- och Y-värden i diagrampunkter i en serie. Aspose.Cells tillhandahåller metoderna `ChartPoint::get_XValueType` och `ChartPoint::get_YValueType` som kan användas för detta ändamål. Observera att du måste anropa `Chart::Calculate()`-metoden innan du kan använda dessa egenskaper effektivt.

## **Hitta typ av X- och Y-värden för punkter i diagramserier**
Följande exempelkod laddar [exempel-Excel-filen](64716905.xlsx) och får tillgång till det första diagrammet i den första arbetsbladet. Den anropar sedan `Chart::Calculate()`-metoden och hittar typen av X- och Y-värden för den första diagrampunkten och skriver ut dem på konsolen. Se konsolutmatningen nedan som en referens.

## **Exempelkod**
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

## **Konsoloutput**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
