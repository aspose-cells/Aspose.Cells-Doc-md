---
title: تعطيل CSS أثناء الحفظ إلى HTML باستخدام C++
linktitle: تعطيل CSS عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/cpp/disable-css-while-saving-to-html/
description: تعلم كيفية تعطيل CSS أثناء حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى صفحة HTML واحدة، عادةً ستكون عناصر CSS مضمنة داخل ملف HTML وتقع في قسم HEAD. إذا أرفقت هذا الملف كمحتوى/جسم لبريد إلكتروني، ستتم إزالة عناصر CSS بواسطة معظم عملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. الإصدار 24.12 من Aspose.Cells يقدم خيارًا يسمح لك بتعطيل CSS بشكل اختياري، مما يتيح تطبيق الأنماط مباشرة داخل عناصر HTML نفسها. إذا كنت ترغب في تعيين HTML كمحتوى/جسم البريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) وتعيينها إلى **true**.

## **تعطيل CSS عند الحفظ إلى HTML**

يزودك المثال التالي بكود يوضح استخدام الخاصية [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/).

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
