---
title: Arbeta med reflexeffekten av form eller diagram med C++
linktitle: Att arbeta med reflektionseffekten i formen eller diagrammet
type: docs
weight: 210
url: /sv/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Lär dig hur man arbetar med refleksionseffekten av former eller diagram med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) tillsammans med [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) klass för att arbeta med refleksionseffekten av form eller diagram. [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) klassen innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationens krav.

- [Oskärpa](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [Riktning](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [Avstånd](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [Fade riktning](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [Rotera med formen](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [Storlek](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [Transparens](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [Typ](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **Att arbeta med reflektionseffekten i formen eller diagrammet**
Följande exempel laddar [källfils Excel](5115424.xlsx) och får åtkomst till den första formen i det första kalkylbladet och ställer in olika egenskaper av [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) klassen och sparar sedan arbetsboken i [utdata Excel-fil](5115423.xlsx).

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

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
