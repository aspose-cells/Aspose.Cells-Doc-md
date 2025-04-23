---
title: إرسال الشكل أمام أو خلف داخل ورقة العمل باستخدام C++
linktitle: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/cpp/send-shape-front-or-back-inside-the-worksheet/
description: تعلم كيفية تغيير موضع تتابع z للأشكال في ورقة العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تكون هناك أشكال متعددة موجودة في نفس الموقع، يتم تحديد مدى رؤيتها من خلال مواقع ترتيب z الخاص بها. توفر Aspose.Cells الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/)، التي تغير موضع ترتيب z للشكل. إذا كنت ترغب في إرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، وما إلى ذلك. إذا كنت تريد إحضار شكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، وما إلى ذلك.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

يعرض نموذج الكود التالي استخدام الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/). يرجى الاطلاع على ملف إكسل النموذجي [ملف إكسل عينة](50528330.xlsx) المستخدم في الكود و [ملف إكسل الناتج](50528331.xlsx) الذي تم إنشاؤه بواسطة الكود. تظهر لقطة الشاشة تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

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

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
