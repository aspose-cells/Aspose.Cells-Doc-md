---
title: 使用C++在非原始形状中插入数据
linktitle: 非基本形状中的数据
type: docs
weight: 300
url: /zh/cpp/data-in-non-primitive-shape/
description: 使用Aspose.Cells和C++访问和操作非原始形状中的数据。
---

## **访问非基本形状的数据**

有时，您需要访问非内置形状的形状的数据。内置形状称为基本形状；而不是内置形状的称为非基本形状。例如，您可以使用不同的曲线连接线定义自己的形状。

## **非基本形状**

在Aspose.Cells中，非原始形状分配的类型为 [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/)。您可以使用 [**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/) 属性检查它们的类型。

使用 [**Shape.GetPaths()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getpaths/) 属性访问形状数据。它返回组成非原始形状的所有连接路径。这些路径的类型为 [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/)，包含了所有段的列表，而每个段又包含了每个段中的点。

|**显示了非原始形状的示例**|
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
