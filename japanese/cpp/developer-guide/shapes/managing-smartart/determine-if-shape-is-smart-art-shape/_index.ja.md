---
title: ShapeがSmart Art Shapeかどうかを判断する方法（C++）
linktitle: 形状がスマートアート形状かどうかの判定
type: docs
weight: 400
url: /ja/cpp/determine-if-shape-is-smart-art-shape/
description: Aspose.Cells for C++を使用して、ShapeがSmart Art Shapeかどうかを判定する方法を学びます。
---

## **可能な使用シナリオ**

スマートアートシェイプは、Microsoft Excelの特別な形状であり、自動的に複雑な図を作成できます。[**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/)プロパティを使用して、形状がスマートアートシェイプか通常の形状かを特定できます。

## **シェイプがスマートアートシェイプかどうかを判定する**

以下のサンプルコードは、第一のShapeの[**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/)プロパティの値が出力される[sample Excel file](55541792.xlsx)をロードし、出力するコンソールの出力結果を表示しています。

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
