---
title: Arbeta med skuggeffekten av form eller diagram med C++
linktitle: Att arbeta med skuggeffekten i formen eller diagrammet
type: docs
weight: 220
url: /sv/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Lär dig hur man manipulerar skuggeffekten av former eller diagram med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller metoden [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) tillsammans med klassen [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) för att arbeta med skuggeffekten av former eller diagram. [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationens krav.

- [GetAngle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **Att arbeta med skuggeffekten i formen eller diagrammet**
Följande exempel laddar [källfils Excel](5115425.xlsx) och får åtkomst till den första formen i det första kalkylbladet och ställer in underegenskaperna för [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) egenskapen och sparar sedan arbetsboken i [utdata Excel-fil](5115411.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
