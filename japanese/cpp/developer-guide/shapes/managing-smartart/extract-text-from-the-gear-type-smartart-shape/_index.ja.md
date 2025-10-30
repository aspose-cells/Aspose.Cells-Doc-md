---
title: GearタイプのSmartArt Shapeからテキストを抽出する（C++）
linktitle: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for C++を使用して、ExcelのGearタイプSmartArt Shapeからテキストを抽出する方法をステップバイステップガイドとコード例付きで学びます。
---

## **可能な使用シナリオ**

Aspose.Cells for C++は、GearタイプのSmartArt Shapeからテキストを抽出できます。これを行うためには、以下の手順に従います：
1. SmartArt Shapeを[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4)メソッドを用いてグループシェイプに変換します。
2. [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a)メソッドを使って、グループシェイプを構成するすべての個別シェイプを取得します。
3. 各個別シェイプをループしながら、[**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a)メソッドを用いてテキストを抽出します。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、GearタイプのSmartArt Shapeを含む[サンプルExcelファイル](67338483.xlsx)を読み込み、その個別シェイプからテキストを抽出します。結果はコンソール出力を参照してください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
