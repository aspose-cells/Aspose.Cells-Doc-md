---
title: Read Color of Shape's Glow Effect with C++
linktitle: Read Color of Shape's Glow Effect
type: docs
weight: 330
url: /cpp/read-color-of-shape-s-glow-effect/
description: Learn how to read the color of the glow effect of any shape using Aspose.Cells for C++.
---

## Possible Usage Scenarios

If you want to read the color of the glow effect of any shape, then please use the [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/color/) property. It will help you find the various properties relating to the color of the glow effect of the shape.

## Read Color of the Glow Effect of Shape

Please see the following sample code and its [source excel file](22774108.xlsx) and the console output for your reference. The following screenshot shows the glow effect of the shape inside the source excel file when viewed in Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## C++ code to read color of shapes glow effect

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Read the source excel file
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = sheet.GetShapes().Get(0);

    // Read the glow effect color and its various properties
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    std::cout << "Color: " << color.GetColor().ToArgb() << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Console Output

Here is the console output of the above sample code when executed with the provided [source excel file](22774108.xlsx).

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}