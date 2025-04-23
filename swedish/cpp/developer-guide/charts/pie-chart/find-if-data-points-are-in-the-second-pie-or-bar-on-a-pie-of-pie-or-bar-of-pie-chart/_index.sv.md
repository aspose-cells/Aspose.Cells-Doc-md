---
title: Hitta om datapunkter finns i den andra tårten eller stolpen på ett Pie of Pie eller Bar of Pie diagram med C++
linktitle: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram
description: Lär dig hur du använder Aspose.Cells for C++ för att avgöra om datapunkter finns i den andra tårten eller stolpen på ett Pie of Pie eller Bar of Pie diagram. Vår guide visar hur man identifierar och får tillgång till sekundärtårten eller stolpen på ett sammansatt diagram, vilket möjliggör effektiv dataanalys och manipulerering.
keywords: Aspose.Cells for C++, Pie of Pie diagram, Bar of Pie diagram, Sekundär tår, Sekundär stolpe, Dataanalys, Datahantering.
type: docs
weight: 180
url: /sv/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Möjliga användningsscenario**
Du kan avgöra om datapoäng i serien finns i den andra tårten på *Pie of Pie*-diagrammet eller i stolpen på *Bar of Pie*-diagrammet med Aspose.Cells. Använd [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) för att fastställa detta.

Ladda ner den [exempelfil i Excel](5115193.xlsx) som används i följande exempelkod och se dess konsoloutput. Om du öppnar [exempelfilen i Excel](5115193.xlsx) hittar du att alla datapunkter som är mindre än 10 finns inuti stapeln på *Stapel av paj*-diagram som också visas i konsoloutputen.

## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**
Följande exempelkod visar hur du tar reda på om datapunkterna finns i den andra pajen eller stapeln på ett *Paj av paj*- eller *Stapel av paj*-diagram.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**
Se följande konsolutskrift som genererats efter körning av ovanstående exempel med [sample excel-fil](5115193.xlsx). Om [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) är **falskt**, är datapunkten inom tårtan, men om den är **sant**, är datapunkten inom stolpen.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
