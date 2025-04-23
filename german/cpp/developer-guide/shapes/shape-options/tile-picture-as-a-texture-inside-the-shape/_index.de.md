---
title: Fliesenbild als Textur in der Form mit C++
linktitle: Kachelbild als Textur in der Form
type: docs
weight: 1700
url: /de/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Lernen Sie, wie man ein Bild als Textur innerhalb einer Form mit Aspose.Cells for C++ tilet.
---

## **Mögliche Verwendungsszenarien**

Wenn das Bild klein ist und nicht die gesamte Oberfläche der Form abdeckt, ohne an Qualität zu verlieren, haben Sie die Möglichkeit, es zu kacheln. Kacheln füllt die Oberfläche der Form mit einem kleinen Bild, indem es diese wiederholt, als wären es Fliesen.

## **Kachelbild als Textur in der Form**

Sie können die Formfläche mit einem Bild füllen und mithilfe der [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) Eigenschaft und dem Einstellen auf **true** kacheln. Bitte sehen Sie sich den folgenden Beispielcode, seine [Beispiel-Excel-Datei](46465050.xlsx) sowie den Screenshot zur Referenz an.

## **Screenshot**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Beispielcode**

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
