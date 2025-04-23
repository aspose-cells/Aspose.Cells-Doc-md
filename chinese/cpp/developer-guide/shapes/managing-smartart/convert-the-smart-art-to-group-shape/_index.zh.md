---
title: 使用C++将Smart Art转换为组形状
linktitle: 将智能图转为组合形状
type: docs
weight: 200
url: /zh/cpp/convert-the-smart-art-to-group-shape/
description: 了解如何使用Aspose.Cells for C++将Smart Art形状转换为组形状，并访问组形状的各个部分。
---

## **可能的使用场景**

您可以使用[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/)方法将智能图形转为组合形状。这将使您能够像处理组合形状一样处理智能图形。因此，您将能够访问组合形状的各个部分或形状。

## **将智能图转换为组合形状**

以下示例代码加载含有Smart Art形状的[示例Excel文件](55541793.xlsx)，并将Smart Art形状转换为组形状，打印Shape::IsGroup属性。请查看下面的控制台输出。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **示例代码**

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

## **控制台输出**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
