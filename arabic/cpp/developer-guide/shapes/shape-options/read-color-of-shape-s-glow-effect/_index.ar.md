---
title: قراءة لون تأثير التوهج للشكل باستخدام C++
linktitle: قراءة لون تأثير إضاءة الشكل
type: docs
weight: 330
url: /ar/cpp/read-color-of-shape-s-glow-effect/
description: تعلم كيفية قراءة لون تأثير التوهج لأي شكل باستخدام Aspose.Cells for C++.
---

## سيناريوات الاستخدام المحتملة

إذا كنت ترغب في قراءة لون تأثير الإضاءة لأي شكل، يرجى استخدام الخاصية [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/). ستساعدك في العثور على الخصائص المتعلقة بلون تأثير الإضاءة للشكل.

## قراءة لون تأثير الإضاءة للشكل

يرجى الاطلاع على الكود النموذجي التالي و[ملف الإكسل الأصلي](22774108.xlsx) وإخراج الكونسول للرجوع إلى. تظهر اللقطة الشاشة التالية تأثير الاضاءة للشكل داخل ملف الإكسل الأصلي عند عرضه في Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## رمز C++ لقراءة لون تأثير توهج الأشكال

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);
    Shape shape = sheet.GetShapes().Get(0);
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    Color clr = color.GetColor();
    uint32_t argb = (static_cast<uint32_t>(clr.a) << 24) | 
                    (static_cast<uint32_t>(clr.r) << 16) | 
                    (static_cast<uint32_t>(clr.g) << 8) | 
                    static_cast<uint32_t>(clr.b);

    std::cout << "Color: " << argb << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## مخرج الكونسول

إليك إخراج الكونسول للرمز النموذجي أعلاه عند تنفيذه مع [ملف الإكسل الأصلي](22774108.xlsx) المقدم.

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
