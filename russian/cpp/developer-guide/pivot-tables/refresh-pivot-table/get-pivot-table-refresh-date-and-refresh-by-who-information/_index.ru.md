---
title: Получить дату обновления сводной таблицы и информацию о том, кто обновил с помощью C++
linktitle: Получить дату обновления сводной таблицы и информацию о том, кто обновил
type: docs
weight: 100
url: /ru/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Научитесь получать дату обновления и информацию о том, кто обновил, из книги с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells теперь поддерживает получение даты обновления и информации о том, кем она обновлялась из книги.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) возвращает дату последнего обновления отчёта PivotTable. Аналогично, свойство [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) возвращает имя пользователя, который последний обновлял отчёт. Следующий пример демонстрирует эту функцию, и пример файла можно скачать по следующей ссылке.

[SourcePivotTable.xlsx](77496335.xlsx)

**Пример кода**

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
