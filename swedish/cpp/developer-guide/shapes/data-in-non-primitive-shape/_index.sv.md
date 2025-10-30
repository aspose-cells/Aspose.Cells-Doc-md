---
title: Data i icke Primär Form med C++
linktitle: data i icke primitiv form
type: docs
weight: 300
url: /sv/cpp/data-in-non-primitive-shape/
description: Åtkomst och manipulera data i icke primära former med Aspose.Cells med C++.
---

## **Åtkomst till data av icke-primitiv form**

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.

## **En icke-primitiv form**

I Aspose.Cells tilldelas icke-primitiva former typen [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/). Du kan kontrollera deras typ med hjälp av egenskapen [**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/).

Åtkomst till formdata med användning av egenskapen [**Shape.GetPaths()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getpaths/). Den returnerar alla de anslutna vägarna som utgör den icke-primitiva formen. Dessa vägar är av typen [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) som håller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

|**Visar ett exempel på en icke-primitiv form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

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

    // Load the workbook
    Workbook workbook(srcDir + u"NonPrimitiveShape.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the user defined shape
    Shape shape = worksheet.GetShapes().Get(0);

    if (shape.GetAutoShapeType() == AutoShapeType::NotPrimitive)
    {
        // Access shape's data
        ShapePathCollection shapePathCollection = shape.GetPaths();

        // Access information of individual path
        for (int i = 0; i < shapePathCollection.GetCount(); ++i)
        {
            ShapePath shapePath = shapePathCollection.Get(i);

            // Access path segment list
            ShapeSegmentPathCollection pathSegments = shapePath.GetPathSegementList();

            // Access individual path segment
            for (int j = 0; j < pathSegments.GetCount(); ++j)
            {
                ShapeSegmentPath pathSegment = pathSegments.Get(j);

                // Gets the points in path segment
                ShapePathPointCollection segmentPoints = pathSegment.GetPoints();

                for (int k = 0; k < segmentPoints.GetCount(); ++k)
                {
                    ShapePathPoint pathPoint = segmentPoints.Get(k);
                    std::cout << "X: " << pathPoint.GetX() << ", Y: " << pathPoint.GetY() << std::endl;
                }
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
