---
title: الحصول على تاريخ تحديث الجدول المحوري ومعلومات من قام بالتحديث باستخدام C++
linktitle: الحصول على تاريخ تحديث الجدول المحوري ومعلومات من قام بالتحديث
type: docs
weight: 100
url: /ar/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: تعلم كيفية جلب تاريخ التحديث ومعلومات من قام بالتحديث من دفتر العمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

Aspose.Cells الآن تدعم الحصول على تاريخ التحديث ومعلومات من يقوم بالتحديث من صفحة العمل.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) يعرض التاريخ الذي تم تحديث تقرير جدول PivotTable آخر مرة. بالمثل، تعيد خاصية [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) اسم المستخدم الذي قام بتحديث التقرير آخر مرة. يوضح المثال التالي هذه الميزة، ويمكن تحميل الملف النموذجي من الرابط التالي.

[SourcePivotTable.xlsx](77496335.xlsx)

**كود عينة**

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
