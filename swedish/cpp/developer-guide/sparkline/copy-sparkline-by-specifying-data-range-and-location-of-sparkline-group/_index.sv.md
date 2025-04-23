---
title: Kopiera Sparkline genom att specificera dataområde och plats för Sparkline grupp med C++
linktitle: Kopiera Sparkline genom att specificera dataområde och plats
type: docs
weight: 300
url: /sv/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Lär dig hur du kopierar sparklines genom att specificera dataområde och plats med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel tillåter dig att kopiera en sparkline genom att ange dataområde och plats för en sparklinegrupp. Aspose.Cells stöder denna funktion.

{{% /alert %}}

För att kopiera en sparkline till andra celler i Microsoft Excel:

1. Välj cellen som innehåller sparklinen.
2. Välj **Redigera data** från **Sparkline**-avsnittet på fliken **Design**.
3. Välj **Redigera gruppplats och data**.
4. Ange dataområdet och platsen.
1. Klicka på **OK**.

Aspose.Cells tillhandahåller metoden `SparklineCollection.Add(dataRange, row, column)` för att specificera ett sparklines dataområde och plats. Följande exempel kod laddar källfilen i Excel som visas i skärmbilden ovan, nås den första sparklinesgruppen och lägger till dataområden och platser i sparklinesgruppen. Slutligen skriver den utdatafilen till disk som också visas i skärmbilden ovan.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
