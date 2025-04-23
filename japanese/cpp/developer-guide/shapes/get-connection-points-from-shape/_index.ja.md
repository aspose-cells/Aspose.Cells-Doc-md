---
title: Shapeから接続ポイントを取得（C++）
linktitle: シェイプから接続ポイントを取得
type: docs
weight: 3500
url: /ja/cpp/get-connection-points-from-shape/
description: Aspose.Cells for C++を使って、シェイプの接続ポイントを取得する方法を学びます。
---

Aspose.Cellsは、スプレッドシート内の図形を管理する豊富な機能を提供します。時には、整列や配置のために図形の接続ポイントを取得する必要があります。以下のコードは、[Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/)メソッドを使用してシェイプの接続ポイントリストを取得する例です。

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
