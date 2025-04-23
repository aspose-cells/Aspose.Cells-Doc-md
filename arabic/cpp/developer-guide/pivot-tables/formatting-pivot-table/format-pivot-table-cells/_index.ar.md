---
title: تنسيق خلايا جدول البيانات المحوري باستخدام C++
linktitle: تنسيق خلايا جدول البيانات المحورية
type: docs
weight: 30
url: /ar/cpp/format-pivot-table-cells/
description: تعلم كيفية تنسيق خلايا الجدول المحوري باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، قد ترغب في تنسيق خلايا الجدول المحوري. على سبيل المثال، قد ترغب في تطبيق لون خلفية على خلايا الجدول المحوري. توفر Aspose.Cells طريقتين [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) و [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) يمكنك استخدامهما لهذا الغرض.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) يطبق النمط على الجدول المحوري بالكامل بينما [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) يطبق النمط على خلية واحدة من الجدول المحوري.

{{% /alert %}}

يحمِّل الكود التالي ملف Excel التجريبي (pivot_format.xlsx) الذي يحتوي على جدولين محوريين، ويحقق عملية تنسيق الجدول بالكامل وتنسيق خلايا فردية في الجدول المحوري.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## مقالات ذات صلة

- [تنسيق جدول الجدول المحوري](/cells/ar/cpp/formatting-pivot-table/)
- [العمل مع تنسيقات عرض البيانات لحقل البيانات في الجدول المحوري](/cells/ar/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
