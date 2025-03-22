---
title: Tile Picture as a Texture inside the Shape with C++
linktitle: Tile Picture as a Texture inside the Shape
type: docs
weight: 1700
url: /cpp/tile-picture-as-a-texture-inside-the-shape/
description: Learn how to tile a picture as a texture inside a shape using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

When the picture is small and does not cover the entire surface of the shape without losing its quality, then you have the option to tile it. Tiling fills the shape surface with a small image by repeating them as if they are tiles.

## **Tile Picture as a Texture inside the Shape**

You can fill the shape surface with some image and tile it using the [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) property and setting it **true**. Please see the following sample code, its [sample Excel file](46465050.xlsx) as well as the screenshot for a reference.

## **Screenshot**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Sample Code**

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```