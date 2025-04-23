---
title: 在工作表内向Shape前后移动（前景层次）用C++
linktitle: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/cpp/send-shape-front-or-back-inside-the-worksheet/
description: 学习如何使用 Aspose.Cells for C++ 改变工作表中形状的z次序位置。
---

## **可能的使用场景**

当多个形状位于同一位置时，它们的可见性由z次序位置决定。Aspose.Cells 提供了 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) 方法，可以改变形状的z次序。如果要将形状送到最底层，可以使用负数如-1、-2、-3等；如果要将形状带到最前面，使用正数如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码演示了 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) 方法的用法。请查看用于此代码的 [示例Excel文件](50528330.xlsx) 和由它生成的 [输出Excel文件](50528331.xlsx)。截图展示了代码执行后对示例Excel文件的效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
