---
title: C++を使用してシェイプ内にタイル状の画像をテクスチャとして配置
linktitle: シェイプ内のテクスチャとして画像をタイル状に配置
type: docs
weight: 1700
url: /ja/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Aspose.Cells for C++を使用して、シェイプ内に画像をテクスチャとしてタイル状に配置する方法を学びます。
---

## **可能な使用シナリオ**

画像が小さく、品質を失うことなく形状の全体の表面をカバーしない場合、タイリングするオプションがあります。タイリングは、タイルであるかのように小さな画像で形状の表面を埋めるものです。

## **画像を形状の内部にテクスチャとしてタイル状にする**

形状表面を画像で塗りつぶしてタイルにする場合は、[**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) プロパティを使用して **true** に設定します。参照用のサンプルコード、[サンプルエクセルファイル](46465050.xlsx)、スクリーンショットをご覧ください。

## **スクリーンショット**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **サンプルコード**

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
