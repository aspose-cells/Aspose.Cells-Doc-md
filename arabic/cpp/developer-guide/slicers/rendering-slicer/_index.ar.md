---
title: عرض مقطع التصفح باستخدام C++
type: docs
weight: 40
url: /ar/cpp/rendering-slicer/
description: عرض مقاطع التصفح في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**
تدعم Aspose.Cells عملية عرض شكل قوالب التصفية. إذا قمت بتحويل ورقة العمل الخاصة بك إلى صورة أو حفظ دفتر العمل الخاص بك إلى صيغ PDF أو HTML، سترى أن قوالب التصفية تتم عرضها بشكل صحيح.
## **تقديم المقطع**
يعرض الكود النموذجي التالي ملف Excel نموذج يحتوي على مقطع تصفح موجود. يحول ورقة العمل إلى صورة بضبط منطقة الطباعة التي تغطي مقطع التصفح فقط. الصورة التالية هي الصورة الناتجة التي تظهر مقطع التصفح المعروض. كما ترى، تم عرض مقطع التصفح بشكل صحيح ويبدو كما في ملف Excel النموذجي.

![todo:image_alt_text](rendering-slicer_1)
## **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
