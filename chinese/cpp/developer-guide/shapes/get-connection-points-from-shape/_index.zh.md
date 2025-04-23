---
title: 从形状获取连接点（C++）
linktitle: 获取连接点
type: docs
weight: 3500
url: /zh/cpp/get-connection-points-from-shape/
description: 学习如何使用Aspose.Cells for C++检索形状的连接点。
---

Aspose.Cells提供丰富的功能管理电子表格中的形状。有时需要获取形状的连接点以进行对齐或定位。以下代码可用于使用 [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/) 方法获取形状的连接点列表。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sampleGetFonts.xlsx");

    Vector<Font> fonts = workbook.GetFonts();

    for (int i = 0; i < fonts.GetLength(); ++i)
    {
        std::cout << fonts[i].ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

.
