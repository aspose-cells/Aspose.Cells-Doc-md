---
title: Läs färgen på formens glödeffekt med C++
linktitle: Läs färgen för formens glow effekt
type: docs
weight: 330
url: /sv/cpp/read-color-of-shape-s-glow-effect/
description: Lär dig hur man läser färgen på glödeffekten för vilken form som helst med Aspose.Cells for C++.
---

## Möjliga användningsfall

Om du vill läsa färgen på ljuseffekten hos någon form, använd [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) egenskapen. Den hjälper dig att hitta olika egenskaper relaterade till färgen på ljuseffekten hos formen.

## Läs färgen på glödeffekten av en form

Se följande exempelkod och dess [käll-Excelfil](22774108.xlsx) och konsoloutputen för din referens. Följande skärmbild visar ljuseffekten hos formen i käll-Excelfilen när den visas i Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## C++ kod för att läsa färgen på shapes glödeffekt

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

## Konsoloutput

Här är konsoloutputen av ovanstående exempelkod när den körs med den angivna [käll-Excelfilen](22774108.xlsx).

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
