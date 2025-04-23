---
title: Amplaufzeitdatum und Aktualisierungsinformationen darüber, wer die Pivot Tabelle aktualisiert hat, mit C++ abrufen
linktitle: Pivot Tabellen Auffragedatum und Aktualisiert von Infos abrufen
type: docs
weight: 100
url: /de/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Lernen Sie, wie Sie das Aktualisierungsdatum und die Information, wer die Pivot Tabelle aktualisiert hat, mit Aspose.Cells und C++ aus einer Arbeitsmappe abrufen.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt nun das Abrufen des Aktualisierungsdatums und der Aktualisierungsinformationen aus einer Arbeitsmappe.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) gibt das Datum an, an dem der PivotTable-Bericht zuletzt aktualisiert wurde. Ebenso gibt die Eigenschaft [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) den Namen des Benutzers an, der den Bericht zuletzt aktualisiert hat. Das folgende Beispiel demonstriert diese Funktion, und die Musterdatendatei kann über den folgenden Link heruntergeladen werden.

[SourcePivotTable.xlsx](77496335.xlsx)

**Beispielcode**

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
