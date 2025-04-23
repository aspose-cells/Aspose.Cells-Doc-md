---
title: Lägga till och ta bort Query Table i arbetsblad med C++
linktitle: Läsning och skrivning av frågetabell i arbetsblad
type: docs
weight: 40
url: /sv/cpp/reading-and-writing-query-table-of-worksheet/
description: Lär dig hur man läser och skriver Query tabeller i Excel ark med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller `Worksheet.QueryTables`-samlingen, som returnerar ett objekt av typen `QueryTable` efter index. Den har följande två egenskaper:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Båda är boolean-värden. Du kan visa dem i Microsoft Excel via **Data > Anslutningar > Egenskaper**.

{{% /alert %}}

## Läsning och skrivning av frågetabell i arbetsblad

Följande exempelkod läser den första `QueryTable` i det första arbetsbladet och skriver ut båda QueryTable-egenskaperna. Sedan sätter den `QueryTable.PreserveFormatting` till `true`.

Du kan ladda ned den angivna källfilen Excel som används i koden och den genererade utdatafilen Excel med hjälp av följande länkar.

- [Käll-Excel-fil](5115533.xlsx)
- [Utdata-Excel-fil](5115537.xlsx)

```c++
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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Konsolutfall

Här är konsolutmatningen för ovanstående exempel:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Hämta resultatområde för Query Table

Aspose.Cells ger möjlighet att läsa adressen (dvs. resultatområdet av celler) för en query table. Följande kod visar denna funktion genom att läsa resultatområdets adress för en query table. Exempelfilen kan laddas ner [här](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
