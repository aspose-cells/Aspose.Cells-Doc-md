---
title: Läsa och skriva tabell med frågetabell datakälla med C++
linktitle: Läs och skriv tabell med datakälla för frågetabell
type: docs
weight: 30
url: /sv/cpp/read-and-write-table-with-query-table-data-source/
description: Lär dig hur du läser och skriver tabeller med QueryTable som datakälla med Aspose.Cells for C++.
---

## **Läs och skriv tabell med datakälla för frågetabell**
 Med Aspose.Cells kan du läsa och skriva en tabell som har en QueryTable som datakälla. Stödet för denna funktion finns även för XLS-filer. Följande kodsnutt demonstrerar att läsa och skriva en sådan tabell genom att först läsa tabellen och sedan modifiera den för att lägga till totalraden.

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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Käll- och utdata Excel-filer är bifogade för referens.

[Källfil](96928091.xls)

[Resultatfil](96928092.xls)
