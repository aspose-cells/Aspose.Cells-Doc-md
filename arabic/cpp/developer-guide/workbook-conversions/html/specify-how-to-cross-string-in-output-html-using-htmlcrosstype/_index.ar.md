---
title: تحديد كيف يتم تجاوز النص في HTML الناتج باستخدام HtmlCrossType مع C++
linktitle: تحديد HtmlCrossType في HTML الناتج
type: docs
weight: 140
url: /ar/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: تعلم كيفية التحكم في تجاوز النص في HTML باستخدام Aspose.Cells for C++ مع HtmlCrossType.
---

## **سيناريوهات الاستخدام المحتملة**

عند احتواء خلية على نص أو سلسلة أكبر من عرض الخلية، يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة أو غير موجودة. عند حفظ ملف Excel الخاص بك إلى HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). يحتوي على القيم التالية:

- **HtmlCrossType.Default**: عرض مثل برنامج MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتجاوز النص أو سيتم قصه.

- **HtmlCrossType.MSExport**: عرض النص كما في تصدير HTML من برنامج MS Excel.

- **HtmlCrossType.Cross**: عرض النص المتقاطع في ملف الـHTML، سيكون الأداء لإنشاء ملفات HTML الكبيرة أكثر من عشر مرات أسرع من تعيين القيمة على الافتراضي أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض النص فقط ضمن عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](51740732.xlsx) وتخزينه بتنسيق HTML عن طريق تحديد قيم [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) المختلفة. يرجى تنزيل [ملفات HTML الناتجة](51740734.zip) التي تم إنشاؤها باستخدام هذه الشفرة. يحتوي ملف Excel النموذجي على صورة محاطة باللون الأحمر كما هو موضح في لقطة الشاشة التي توضح تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) على HTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
