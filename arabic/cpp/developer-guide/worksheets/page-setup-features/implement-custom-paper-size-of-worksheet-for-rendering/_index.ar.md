---
title: تنفيذ حجم ورق مخصص للورقة للعملية الطباعة باستخدام C++
linktitle: تنفيذ حجم ورق مخصص لورقة العمل للتقديم
type: docs
weight: 70
url: /ar/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: توضح هذه المقالة كيفية استخدام واجهة برمجة التطبيقات لـ C++ لضبط حجم ورق مخصص للورقة العمل عند التحويل من Excel إلى PDF برمجيًا.
keywords: تعيين حجم ورق مخصص أثناء تحويل Excel إلى PDF باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

لا يتوفر خيار مباشر لإنشاء أحجام ورق مخصصة في MS Excel؛ ومع ذلك، يمكنك تعيين حجم ورق مخصص للورقة العمل عند تصدير ملفات Excel إلى صيغة PDF. يشرح هذا المستند كيفية تعيين حجم ورق مخصص لورقة عمل باستخدام واجهات Aspose.Cells.

## **تنفيذ حجم ورق مخصص لورقة العمل للتقديم**

تسمح Aspose.Cells بتنفيذ حجم ورق مخصص للورقة العمل. يمكنك استخدام طريقة [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) من فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) لتحديد حجم صفحة مخصص. يوضح الكود النموذجي التالي كيفية تحديد حجم ورق مخصص لورقة العمل الأولى في دفتر العمل. يرجى أيضًا مراجعة [الإخراج PDF](45056028.pdf) الذي تم توليده باستخدام الكود التالي للمراجعة.

## **لقطة شاشة**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
