---
title: 用C++提取Gear类型SmartArt形状中的文本
linktitle: 从齿轮型智能图形中提取文本
type: docs
weight: 500
url: /zh/cpp/extract-text-from-the-gear-type-smartart-shape/
description: 学习如何使用Aspose.Cells for C++逐步指导和代码示例，从Excel中的Gear类型SmartArt形状中提取文本。
---

## **可能的使用场景**

Aspose.Cells for C++可以提取Gear类型SmartArt形状中的文本。请按以下步骤操作：
1. 使用[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4)方法将SmartArt形状转换为组形状。
2. 使用[**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a)方法获取组成组形状的所有单个形状。
3. 遍历每个单个形状并使用[**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a)方法提取文本。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含Gear类型SmartArt形状的[示例Excel文件](67338483.xlsx)，并从其单个形状中提取文本。结果请参见下面的控制台输出。

## **示例代码**

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

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
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

## **控制台输出**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
