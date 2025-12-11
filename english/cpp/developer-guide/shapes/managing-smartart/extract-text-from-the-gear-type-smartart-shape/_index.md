---
title: Extract Text from the Gear Type SmartArt Shape with C++
linktitle: Extract Text from the Gear Type SmartArt Shape
type: docs
weight: 500
url: /cpp/extract-text-from-the-gear-type-smartart-shape/
description: Learn how to extract text from Gear Type SmartArt shapes in Excel using Aspose.Cells for C++ with step-by-step guidance and code examples.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells for C++ can extract text from the Gear Type SmartArt Shape. To achieve this, follow these steps:
1. Convert SmartArt Shape to Group Shape using the [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4) method.
2. Retrieve all individual shapes forming the Group Shape using the [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a) method.
3. Iterate through each individual shape and extract text using the [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a) method.

## **Extract Text from the Gear Type SmartArt Shape**

The following sample code loads a [sample Excel file](67338483.xlsx) containing a Gear Type SmartArt Shape and extracts text from its individual shapes. Refer to the console output below for results.

## **Sample Code**

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

    // Access the first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get the SmartArt result as a group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through the shapes and check gear types
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

## **Console Output**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
