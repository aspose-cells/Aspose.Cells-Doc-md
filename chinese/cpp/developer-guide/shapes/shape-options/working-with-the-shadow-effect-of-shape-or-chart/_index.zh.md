---
title: 使用C++处理形状或图表的阴影效果
linktitle: 使用形状或图表的阴影效果
type: docs
weight: 220
url: /zh/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: 学习如何使用Aspose.Cells for C++操控形状或图表的阴影效果。
---

## **可能的使用场景**
Aspose.Cells提供[GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/)方法和[ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/)类，用于处理形状或图表的阴影效果。[ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/)类包含不同属性，可按应用需求设置以实现不同效果。

- [GetAngle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **使用 Aspose.Cells 处理形状或图表的阴影效果**
以下示例代码加载[源Excel文件](5115425.xlsx)，访问第一个工作表中的第一个形状，设置[GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/)属性的不同子属性，然后将工作簿保存为[输出Excel文件](5115411.xlsx)。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
