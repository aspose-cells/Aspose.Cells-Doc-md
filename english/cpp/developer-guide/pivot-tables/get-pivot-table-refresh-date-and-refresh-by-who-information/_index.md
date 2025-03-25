---
title: Get Pivot Table refresh date and refresh by who information with C++
linktitle: Get Pivot Table Refresh Date and Refresh By Who Information
type: docs
weight: 100
url: /cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Learn how to fetch the refresh date and refresh by who information from a workbook using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Aspose.Cells now supports fetching the refresh date and refresh by who information from a workbook.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) returns the date on which the PivotTable report was last refreshed. Similarly, [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) property returns the name of the user who refreshed the report last time. The following example demonstrates this feature, and the sample file can be downloaded from the following link.

[SourcePivotTable.xlsx](77496335.xlsx)

**Sample Code**

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