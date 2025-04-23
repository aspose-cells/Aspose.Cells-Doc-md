---
title: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML مع C++
linktitle: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/cpp/enable-css-custom-properties-while-saving-to-html/
description: تعلم كيف تمكّن خصائص CSS المخصصة عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for C++. تحسين الأداء من خلال تقليل بيانات الصورة الزائدة.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML، وفي حالة وجود تكرارات متعددة لصورة base64 واحدة، مع الخاصية المخصصة، يحتاج البيانات لمرَّة واحدة فقط، مما يُحسّن أداء HTML الناتج. يرجى استخدام الخاصية [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) وتعيينها إلى **true** عند الحفظ إلى HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML**

يوضح المثال التالي استخدام الخاصية [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/). تُظهر لقطة الشاشة تأثير هذه الخاصية عند عدم تعيينها إلى **true**. يرجى تنزيل ملف Excel التجريبي [الملف](50528260.xlsx) المستخدم في هذا الكود وملف HTML المخرج [الملف](50528261.zip) للاطلاع عليه كمصدر مرجعي.

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
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
