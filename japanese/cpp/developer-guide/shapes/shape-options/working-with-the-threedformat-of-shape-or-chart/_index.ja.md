---
title: ShapeまたはChartのThreeDFormatをC++で操作する方法
linktitle: 図形またはグラフの3 D形式の操作
type: docs
weight: 250
url: /ja/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Aspose.Cellsは、ShapeまたはChartの3Dフォーマットを操作するために、[Shape.ThreeDFormat](https //reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/)プロパティと[ThreeDFormat](https //reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)クラスを提供しています。[ThreeDFormat](https //reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)クラスは、アプリケーションの要件に応じてさまざまな結果を達成するために設定できる複数のプロパティを含んでいます。
---

## **可能な使用シナリオ**
Aspose.Cellsは、[Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/)プロパティと[ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)クラスを提供し、形状やチャートの3Dフォーマットを操作します。[ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/)クラスには、アプリケーションの要件に応じてさまざまな結果を得るために設定できるさまざまなプロパティが含まれています。

## **図形またはグラフの3-D形式の操作**
次のサンプルコードは、[ソースエクセルファイル](5115419.xlsx)を読み込み、最初のワークシートの最初のシェイプにアクセスします。その後、[Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) プロパティのサブプロパティを設定し、ワークブックを[出力エクセルファイル](5115410.xlsx)として保存します。

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

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
