---
title: Hämta pivot tabellens uppdateringsdatum och vem som uppdaterade den med C++
linktitle: Hämta pivot tabellens uppdateringsdatum och vem som uppdaterade den
type: docs
weight: 100
url: /sv/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Lär dig hur man hämtar uppdateringsdatum och vem som uppdaterade en arbetsbok med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder nu hämtning av uppdateringsdatum och information om vem som uppdaterade från en arbetsbok.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) visar datumet då PivotTable-rapporten senast uppdaterades. På samma sätt returnerar [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/)-egenskapen namnet på användaren som senast uppdaterade rapporten. Följande exempel illustrerar denna funktion, och exempel-Filen kan laddas ner från följande länk.

[SourcePivotTable.xlsx](77496335.xlsx)

**Exempelkod**

```cpp
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

std::string Date_To_String(const Aspose::Cells::Date& date) {
    char buffer[100];
    snprintf(buffer, sizeof(buffer), "%04d-%02d-%02d %02d:%02d:%02d",
             date.year, date.month, date.day, date.hour, date.minute, date.second);
    return buffer;
}

std::string convert_u16_to_string(const char16_t* str) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(str);
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sourcePivotTable.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    std::cout << "Pivot table refresh by who = " << convert_u16_to_string(pivotTable.GetRefreshedByWho().GetData()) << std::endl;

    std::cout << "Pivot table refresh date = " << Date_To_String(pivotTable.GetRefreshDate()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
