---
title: العمل مع تأثير الانعكاس للشكل أو المخطط باستخدام C++
linktitle: العمل مع تأثير الانعكاس الداخلي للشكل أو الرسم البياني
type: docs
weight: 210
url: /ar/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: تعلم كيفية العمل مع تأثير الانعكاس للأشكال أو المخططات باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**
 توفر Aspose.Cells الخاصية [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) مع فئة [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) للعمل مع تأثير الانعكاس للشكل أو المخطط. تحتوي فئة [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) على الخصائص التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

- [الضباب](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [اتجاه](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [المسافة](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [اتجاه التلاشي](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [التدوير مع الشكل](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [الحجم](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [الشفافية](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [النوع](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **العمل مع تأثير الانعكاس للشكل أو الرسم البياني**
يقوم الكود النموذجي التالي بتحميل ملف إكسل المصدر والوصول إلى الشكل الأول في ورقة العمل الافتراضية ويضبط خصائص مختلفة من فئة [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) ثم يحفظ المصنف في [ملف إكسل الإخراج](5115423.xlsx).

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

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
