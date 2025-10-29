---
title: 用C++判断Shape是否为Smart Art Shape
linktitle: 确定形状是否为智能图形
type: docs
weight: 400
url: /zh/cpp/determine-if-shape-is-smart-art-shape/
description: 了解如何使用Aspose.Cells for C++判断一个形状是否为Smart Art Shape。
---

## **可能的使用场景**

智能图形是Microsoft Excel中特殊的形状，允许您自动生成复杂的图表。使用[**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/)属性可以确定该形状是智能图形还是常规图形。

## **确定形状是否为智能图形**

以下示例代码加载包含智能图形的[sample Excel文件](55541792.xlsx)，如下图所示。然后打印第一个形状的[**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/)属性的值。请参阅下面提供的示例代码的控制台输出。

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **示例代码**

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

## **控制台输出**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
