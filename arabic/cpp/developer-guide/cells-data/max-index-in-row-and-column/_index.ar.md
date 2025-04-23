---
title: الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود باستخدام ++C
linktitle: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/cpp/get-max-index-in-row-and-column/
description: تعرف على كيفية الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود من خلال API Aspose.Cells for C++.
keywords: الحصول على مؤشر العمود الأقصى في الصف، الحصول على مؤشر الصف الأقصى في العمود، الحصول على مؤشر البيانات العمود الأقصى في الصف، الحصول على مؤشر بيانات الصف الأقصى في العمود.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى تعديل بعض البيانات على الصفوف أو الأعمدة، تحتاج إلى معرفة نطاق البيانات للصفوف والأعمدة. يوفر Aspose.Cells هذه الميزة. للحصول على أقصى فهرس عمود في صف، يمكنك الحصول على خصائص [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) و [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)، ثم استخدام خاصية [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) للحصول على أقصى فهرس عمود وأقصى فهرس عمود بيانات. ولكن للحصول على أقصى فهرس صف وأقصى فهرس بيانات صف في العمود، عليك إنشاء نطاق على العمود، ثم تصفح النطاق للعثور على آخر خلية، وأخيرًا الحصول على الخاصية [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) في الخلية.

Aspose.Cells توفر الخصائص والأساليب التالية للمساعدة في تحقيق أهدافك.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **الحصول على مؤشر العمود الأقصى في الصف ومؤشر الصف الأقصى في العمود باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. الحصول على خاصية [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) في الخلية.
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. الحصول على خاصية [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) في الخلية.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
