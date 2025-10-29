---
title: عرض الأحرف التكميلية يونيكود في ملف PDF الناتج باستخدام C++ بواسطة Aspose.Cells
linktitle: عرض أحرف يونيكود التكميلية
type: docs
weight: 350
url: /ar/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: تعلم كيفية عرض أحرف يونيكود التكميلية في ملف PDF الناتج باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

الحروف اليونيكود العادية طول كل منها 2 بايت بينما الحروف اليونيكود الأعلى طول كل منها 4 بايت. Aspose.Cells الآن يدعم تقديم هذه الحروف اليونيكود الأعلى بطول 4 بايت.

في معيار الحروف اليونيكود، الحروف الأعلى هي الحروف التي تم تخصيص نقاط الرموز لها من U+10000 إلى U+10FFFF. وبمعنى آخر، هذه هي الحروف اليونيكود التي تكون أكبر من U+FFFF.

- في UTF-8 طول كل من هذه الحروف هو 4 بايت.
- في UTF-16، هذه الحروف تتطلب 2 حروف دعائية (وحدات بت بطول 16).

{{% /alert %}}

## تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells

تظهر اللقطة الشاشة التالية كيف قدمت Aspose.Cells [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf). كما يمكنك رؤية تم تقديم كل الحروف اليونيكود الأعلى الثلاثة بالضبط كما فعله Microsoft Excel.

![todo:image_alt_text](output.png)

## كود عينة

يمكنك استخدام هذا الكود العيني لتحويل [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf).

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
