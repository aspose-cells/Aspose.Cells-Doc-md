---
title: Pivot Tablo yenileme tarihi ve yenilemeyi yapan kişi bilgisi almak (C++)
linktitle: Pivot Tablo Yenileme Tarihi ve Yenilemeyi Yapan Kişi Bilgisi Alma
type: docs
weight: 100
url: /tr/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Aspose.Cells kullanarak çalışma kitabından yenileme tarihi ve yenilemeyi yapan kişi bilgisini nasıl alacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells şimdi bir çalışma kitabından yenileme tarihi ve son yenileyen bilgisini almayı destekler.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) son güncelleştirilen PivotTable raporunun tarihini döndürür. Benzer şekilde, [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) özelliği raporu en son yenilemiş kullanıcının adını döndürür. Aşağıdaki örnek bu özelliği gösterir ve örnek dosya aşağıdaki bağlantıdan indirilebilir.

[SourcePivotTable.xlsx](77496335.xlsx)

**Örnek Kod**

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
