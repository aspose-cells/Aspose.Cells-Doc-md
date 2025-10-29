---
title: تحديد الأرقام ذات الأهمية للاحتفاظ بها في ملف Excel باستخدام C++
linktitle: تحديد الأرقام المهمة
type: docs
weight: 30
url: /ar/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: تعلم كيف تحدد الأرقام المهمة التي سيتم تخزينها في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

افتراضيًا، يخزن Aspose.Cells 17 رقماً مهمًا لقيم double داخل ملف Excel، على عكس MS-Excel الذي يخزن فقط 15 رقمًا مهمًا. يمكنك تغيير سلوك الافتراضي لـ Aspose.Cells من 17 رقمًا مهمًا إلى 15 باستخدام الخاصية [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/).

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**

يوضح الكود النموذجي التالي كيف يجبر Aspose.Cells على استخدام 15 رقمًا مهمًا عند تخزين قيم double داخل ملف Excel. يرجى التحقق من ملف Excel الناتج [ملف الإخراج](22774105.xlsx). غيّر امتداده إلى .zip وفك ضغطه، وسترى أن 15 رقمًا مهمًا فقط تم تخزينها داخل ملف Excel. يوضح لقطة الشاشة التالية تأثير الخاصية [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) على ملف الإخراج.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
