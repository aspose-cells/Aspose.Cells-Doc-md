---
title: Data in Non-Primitive Shape with C++
linktitle: Data in Non-Primitive Shape
type: docs
weight: 300
url: /cpp/data-in-non-primitive-shape/
description: Access and manipulate data in non-primitive shapes using Aspose.Cells with C++.
---

## **Accessing Data of Non-Primitive Shape**

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.

## **A Non-Primitive Shape**

In Aspose.Cells, non-primitive shapes are assigned the type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/). You can check their type using the [**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/autoshapetype/) property.

Access the shape data using the [**Shape.Paths**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/paths/) property. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) that holds a list of all the segments which in turn contain the points in each segment.

|**Shows an example of a non-primitive shape**|
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