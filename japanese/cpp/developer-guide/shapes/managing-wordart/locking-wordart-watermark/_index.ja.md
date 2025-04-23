---
title: C++を使ったWordArtウォーターマークのロック
linktitle: WordArtウォーターマークをロックする
type: docs
weight: 170
url: /ja/cpp/locking-wordart-watermark/
description: Aspose.Cells for C++を使ってExcelワークシートのWordArtウォーターマークをロックする方法を学びます。編集、移動、選択をプログラムによって防止します。
---

{{% alert color="primary" %}}

Aspose.Cells APIを使用すると、ワードアートの透かしをワークシート上に追加し、ワードアートが移動および配置可能なオブジェクトとなる方法を提供します。また、編集、移動、選択などの操作をロックすることも可能です。この記事では、[**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/)メソッドを使用して透かしのいくつかの側面をロックする方法について説明します。

{{% /alert %}}

Aspose.Cells APIは、透かしの特定の側面をロックして、ユーザーの操作を制限または完全にブロックすることを可能にします。以下のコードスニペットは、最初からスプレッドシートを作成し、Aspose.Cells for C++ APIを使用して透かしの選択、移動、編集、およびリサイズをロックする例を示しています。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
