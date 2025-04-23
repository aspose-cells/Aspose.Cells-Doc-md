---
title: Leer color del efecto de resplandor de la forma con C++
linktitle: Leer color del efecto de resplandor de la forma
type: docs
weight: 330
url: /es/cpp/read-color-of-shape-s-glow-effect/
description: Aprenda cómo leer el color del efecto de resplandor de cualquier forma usando Aspose.Cells for C++.
---

## Posibles Escenarios de Uso

Si desea leer el color del efecto de resplandor de cualquier forma, utilice la propiedad [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/). Le ayudará a encontrar varias propiedades relacionadas con el color del efecto de resplandor de la forma.

## Leer color del efecto de resplandor de la forma

Consulte el siguiente código de ejemplo y su [archivo de Excel fuente](22774108.xlsx) y la salida de la consola para su referencia. La siguiente captura de pantalla muestra el efecto de resplandor de la forma dentro del archivo de Excel fuente cuando se ve en Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Código C++ para leer el color del efecto de resplandor de formas

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

## Salida de la consola

Esta es la salida de la consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel fuente](22774108.xlsx) proporcionado.

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
