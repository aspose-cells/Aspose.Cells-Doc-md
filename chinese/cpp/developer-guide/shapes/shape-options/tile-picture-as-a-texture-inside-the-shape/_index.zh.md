---
title: 使用 C++ 将图片作为纹理铺设到形状内部
linktitle: 在形状内作为纹理平铺图片
type: docs
weight: 1700
url: /zh/cpp/tile-picture-as-a-texture-inside-the-shape/
description: 学习如何使用Aspose.Cells for C++将图片平铺为形状内的纹理。
---

## **可能的使用场景**

当图片较小且不覆盖整个形状表面而又不失真时，可以选择将其平铺。平铺会通过重复小图像来填充形状表面，就像它们是瓷砖一样。

## **在形状内部将图片作为纹理平铺**

您可以使用[**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/)属性填充形状表面并设置为**true**以平铺。请查看以下示例代码、[示例Excel文件](46465050.xlsx)以及屏幕截图供参考。

## **屏幕截图**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **示例代码**

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
