---
title: Smart Artをグループシェイプに変換する方法（C++）
linktitle: スマートアートをグループ形状に変換
type: docs
weight: 200
url: /ja/cpp/convert-the-smart-art-to-group-shape/
description: Aspose.Cells for C++を使用して、Smart Art ShapeをGroup Shapeに変換し、グループシェイプの個々の部分にアクセスする方法を学びます。
---

## **可能な使用シナリオ**

Smart Art ShapeをGroup Shapeに変換するには、[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/)メソッドを使用します。これにより、スマートアートの形状をグループ形状として扱えるようになります。それにより、グループ形状の個々の部分または形状にアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

以下のサンプルコードは、Smart Art Shapeを含む[sample Excelファイル](55541793.xlsx)を読み込み、スクリーンショットのような表示をします。その後、Smart Art Shapeをグループシェイプに変換し、Shape::IsGroupプロパティを出力します。サンプルコードのコンソール出力例は以下です。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
