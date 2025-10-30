---
title: C++ ile Primitif olmayan Şekildeki Veriler
linktitle: Non Primitive Şekildeki Veri
type: docs
weight: 300
url: /tr/cpp/data-in-non-primitive-shape/
description: Aspose.Cells kullanarak C++ ile primitif olmayan şekillerdeki verilere erişin ve bunları yönetin.
---

## **Basit olmayan Şeklin Verilerine Erişmek**

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **Basit Olmayan Bir Şekil**

Aspose.Cells'te primitif olmayan şekillere [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/) türü atanır. Onların türünü [**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/) özelliğini kullanarak kontrol edebilirsiniz.

Şekil verisine [**Shape.GetPaths()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getpaths/) özelliğini kullanarak erişin. Bu, primitif olmayan şekli oluşturan tüm bağlantılı yol segmentlerini döndürür. Bu yollar, her bir segmentteki noktaları içeren [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) türünden oluşan bir listeyi tutar.

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|
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
