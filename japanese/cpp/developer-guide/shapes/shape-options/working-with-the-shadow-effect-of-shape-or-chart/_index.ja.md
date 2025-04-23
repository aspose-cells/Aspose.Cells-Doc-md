---
title: C++でシェイプやチャートのシャドウ効果を操作する
linktitle: 図形またはグラフの影効果の操作
type: docs
weight: 220
url: /ja/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Aspose.Cells for C++を使用して、シェイプやチャートのシャドウ効果を操作する方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsは、[GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/)メソッドと[ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/)クラスを提供し、シェイプやチャートのシャドウ効果を操作します。[ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/)クラスには、さまざまな結果を得るために設定可能な次のプロパティが含まれています。

- [GetAngle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **図形またはグラフの影効果の操作**
以下のサンプルコードは、[ソースエクセルファイル](5115425.xlsx)を読み込み、最初のワークシートの最初のシェイプにアクセスし、[GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/)プロパティのサブプロパティを設定し、その後ワークブックを[出力エクセルファイル](5115411.xlsx)として保存します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
