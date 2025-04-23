---
title: إزالة الصفوف المكررة في ورقة عمل باستخدام C++
linktitle: إزالة الصفوف المكررة في ورقة العمل
type: docs
weight: 370
url: /ar/cpp/remove-duplicate-rows-in-a-worksheet/
description: تعلم كيفية إزالة الصفوف المكررة في ورقة عمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

إزالة الصفوف المكررة هي واحدة من الميزات المفيدة في Microsoft Excel. تسمح للمستخدمين بإزالة الصفوف المكررة في ورقة عمل، ويمكنك اختيار الأعمدة التي يجب فحصها لوجود معلومات مكررة.

 يوفر Aspose.Cells طريقة `Cells::RemoveDuplicates()` لهذا الغرض. يمكنك أيضًا ضبط `startRow`، `startColumn`، `endRow`، و `endColumn` لاختيار الأعمدة.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
