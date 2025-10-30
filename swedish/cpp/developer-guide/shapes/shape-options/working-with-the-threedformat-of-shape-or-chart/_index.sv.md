---
title: Arbeta med ThreeDFormat av form eller diagram med C++
linktitle: Att arbeta med ThreeDFormat av formen eller diagrammet
type: docs
weight: 250
url: /sv/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Lär dig hur man manipulerar 3 D formatet av former eller diagram med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) tillsammans med [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) klass för att arbeta med 3-D-formatet av former eller diagram. [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) klassen innehåller olika egenskaper som kan ställas in för att uppnå olika resultat enligt applikationens krav.

## **Att arbeta med ThreeDFormat av formen eller diagrammet**
Följande exempel laddar [källfils Excel](5115419.xlsx) och får åtkomst till den första formen i det första kalkylbladet. Det ställer in sedan underegenskaperna för [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) egenskapen och sparar arbetsboken i [utdata Excel](5115410.xlsx).

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

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
