---
title: 使用C++处理形状或图表的发光效果
linktitle: 处理形状或图表的发光效果
type: docs
weight: 240
url: /zh/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: 学习如何使用Aspose.Cells for C++处理形状或图表的发光效果。
---

## **可能的使用场景**
Aspose.Cells提供[Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/)属性和[GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/)类，用于处理形状或图表的发光效果。[GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/)类包含以下属性，可按应用需求设置以实现不同效果。

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **处理形状或图表的发光效果**
以下示例代码加载[源Excel文件](5115407.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/)属性的子属性，然后将工作簿保存为[输出Excel文件](5115414.xlsx)。

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
