---
title: 使用C++处理Shape或Chart的ThreeDFormat
linktitle: 使用 Aspose.Cells 处理形状或图表的三维格式
type: docs
weight: 250
url: /zh/cpp/working-with-the-threedformat-of-shape-or-chart/
description: 学习如何用C++操控形状或图表的3D格式。
---

## **可能的使用场景**
Aspose.Cells提供[Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/)属性和[ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)类，用于处理形状或图表的3D格式。[ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)类包含多种属性，可根据应用需求设置不同效果。

## **使用 Aspose.Cells 处理形状或图表的三维格式**
以下示例代码加载[源Excel文件](5115419.xlsx)，访问第一个工作表中的第一个形状，然后设置[Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/)属性的子属性，并保存为[输出Excel文件](5115410.xlsx)。

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

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
