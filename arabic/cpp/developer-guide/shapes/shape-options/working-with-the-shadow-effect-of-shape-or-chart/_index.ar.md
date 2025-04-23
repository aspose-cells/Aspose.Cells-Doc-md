---
title: العمل مع تأثير الظل للشكل أو المخطط باستخدام C++
linktitle: العمل مع تأثير الظل للشكل أو الرسم البياني
type: docs
weight: 220
url: /ar/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: تعلم كيفية التلاعب بتأثير الظل للأشكال أو المخططات باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 توفر Aspose.Cells الطريقة [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) مع فئة [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) للعمل مع تأثير الظل للأشكال أو المخططات. تحتوي فئة [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) على الخصائص التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

- [الحصول على الزاوية()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [الحصول على التمويه()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [احصل على اللون()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [احصل على المسافة()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [احصل على نوع الإعداد المسبق()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [احصل على الحجم()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [احصل على الشفافية()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **العمل مع تأثير الظل للشكل أو الرسم البياني**
الكود النموذجي التالي يحمّل ملف إكسل المصدر ويصل إلى الشكل الأول في ورقة العمل الأولى ويضبط الخصائص الفرعية لخاصية تأثير الظل ويقوم بعد ذلك بحفظ الملف في ملف الإكسل الناتج.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
