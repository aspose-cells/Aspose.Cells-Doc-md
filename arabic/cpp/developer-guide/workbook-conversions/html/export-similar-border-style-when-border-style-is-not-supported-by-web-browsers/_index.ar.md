---
title: تصدير نمط حدود مشابه عند عدم دعم نمط الحدود من قبل متصفحات الويب باستخدام C++
linktitle: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب
type: docs
weight: 70
url: /ar/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: تعلم كيف تقوم بتصدير أنماط حدود مماثلة عند عدم دعمها بواسطة متصفحات الويب باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Microsoft Excel بعض أنواع الحدود المتقطعة التي لا يدعمها متصفحات الويب. عند تحويل ملف إكسل من نوع HTML باستخدام Aspose.Cells، تتم إزالة هذه الحدود. ومع ذلك، يدعم Aspose.Cells أيضًا عرض هذه الحدود مع الخاصية [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/). الرجاء تعيين قيمتها إلى **صحيح** وسيتم تصدير هذه الحدود غير المدعومة أيضًا إلى ملف HTML.

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**

يحمِّل رمز النموذج التالي ملف إكسل النموذجي (64716806.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة أدناه. توضح لقطة الشاشة أيضًا تأثير الخاصية [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/) داخل ملف HTML الإخراجي (64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
