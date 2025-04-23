---
title: Konvertera Smart Art till Gruppform med C++
linktitle: Konvertera Smart Art till gruppform
type: docs
weight: 200
url: /sv/cpp/convert-the-smart-art-to-group-shape/
description: Lär dig hur man konverterar Smart Art Shape till Gruppform med Aspose.Cells for C++ och får tillgång till enskilda delar av gruppformen.
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art Shape till gruppform med hjälp av [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/)-metoden. Det gör att du kan hantera Smart Art Shape som en gruppform. Som följd kommer du att ha tillgång till de enskilda delarna eller formarna i gruppformen.

## **Konvertera SmartArt till gruppform**

Följande exempel kod laddar [exempel-Excelfil](55541793.xlsx) som innehåller en smart art form som visas i denna skärmdump. Den konverterar sedan smart art formen till gruppform och skriver ut Shape::IsGroup-egenskapen. Se konsolutmatningen av koden nedan.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
