---
title: العمل مع تأثير التوهج للشكل أو المخطط باستخدام C++
linktitle: العمل مع تأثير التوهج الداخلي للشكل أو الرسم البياني
type: docs
weight: 240
url: /ar/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: تعلم كيفية العمل مع تأثير التوهج للأشكال أو المخططات باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 توفر Aspose.Cells الخاصية [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) مع فئة [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) للعمل مع تأثير التوهج للشكل أو المخطط. تحتوي فئة [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) على الخصائص التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **العمل مع تأثير التوهج الداخلي للشكل أو الرسم البياني**
يقوم الكود النموذجي التالي بتحميل ملف إكسل المصدر والوصول إلى الشكل الأول في ورقة العمل الأولى ويضبط الخصائص الفرعية لخاصية [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) ثم يحفظ المصنف في [ملف إكسل الإخراج](5115414.xlsx).

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
