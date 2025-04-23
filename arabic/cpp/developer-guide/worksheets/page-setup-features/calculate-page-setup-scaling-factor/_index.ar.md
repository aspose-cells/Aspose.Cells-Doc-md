---
title: حساب مقياس إعداد الصفحة باستخدام C++
linktitle: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/cpp/calculate-page-setup-scaling-factor/
description: يقدم هذا المقال رمز عينة يوضح كيفية استخدام API أو مكتبة C++ لحساب مقياس إعداد الصفحة باستخدام خيار التناسب مع n صفحة عريضة و m طويلة من ورقة عمل Excel برمجياً.
keywords: التناسب مع n صفحة عريضة بواسطة m طويلة في Excel باستخدام C++، حساب مقياس إعداد الصفحة بالـ C++
---

{{% alert color="primary" %}}

عند تعيين تحجيم إعداد الصفحة باستخدام خيار **تناسب عرض صفحة n بارتفاع صفحة m**، يقوم Microsoft Excel بحساب عامل تحجيم إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام خاصية [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/). تعيد هذه الخاصية قيمة من نوع double يمكن تحويلها إلى قيمة نسبية. على سبيل المثال، إذا عادت 0.5 فهذا يعني أن عامل التحجيم هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
