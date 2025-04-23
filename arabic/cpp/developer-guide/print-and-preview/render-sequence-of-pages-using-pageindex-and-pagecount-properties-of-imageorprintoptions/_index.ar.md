---
title: عرض تسلسل الصفحات باستخدام خصائص PageIndex و PageCount لخيارات الصورة والطباعة باستخدام C++
linktitle: عرض تسلسل الصفحات
type: docs
weight: 110
url: /ar/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: عرض تسلسل الصفحات من ملف إكسل إلى صور باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تقديم تسلسل من الصفحات من ملف Excel الخاص بك إلى صور باستخدام Aspose.Cells مع الخصائص [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) و [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). تعتبر هذه الخصائص مفيدة عندما يكون هناك الكثير مثل آلاف الصفحات في ورقة العمل الخاصة بك ولكنك تريد تقديم بعضها فقط. سيوفر هذا الوقت وسيوفر أيضًا استهلاك الذاكرة لعملية التقديم.

## **تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة**

الشفرة العينية التالية تحمل [ملف Excel عيني] (55541781.xlsx) وتقدم الصفحات 4 و 5 و 6 و 7 فقط باستخدام الخصائص [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) و [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). إليك الصفحات المقدمة التي تم إنشاؤها بواسطة الشفرة.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **الكود المثالي**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
