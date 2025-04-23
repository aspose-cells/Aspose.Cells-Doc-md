---
title: C++を使用してシェイプやチャートのグロー効果を操作する
linktitle: 形状またはチャートのグローエフェクトの操作
type: docs
weight: 240
url: /ja/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Aspose.Cells for C++を使用して、シェイプまたはチャートのグロー効果を操作する方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsは、[Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/)プロパティと[GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/)クラスを提供し、シェイプやチャートのグロー効果を操作します。 [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/)クラスには、さまざまな結果を得るために設定可能な次のプロパティが含まれています。

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **形状またはチャートのグローエフェクトの操作**
以下のサンプルコードは、[ソースExcelファイル](5115407.xlsx)を読み込み、最初のワークシートの最初のシェイプにアクセスし、[Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getgloweffect/)のサブプロパティを設定し、その後ワークブックを[出力Excelファイル](5115414.xlsx)に保存します。

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
