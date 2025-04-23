---
title: Farbe des Glüh Effekts eines Shapes mit C++ auslesen
linktitle: Lesen Sie die Farbe des Leuchteffekts der Form.
type: docs
weight: 330
url: /de/cpp/read-color-of-shape-s-glow-effect/
description: Erfahre, wie man die Farbe des Glüh Effekts eines beliebigen Shapes mit Aspose.Cells for C++ liest.
---

## Mögliche Anwendungsszenarien

Wenn Sie die Farbe des Leuchteffekts einer Form lesen möchten, verwenden Sie bitte die [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) Eigenschaft. Dies hilft Ihnen, verschiedene Eigenschaften in Bezug auf die Farbe des Leuchteffekts der Form zu finden.

## Farbe des Glow-Effekts der Form lesen

Bitte sehen Sie sich den folgenden Beispielcode und seine [Quelldatei](22774108.xlsx) sowie die Konsolenausgabe zu Ihrer Referenz an. Der folgende Screenshot zeigt den Leuchteffekt der Form in der Quelldatei, wenn sie in Microsoft Excel angezeigt wird.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## C++-Code zum Lesen der Farbe des Glüheffekts von Formen

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

## Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der bereitgestellten [Quelldatei](22774108.xlsx) ausgeführt wird.

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
