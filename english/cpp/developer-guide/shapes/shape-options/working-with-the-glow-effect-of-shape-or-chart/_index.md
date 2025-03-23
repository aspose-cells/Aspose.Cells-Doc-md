---
title: Working with the Glow Effect of Shape or Chart with C++
linktitle: Working with the Glow Effect of Shape or Chart
type: docs
weight: 240
url: /cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Learn how to work with the glow effect of shapes or charts using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) property along with [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) class to work with the glow effect of shape or chart. The [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) class contains the following properties which can be set to achieve different results as per application requirements.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Working with the Glow Effect of Shape or Chart**
The following sample code loads the [source excel file](5115407.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) property and then saves the workbook in [output excel file](5115414.xlsx).

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