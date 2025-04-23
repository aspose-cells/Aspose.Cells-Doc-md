---
title: استخدام الأنماط المدمجة مع C++
linktitle: استخدام الأنماط المدمجة
type: docs
weight: 80
url: /ar/cpp/using-built-in-styles/
description: كود C++ لاستخدام أنماط إكسل المدمجة مع واجهة برمجة التطبيقات Aspose.Cells for C++
keywords: استخدام أنماط إكسل المدمجة بلغة C++، تطبيق الأنماط برمجياً في مفكرة العمل، تطبيق الأنماط المدمجة في مفكرة العمل، برمجة تطبيق الأنماط المدمجة في إكسل، كود C++ لتطبيق الأنماط المدمجة في مفكرة العمل، الكود لتطبيق الأنماط المدمجة في مفكرة العمل، تطبيق الكود الخاص بالأنماط المدمجة في ملف إكسل.
---

{{% alert color="primary" %}}

توفر Aspose.Cells مجموعة هائلة من الأنماط التي يمكن إعادة استخدامها لتنسيق خلية في وثيقة جدول بيانات. يمكننا استخدام الأنماط المدمجة في دفتر العمل الخاص بنا وأيضًا إنشاء أنماط مخصصة.

{{% /alert %}}

## **كيفية استخدام الأنماط المدمجة**

الطريقة [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) والتعداد [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) تجعل من السهل استخدام الأنماط المضمنة. إليك قائمة بجميع الأنماط المضمنة الممكنة:

- TWENTY_PERCENT_ACCENT_1
- TWENTY_PERCENT_ACCENT_2
- TWENTY_PERCENT_ACCENT_3
- TWENTY_PERCENT_ACCENT_4
- TWENTY_PERCENT_ACCENT_5
- TWENTY_PERCENT_ACCENT_6
- FORTY_PERCENT_ACCENT_1
- FORTY_PERCENT_ACCENT_2
- FORTY_PERCENT_ACCENT_3
- FORTY_PERCENT_ACCENT_4
- FORTY_PERCENT_ACCENT_5
- FORTY_PERCENT_ACCENT_6
- SIXTY_PERCENT_ACCENT_1
- SIXTY_PERCENT_ACCENT_2
- SIXTY_PERCENT_ACCENT_3
- أكثر من ستين في المائة
- أكثر من ستين في المائة
- أكثر من ستين في المائة
- لهجة 1
- لهجة 2
- لهجة 3
- لهجة 4
- لهجة 5
- لهجة 6
- سيء
- حساب
- تحقق الخلية
- فاصلة
- فاصلة 1
- عملة
- عملة 1
- نص توضيحي
- جيد
- رأس الجدول 1
- رأس الجدول 2
- HEADER_3
- HEADER_4
- HYPERLINK
- FOLLOWED_HYPERLINK
- INPUT
- LINKED_CELL
- NEUTRAL
- NORMAL
- NOTE
- OUTPUT
- PERCENT
- العنوان
- المجموع
- نص التحذير
- مستوى الصف
- مستوى العمود

## كود C++ لاستخدام الأنماط الداخلية

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
