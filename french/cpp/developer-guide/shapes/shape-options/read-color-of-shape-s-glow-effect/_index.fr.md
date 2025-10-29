---
title: Lire la couleur de l effet de glow de la forme avec C++
linktitle: Lire la couleur de l effet de luminescence de la forme
type: docs
weight: 330
url: /fr/cpp/read-color-of-shape-s-glow-effect/
description: Découvrez comment lire la couleur de l effet de glow de n importe quelle forme en utilisant Aspose.Cells for C++.
---

## Scénarios d'utilisation possibles

Si vous souhaitez lire la couleur de l'effet de luminescence de n'importe quelle forme, veuillez utiliser la propriété [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/). Cela vous aidera à trouver les différentes propriétés concernant la couleur de l'effet de luminescence de la forme.

## Lire la couleur de l'effet de luminescence de la forme

Veuillez consulter le code d'échantillon suivant et son [fichier Excel source](22774108.xlsx) ainsi que la sortie de la console pour votre référence. La capture d'écran suivante montre l'effet de luminescence de la forme à l'intérieur du fichier Excel source lorsqu'il est visualisé dans Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Code C++ pour lire la couleur de l'effet de glow des formes

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

## Sortie de la console

Voici la sortie de la console du code d'échantillon ci-dessus lorsqu'il est exécuté avec le [fichier Excel source](22774108.xlsx) fourni.

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
