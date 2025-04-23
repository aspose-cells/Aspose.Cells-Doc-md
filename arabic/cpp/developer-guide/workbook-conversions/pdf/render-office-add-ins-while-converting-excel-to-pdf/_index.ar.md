---
title: عرض إضافات Office أثناء تحويل Excel إلى PDF مع C++
linktitle: عرض إضافات Office أثناء تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: تعلم كيفية عرض إضافات Office أثناء تحويل ملفات Excel إلى PDF باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في السابق، لم تكن Aspose.Cells تدعم عرض إضافات Office عند حفظ ملف Excel بصيغة PDF. الآن، تقوم Aspose.Cells بعرضها بشكل صحيح. لست بحاجة إلى استخدام أية طريقة أو خاصية خاصة لعرض الإضافات في PDF الناتج. فقط قم بحفظ ملف Excel بصيغة PDF، وسيتم عرض الإضافات تلقائيًا.

## **تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF**

الكود التالي يحفظ [ملف Excel النموذجي](60489769.xlsx) الذي يحتوي على إضافات Office، يرجى الاطلاع على [ملف PDF الناتج مع الإصدار السابق 17.11](60489770.pdf) و[ملف PDF الناتج مع الإصدار الأحدث 17.12 وما بعد](60489771.pdf). الملف السابق يكون PDF الناتج فارغًا، لكن النسخة الأحدث تظهر الإضافة.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
