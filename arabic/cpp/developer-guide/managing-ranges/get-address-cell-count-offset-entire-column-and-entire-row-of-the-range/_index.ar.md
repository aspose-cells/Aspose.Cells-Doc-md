---
title: الحصول على عنوان، عدد الخلايا، الإزاحة، العمود بالكامل، والصف الكامل للنطاق باستخدام C++
linktitle: الحصول على عنوان، عدد الخلايا، الإزاحة، العمود بالكامل، والصف الكامل للنطاق
type: docs
weight: 330
url: /ar/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: تعلم كيفية الحصول على العنوان، وعدد الخلايا، والإزاحة، والعمود الكامل، والصف الكامل لنطاق باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
توفر Aspose.Cells كائن `Range` الذي يمتلك طرق أدوات متنوعة تسهل العمل مع نطاقات Excel. توضح هذه المقالة استخدام الطرق أو الخصائص التالية لكائن `Range`:

- **العنوان**

  يحصل على عنوان النطاق.

- **عدد الخلايا**

  يحصل على إجمالي عدد الخلايا في النطاق.

- **الإزاحة**

  يحصل على نطاق بواسطة الإزاحة.

- **العمود الكامل**

  يحصل على كائن `Range` يمثل العمود بالكامل (أو الأعمدة) التي يحتويها النطاق المحدد.

- **الصف الكامل**

  يحصل على كائن `Range` يمثل الصف الكامل (أو الصفوف) الذي يحتوي على النطاق المحدد.

## **احصل على عنوان، عدد الخلايا، الإزاحة، العمود الكامل، والصف الكامل للنطاق**
الرمز النموذجي التالي يوضح استخدام الطرق والخصائص التي نوقشت أعلاه. يرجى مراجعة الإخراج الخاص بالرمز أدناه للمرجعية.

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
