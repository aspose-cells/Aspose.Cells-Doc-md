---
title: ملائمة الصفوف للعرض مع C++
linktitle: تحجيم الصفوف تلقائيًا للتقديم
type: docs
weight: 130
url: /ar/cpp/autofit-rows-for-rendering/
description: تعلم كيف تقوم بضبط ملائمة الصفوف تلقائيًا لعرضها في ملفات Excel باستخدام Aspose.Cells مع C++.
---

عموما، عندما ترغب في عرض كامل النص في خلية، يمكنك تحجيم الصف في العرض العادي بنسبة تكبير 100% في Microsoft Excel. يسمح ذلك بظهور النص بشكل كامل في العرض العادي، وحتى عند الطباعة أو حفظ الملف كملف PDF، سيتم عرض النص بشكل صحيح.

ومع ذلك، في بعض الحالات، يعمل تحجيم الصف بشكل جيد في العرض العادي، ولكن عند التبديل إلى وضع الطباعة أو حفظ الملف كملف PDF، يتم قص النص. يرجى التحقق من ملف المصدر [Book1.xlsx](Book1.xlsx) واللقطات.

![تم قص النص في عرض الطباعة](text_clipped_in_printview.png)

إذا كنت تريد منع قص النص في ملف PDF الذي تم حفظه، يمكنك ملائمة الصف تلقائيًا باستخدام خيار {AutoFitterOptions.GetForRendering()}) .

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

الآن، لم يتم قص النص في ملف PDF الناتج.

![النص لم يتم قصه في ملف PDF المحفوظ](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="cpp" >}}
