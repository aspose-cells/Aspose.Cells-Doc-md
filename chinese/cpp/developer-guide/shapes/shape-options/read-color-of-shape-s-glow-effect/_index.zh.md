---
title: 用C++读取形状发光效果的颜色
linktitle: 读取形状的发光效果的颜色
type: docs
weight: 330
url: /zh/cpp/read-color-of-shape-s-glow-effect/
description: 学习如何使用 Aspose.Cells for C++ 读取任何形状发光效果的颜色。
---

## 可能的使用场景

如果您想要阅读任何形状的发光效果的颜色，请使用[**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/)属性。这将帮助您找到与形状的发光效果的颜色相关的各种属性。

## 读取形状发光效果的颜色

请查看以下示例代码及其[源Excel文件](22774108.xlsx)和控制台输出，供您参考。以下屏幕截图显示了在Microsoft Excel中查看源Excel文件时形状的发光效果。

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## 用C++读取形状发光效果颜色的代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);
    Shape shape = sheet.GetShapes().Get(0);
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    Color clr = color.GetColor();
    uint32_t argb = (static_cast<uint32_t>(clr.a) << 24) | 
                    (static_cast<uint32_t>(clr.r) << 16) | 
                    (static_cast<uint32_t>(clr.g) << 8) | 
                    static_cast<uint32_t>(clr.b);

    std::cout << "Color: " << argb << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 控制台输出

以下是在提供的[源Excel文件](22774108.xlsx)上执行上述示例代码时的控制台输出。

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
