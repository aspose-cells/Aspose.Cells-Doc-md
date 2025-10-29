---
title: الوصول إلى مربع النص باسم باستخدام C++
linktitle: الوصول إلى مربع النص من خلال الاسم
type: docs
weight: 230
url: /ar/cpp/access-the-text-box-by-the-name/
description: تعلم كيفية الوصول إلى مربع نص باسمه باستخدام Aspose.Cells for C++.
---

## الوصول إلى مربع النص بالاسم

في السابق، كان يتم الوصول إلى صناديق النص بالترتيب من مجموعة [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)، لكن الآن يمكنك الوصول أيضًا إلى صندوق النص بالاسم من هذه المجموعة. هذه طريقة مريحة وسريعة للوصول إلى صندوق النص إذا كنت تعرف اسمه بالفعل.

 الشيفرة النموذجية التالية أولاً تنشئ مربع نص وتخصص له نصًا واسمًا. ثم، في الأسطر التالية، نصل إلى نفس مربع النص بواسطة اسمه ونطبع نصه.

### الشيفرة C++ للوصول إلى مربع النص باسمه

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
