---
title: الحصول على نطاق الخلايا مع C++
linktitle: الحصول على نطاقات الخلايا
type: docs
weight: 600
url: /ar/cpp/get-cells-range/
description: تعلم كيفية الحصول على نطاق الخلايا من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: الحصول على أقصى نطاق عرض للخلايا، الحصول على أقصى صف للخلايا، الحصول على أقصى صف للبيانات للخلايا، الحصول على أقصى عمود للخلايا، الحصول على أقصى عمود للبيانات للخلايا،
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط للتلاعب ببعض البيانات في ورقة العمل، تحتاج إلى معرفة مدى البيانات للورقة بأكملها. توفر Aspose.Cells هذه الميزة. يوفر Aspose.Cells الخصائص والطرق التالية لمساعدتك في تحقيق أهدافك.
- [**Cells.GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)
- [**Cells.GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/)
- [**Cells.GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)
- [**Cells.GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)
- [**Cells.GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)

## **الحصول على نطاقات الخلايا باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
3. الحصول على الخلايا [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    Range range = cells.GetMaxDisplayRange();

    std::cout << cells.GetMaxRow() << std::endl;
    std::cout << cells.GetMaxDataRow() << std::endl;
    std::cout << cells.GetMaxColumn() << std::endl;
    std::cout << cells.GetMaxDataColumn() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
