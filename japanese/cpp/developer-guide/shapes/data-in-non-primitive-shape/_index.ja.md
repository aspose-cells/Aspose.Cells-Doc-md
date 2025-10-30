---
title: 非プリミティブ図形のデータをC++で操作
linktitle: 非原始の形のデータ
type: docs
weight: 300
url: /ja/cpp/data-in-non-primitive-shape/
description: Aspose.Cellsを使って非プリミティブ図形のデータにアクセスし、操作します。
---

## **非原始の形のデータへのアクセス**

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。

## **非原始の形状**

Aspose.Cellsでは、非原始の形状にはタイプ[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/)が割り当てられます。[**Shape.AutoShapeType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/autoshapetype/)プロパティを使用してそのタイプを確認できます。

[**Shape.GetPaths()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getpaths/)プロパティを使用して形状データにアクセスします。これにより、非原始の形状を構成するすべての接続パスが返されます。これらのパスは、各セグメント内のポイントを含むセグメントのリストを保持する[**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/)タイプです。

|**非原始の形状の例を示す**|
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
