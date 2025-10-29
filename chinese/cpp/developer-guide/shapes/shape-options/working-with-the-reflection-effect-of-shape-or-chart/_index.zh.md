---
title: 使用C++处理形状或图表的反射效果
linktitle: 处理形状或图表的倒影效果
type: docs
weight: 210
url: /zh/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: 学习如何使用Aspose.Cells和C++处理形状或图表的反射效果。
---

## **可能的使用场景**
Aspose.Cells提供[Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/)属性和[ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/)类，用于处理形状或图表的反射效果。[ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/)类包含不同属性，可根据应用需求设置以实现不同效果。

- [模糊](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [方向](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [距离](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [渐变方向](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [随形状旋转](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [大小](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [透明度](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [类型](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **使用形状或图表的反射效果**
以下示例代码加载[源Excel文件](5115424.xlsx)，访问默认工作表中的第一个形状，设置[Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/)类的不同属性，然后将工作簿保存为[输出Excel文件](5115423.xlsx)。

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

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
