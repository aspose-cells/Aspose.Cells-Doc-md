---
title: C++を使ってシート内の図形を前面または背面に送る
linktitle: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 3400
url: /ja/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for C++を利用して、ワークシート内の図形のz順位置を変更する方法を学びます。
---

## **可能な使用シナリオ**

同一位置に複数の図形が存在する場合、その表示順はz順位置によって決まります。Aspose.Cellsは[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/)メソッドを提供し、これを使って図形のz順位置を変更します。図形を背面に送るには-1、-2、-3のような負の数を、前面に持ち上げるには1、2、3のような正の数を使います。

## **ワークシート内でShape FrontまたはBackを送信する**

以下のサンプルコードは[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/)メソッドの使用例です。コードで使用されている[サンプルExcelファイル](50528330.xlsx)と、それによって生成された[出力Excelファイル](50528331.xlsx)を参照してください。スクリーンショットは、コード実行後のサンプルExcelファイルの効果を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

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
