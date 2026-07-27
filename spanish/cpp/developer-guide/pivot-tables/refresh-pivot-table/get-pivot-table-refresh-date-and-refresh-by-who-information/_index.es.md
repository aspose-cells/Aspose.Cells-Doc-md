---
title: Obtener la fecha de actualización de la tabla dinámica y quién la actualizó con C++
linktitle: Obtener la fecha de actualización de la tabla dinámica y quién realizó la actualización
type: docs
weight: 100
url: /es/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Aprenda cómo obtener la fecha de actualización y quién realizó la actualización de un libro de trabajo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells ahora admite obtener la fecha de actualización y la información de quién la actualizó desde un libro de trabajo.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) devuelve la fecha en la que se actualizó por última vez el informe de PivotTable. De manera similar, la propiedad [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) devuelve el nombre del usuario que actualizó el informe por última vez. El siguiente ejemplo demuestra esta función, y el archivo de muestra se puede descargar desde el siguiente enlace.

[SourcePivotTable.xlsx](77496335.xlsx)

**Código de Ejemplo**

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
