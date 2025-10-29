---
title: عرض تدرج اللون ل WordArt أثناء تحويل جداول البيانات إلى HTML باستخدام C++
linktitle: عرض تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى صيغة HTML
type: docs
weight: 90
url: /ar/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: تعلم كيفية عرض تدرج اللون ل WordArt أثناء تحويل جداول البيانات إلى HTML باستخدام C++.
---

## **سيناريوهات الاستخدام المحتملة**
قبل Aspose.Cells 17.1، لم تقم Aspose.Cells بعرض تعبئة التدرج لـ word art عند تحويل ملف Excel إلى صيغة HTML. منذ إصدار Aspose.Cells 17.1 ، يتم دعم تعبئة التدرج لكلمة word art. تُظهر الصورة الملتقطة التالية مقارنة التأثير على تعبئة التدرج من خلال تحويل ملف Excel باستخدام Aspose.Cells 17.1 والإصدار الأقدم.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **عرض تعبئة التدرج لكلمة WordArt أثناء تحويل جداول البيانات إلى صيغة HTML**
يقوم الكود العينة التالي بتحويل [ملف إكسل المصدر](22774111.xlsx) إلى [تنسيق صفحة HTML الناتجة](22774109.zip). يحتوي ملف إكسل المصدر على كائن WordArt بتعبئة تدرجية كما هو مبين في الصورة أعلاه.
## **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
