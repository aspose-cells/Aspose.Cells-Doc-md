---
title: تعطيل التعليقات المكشوفة على مستوى أدنى عند الحفظ إلى HTML باستخدام C++
linktitle: تعطيل التعليقات المكشوفة على مستوى أدنى
type: docs
weight: 20
url: /ar/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: القضاء على التعليقات المكشوفة على مستوى أدنى عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel إلى HTML، يكشف Aspose.Cells عن تعليقات الشرط على مستوى أدنى. هذه التعليقات الشرطية تهم بشكل رئيسي إصدارات أقدم من Internet Explorer ولا تهم المتصفحات الحديثة. يمكنك قراءتها بالتفصيل على الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 يسمح لك Aspose.Cells بالتخلص من هذه التعليقات المكشوفة على مستوى أدنى عن طريق تعيين الخاصية [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

يوضح المثال التالي استخدام خاصية [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/). تُظهر لقطة الشاشة تأثير هذه الخاصية عند عدم تعيينها إلى true. يرجى تنزيل ملف Excel النموذجي [الملف التجريبي](50528257.xlsx) المستخدم في هذا الكود وملف HTML الناتج [المخرجات](50528258.zip) للاطلاع عليهما كمصدر مرجعي.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
