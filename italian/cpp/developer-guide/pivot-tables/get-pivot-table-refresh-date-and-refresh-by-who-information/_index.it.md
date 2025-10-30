---
title: Ottieni la data di aggiornamento e le informazioni su chi ha aggiornato la pivot table con C++
linktitle: Ottieni la data di aggiornamento della pivot table e le informazioni su chi ha aggiornato
type: docs
weight: 100
url: /it/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Impara come recuperare la data di aggiornamento e le informazioni su chi ha aggiornato da un workbook usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta ora l'ottenimento della data di aggiornamento e dell'informazione sull'aggiornamento di un documento di lavoro.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) restituisce la data dell'ultimo aggiornamento del report PivotTable. Analogamente, la proprietà [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) restituisce il nome dell'utente che ha aggiornato il report per l'ultima volta. L'esempio seguente dimostra questa funzionalità, e il file di esempio può essere scaricato dal seguente link.

[SourcePivotTable.xlsx](77496335.xlsx)

**Codice di Esempio**

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
