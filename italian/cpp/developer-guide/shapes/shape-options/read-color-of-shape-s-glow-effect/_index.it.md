---
title: Leggi il colore dell effetto bagliore della forma con C++
linktitle: Leggi il colore dell effetto di luce esterna della forma
type: docs
weight: 330
url: /it/cpp/read-color-of-shape-s-glow-effect/
description: Impara come leggere il colore dell effetto bagliore di qualsiasi forma usando Aspose.Cells for C++.
---

## Possibili scenari di utilizzo

Se si desidera leggere il colore dell'effetto di luce esterna di una qualsiasi forma, si prega di utilizzare la proprietà [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/). Questo vi aiuterà a trovare le varie proprietà relative al colore dell'effetto di luce esterna della forma.

## Leggere il colore dell'effetto di bagliore di una forma

Si prega di vedere il seguente codice di esempio e il suo [file excel di origine](22774108.xlsx) e l'output della console per il vostro riferimento. La seguente schermata mostra l'effetto di luce esterna della forma all'interno del file excel di origine quando visualizzato in Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Codice C++ per leggere il colore dell'effetto bagliore delle forme

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

## Output della console

Ecco l'output della console del codice di esempio precedente quando eseguito con il seguente [file excel di origine](22774108.xlsx).

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
