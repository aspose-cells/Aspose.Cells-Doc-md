---
title: التحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom باستخدام C++
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم فحص تنسيقات الأرقام المخصصة عند التنسق. ستوضح لك هذه المقالة كيفية استخدام مكتبة Aspose.Cells للتحقق من تنسيقات الأرقام المخصصة لضمان صحة التنسق.
keywords: مكتبة Aspose.Cells، مكتبات C++، جداول البيانات، التنسق، تنسيق الأرقام المخصصة، التحقق، التحقق من الصحة
type: docs
weight: 170
url: /ar/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)، فلن ترمي مكتبة Aspose.Cells استثناءً. ولكن إذا كنت تريد أن تتحقق Aspose.Cells مما إذا كان التنسيق المخصص المعين صالحًا أم لا، يرجى ضبط الخاصية [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) على **true**.

## **فحص تنسيق الرقم المخصص عند ضبط خاصية Style.Custom**

يُظهر نموذج الشفرة التالي تعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). بما أننا قمنا بالفعل بضبط الخاصية [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) على **true**، فإنه يرمي استثناءً، مثلاً، صيغة رقم غير صالحة. اقرأ التعليقات داخل الشفرة للمساعدة.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
