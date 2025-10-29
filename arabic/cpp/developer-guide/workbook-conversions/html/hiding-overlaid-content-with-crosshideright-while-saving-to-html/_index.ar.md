---
title: إخفاء المحتوى المتداخل باستخدام CrossHideRight عند الحفظ إلى HTML باستخدام C++
linktitle: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: استخدم CrossHideRight مع Aspose.Cells في C++ لإخفاء المحتوى المتداخل عند الحفظ إلى HTML.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML، يمكنك تحديد أنواع تقاطع مختلفة لنصوص الخلايا. بشكل افتراضي، يُولد Aspose.Cells HTML حسب Microsoft Excel، ولكن عندما تغير نوع التقاطع إلى [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)، فإنه يخفي جميع النصوص على الجانب الأيمن من الخلية التي تتداخل أو تتداخل مع نص الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمِّل رمز النموذج التالي ملف إكسل النموذجي (64716894.xlsx) ويحفظه إلى [الإخراج HTML](64716893.zip) بعد تعيين [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) إلى [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). يوضح لقطة الشاشة كيف يؤثر [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) على الإخراج HTML من الإخراج الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
