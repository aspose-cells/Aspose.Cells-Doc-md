---
title: Hämta ekvationstext för trendlinje i diagram med C++
linktitle: Trendlinjer
description: Lär dig hur du använder Aspose.Cells for C++ för att hämta ekvationstexten för en trendlinje i ett diagram skapat i Microsoft Excel. Vår guide kommer att visa hur du kommer åt och extraherar ekvationen för trendlinjen för vidare analys eller visning.
keywords: Aspose.Cells for C++, Diagramtrendlinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
type: docs
weight: 110
url: /sv/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvations text av diagramtrendlinje med Aspose.Cells. Aspose.Cells tillhandahåller egenskapen [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) som returnerar ekvations texten av diagramtrendlinjen. För att använda denna egenskap måste du först anropa metoden [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Följande skärm visar diagrammet med en trendlinje och dess ekvationstext visas i röd färg. Vi kommer att hämta denna text med hjälp av [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) egenskapen i följande kodexempel.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++-kod för att få ekvationstexten av diagramtrendlinjen

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

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
