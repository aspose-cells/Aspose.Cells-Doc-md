---
title: Hämta kalkylblad för diagrammet med C++
linktitle: Hämta kalkylbladet för diagrammet
description: Lär dig hur du hämtar kalkylbladet som är kopplat till ett Excel diagram med Aspose.Cells for C++. Vår guide visar hur du får tillgång till kalkylbladet och utför operationer på det för att manipulera diagrammets underliggande data.
keywords: Aspose.Cells for C++, Excel diagram, kalkylblad, datamanipulation, underliggande data, operationer.
type: docs
weight: 1000
url: /sv/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du få åtkomst till ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/). Koden skriver först ut namnet på kalkylbladet, accessar sedan det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen, med hjälp av metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
