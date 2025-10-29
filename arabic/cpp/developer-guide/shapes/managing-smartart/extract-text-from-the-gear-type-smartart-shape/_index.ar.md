---
title: استخراج النص من شكل فن ذكي من نوع الترس باستخدام C++
linktitle: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 500
url: /ar/cpp/extract-text-from-the-gear-type-smartart-shape/
description: تعلم كيفية استخراج النص من أشكال فن ذكي من نوع الترس في إكسل باستخدام Aspose.Cells for C++ مع إرشادات خطوة بخطوة وأمثلة على الشيفرة.
---

## **سيناريوهات الاستخدام المحتملة**

 يمكن لـ Aspose.Cells for C++ استخراج النص من شكل فن ذكي من نوع الترس. لتحقيق ذلك، اتبع الخطوات التالية:
1. تحويل شكل الفن الذكي إلى شكل مجموعة باستخدام طريقة [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4).
2. استرجاع جميع الأشكال الفردية التي تشكل شكل المجموعة باستخدام طريقة [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
3. التكرار عبر كل شكل فردي واستخراج النص باستخدام طريقة [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **استخراج النص من شكل SmartArt نوع الحركة**

الشيفرة النموذجية التالية تقوم بتحميل [ملف إكسل نموذج](67338483.xlsx) يحتوي على شكل فن ذكي من نوع الترس وتستخرج النص من أشكاله الفردية. يرجى مراجعة مخرجات وحدة التحكم أدناه للنتائج.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
