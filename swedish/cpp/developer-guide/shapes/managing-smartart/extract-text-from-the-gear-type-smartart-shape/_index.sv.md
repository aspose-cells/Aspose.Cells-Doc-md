---
title: Extrahera text från Gear typ SmartArt Shape med C++
linktitle: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 500
url: /sv/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Lär dig hur man extraherar text från Gear typ SmartArt former i Excel med Aspose.Cells for C++ med steg för steg guidning och kodexempel.
---

## **Möjliga användningsscenario**

Aspose.Cells for C++ kan extrahera text från Gear-typ SmartArt Shape. Följ dessa steg för att göra det:
1. Konvertera SmartArt Shape till Gruppform med [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4) metoden.
2. Hämta alla enskilda former som bildar Gruppformen med [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a) metoden.
3. Loop igenom varje enskild form och extrahera text med [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a) metoden.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande exempel kod laddar en [exempel-Excelfil](67338483.xlsx) som innehåller en Gear-typ SmartArt Shape och extraherar text från dess enskilda former. Se resultaten i konsolutmatningen nedan.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
