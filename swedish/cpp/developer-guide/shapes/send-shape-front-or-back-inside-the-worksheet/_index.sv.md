---
title: Skicka figur framåt eller bakåt inuti arbetsbladet med C++
linktitle: Skicka form framåt eller bakåt inne i Arbetsbladet
type: docs
weight: 3400
url: /sv/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Lär dig hur du ändrar z ordningen för figurer i ett arbetsblad med API Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När flera former finns på samma plats bestäms deras synlighet av deras z-order-placeringar. Aspose.Cells tillhandahåller [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/)-metoden, som ändrar formen z-ordningsposition. Om du vill skicka en form till bakgrunden använder du ett negativt nummer som -1, -2, -3 etc. Om du vill föra en form till fronten använder du ett positivt nummer som 1, 2, 3 etc.

## **Skicka form framåt eller bakåt inne i Arbetsbladet**

Följande exempel visar användningen av [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/)-metoden. Se [exempel-Excelfilen](50528330.xlsx) som används i koden och den [utdata-Excelfil](50528331.xlsx) som genereras. Skärmbilden visar effekten av koden på exempel-Excelfilen vid körning.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
