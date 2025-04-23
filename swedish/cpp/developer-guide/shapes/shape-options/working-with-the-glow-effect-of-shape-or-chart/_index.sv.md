---
title: Arbeta med glödeffekten av form eller diagram med C++
linktitle: Arbeta med glödeffekten av form eller diagram
type: docs
weight: 240
url: /sv/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Lär dig hur man arbetar med glödeffekten av former eller diagram med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) tillsammans med [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) klass för att arbeta med glödeffekten av form eller diagram. [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) klassen innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationens krav.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Arbeta med glödeffekten av form eller diagram**
Följande exempel laddar [källfils Excel](5115407.xlsx) och får åtkomst till den första formen i det första kalkylbladet och ställer in underegenskaperna för [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) egenskapen och sparar sedan arbetsboken i [utdata Excel-fil](5115414.xlsx).

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
