---
title: Bestäm om Shape är Smart Art Shape med C++
linktitle: Avgöra om en form är Smart Art Shape
type: docs
weight: 400
url: /sv/cpp/determine-if-shape-is-smart-art-shape/
description: Lär dig hur man avgör om en form är en Smart Art Shape med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Smart Art Shapes är speciella former i Microsoft Excel som gör att du kan skapa komplexa diagram automatiskt. Du kan ta reda på om formen är en smart konstform eller vanlig form med [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) egenskapen.

## **Avgör om formen är en SmartArt-form**

Följande kodexempel laddar [exempel Excel-filen](55541792.xlsx) som innehåller en smart konstform som visas på den här bilden. Sedan skriver den ut värdet på [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) egenskapen för den första formen. Se konsoloutputen från det angivna kodexemplet nedan.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
