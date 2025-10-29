---
title: Данные в не Primitive Shape с C++
linktitle: Данные в не примитивной форме
type: docs
weight: 300
url: /ru/cpp/data-in-non-primitive-shape/
description: Доступ и манипуляции с данными в не Primitive Shapes с использованием Aspose.Cells и C++.
---

## **Доступ к данным не примитивной формы**

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.

## **Форма не примитивной формы**

В Aspose.Cells нетипичным формам присваивается тип [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/). Вы можете проверить их тип, используя свойство [**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/).

Доступ к данным формы с использованием свойства [**Shape.GetPaths()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getpaths/). Оно возвращает все связанные пути, составляющие нетипичную форму. Эти пути имеют тип [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) и содержат список всех сегментов, в свою очередь содержащих точки в каждом сегменте.

|**Показывает пример нетипичной формы**|
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
