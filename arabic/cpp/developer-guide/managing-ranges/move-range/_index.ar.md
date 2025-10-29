---
title: نطاق نقل خلايا في ورقة العمل باستخدام C++
linktitle: نقل مجموعة من الخلايا في ورقة العمل
type: docs
weight: 370
url: /ar/cpp/move-range-of-cells-in-a-worksheet/
description: تعلم كيفية نقل نطاق من الخلايا في ورقة عمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يوضح هذا المقال كيفية نقل مجموعة من الخلايا في ورقة العمل.

{{% /alert %}}

## **نقل مجموعة من الخلايا في ورقة العمل**
يستخدم الشفرة المثالية ملف قالب لتوضيح المهمة.

**ملف الإدخال**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

يرجى الاطلاع على الملف الناتج التالي بالنطاق A1:B5 المحرك إلى C1:D5.

ملف الإخراج

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
