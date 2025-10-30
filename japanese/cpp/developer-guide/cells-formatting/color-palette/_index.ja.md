---
title: C++でカラーパレットを使用する方法
linktitle: カラーパレットの使用方法
type: docs
weight: 80
url: /ja/cpp/excel-color-palette/
description: カスタムカラーをパレットに追加し、Aspose.Cells for C++ APIを使用してExcelのカラーパレットを利用するC++コード。
keywords: c++でカスタムカラーをパレットに追加、プログラム的にExcelのカラーパレットを操作、ブック内でカラー パレットを操作する方法、C++でExcelのカラーパレットを使用する方法
---

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

## **パレットにカスタムカラーを追加する**

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、パレットを変更するための [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) メソッドがあり、カスタム色を追加するために次のパラメータを取ります:

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
