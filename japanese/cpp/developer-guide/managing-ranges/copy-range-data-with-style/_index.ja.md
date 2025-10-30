---
title: スタイル付きデータの範囲コピー（C++）
linktitle: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 610
url: /ja/cpp/copy-range-data-with-style/
description: セルのスタイルを含む範囲のデータを、Aspose.Cells for C++を使用してコピーします。
---

{{% alert color="primary" %}}

[コピー範囲のデータのみ](/cells/ja/cpp/copy-range-data-only/)では、セル範囲間でセルデータをコピーする方法を説明しています。本記事では、Aspose.Cells for C++を使用してセル範囲をコピーし、その書式スタイルを保持する方法を紹介します。

{{% /alert %}}

Aspose.Cellsは、範囲に関するクラスとメソッド（[**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)、[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)）を提供しています。

この例は、次の操作方法を示しています：

1. ブックを作成
1. セルにデータを入力
1. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)を作成
1. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)オブジェクトを作成および設定
1. 範囲にスタイルを適用
1. 2つ目の範囲を作成
1. 範囲間でフォーマットされたデータをコピー

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    for (int i = 0; i < 50; ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            cells.Get(i, j).PutValue((std::to_wstring(i) + L"," + std::to_wstring(j)).c_str());
        }
    }

    Range range = cells.CreateRange(u"A1", u"D3");
    Style style = workbook.CreateStyle();

    style.GetFont().SetName(u"Calibri");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    StyleFlag flag1;
    flag1.SetFontName(true);
    flag1.SetCellShading(true);
    flag1.SetBorders(true);

    range.ApplyStyle(style, flag1);

    Range range2 = cells.CreateRange(u"C10", u"F12");
    range2.Copy(range);

    U16String outputPath = outDir + u"CopyRange.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range copied with formatting successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
