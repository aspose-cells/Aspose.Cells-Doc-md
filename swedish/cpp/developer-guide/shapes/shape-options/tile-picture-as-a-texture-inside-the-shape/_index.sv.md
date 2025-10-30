---
title: Bildplatta som textur inuti formen med C++
linktitle: Använda bild som texture i en form
type: docs
weight: 1700
url: /sv/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Lär dig hur man tilear ett foto som en textur inuti en form med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När bilden är liten och täcker inte hela ytan av formen utan att förlora kvalitet, har du möjlighet att använda den som texture. Texturen fyller formens yta med en liten bild genom att upprepa dem som om de är kakel.

## **Använda bild som texture i en form**

Du kan fylla formytan med någon bild och kachelera den med [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) egenskapen och ställa in den som **true**. Se följande exempelkod, dess [exempel-Excelfil](46465050.xlsx) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
