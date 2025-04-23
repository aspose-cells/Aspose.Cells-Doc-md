---
title: C++でシェイプのグロー効果の色を読む
linktitle: 形状のグローエフェクトの色を読み取りたい場合は、{0}プロパティを使用してください。これにより、形状のグローエフェクトの色に関連するさまざまなプロパティがわかります。
type: docs
weight: 330
url: /ja/cpp/read-color-of-shape-s-glow-effect/
description: Aspose.Cells for C++を使用して、任意のシェイプのグロー効果の色を読む方法を学びます。
---

## 可能な使用シナリオ

形状のグローエフェクトの色を読み取りたい場合は、[**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/)プロパティを使用してください。これにより、形状のグローエフェクトの色に関連するさまざまなプロパティがわかります。

## シェイプのグローエフェクトの色を読む

参照のために、以下はサンプルコードとその [ソースエクセルファイル](22774108.xlsx) およびコンソール出力を示したスクリーンショットです。次のスクリーンショットは、Microsoft Excelで表示したときのソースエクセルファイル内の形状のグローエフェクトを示しています。

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## C++コード: シェイプのグロー効果の色を読む

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);
    Shape shape = sheet.GetShapes().Get(0);
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    Color clr = color.GetColor();
    uint32_t argb = (static_cast<uint32_t>(clr.a) << 24) | 
                    (static_cast<uint32_t>(clr.r) << 16) | 
                    (static_cast<uint32_t>(clr.g) << 8) | 
                    static_cast<uint32_t>(clr.b);

    std::cout << "Color: " << argb << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## コンソール出力

提供された [ソースエクセルファイル](22774108.xlsx) で上記のサンプルコードを実行したときのコンソール出力は次のとおりです。

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
