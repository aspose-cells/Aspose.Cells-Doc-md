---
title: C++を使用した範囲のデータのみコピー
linktitle: 範囲のデータのみをコピーします。
type: docs
weight: 600
url: /ja/cpp/copy-range-data-only/
description: Aspose.Cellsを使ってフォーマットなしで範囲のデータだけをコピーする方法を学びます。
---

{{% alert color="primary" %}}

時には、セルの範囲からデータを別の範囲にコピーする必要があります。しかし、書式ではなくデータのみが必要なことがあります。Aspose.Cellsではこの機能が提供されます。

この記事では、Aspose.Cellsを使用してデータの範囲をコピーするサンプルコードを提供します。

{{% /alert %}}

この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)を作成します。
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)を作成します。
1. 範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
1. 最初の範囲のデータを2番目の範囲にコピーします。

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

    for (int i = 0; i < 50; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            std::wstring value = std::to_wstring(i) + L"," + std::to_wstring(j);
            cells.Get(i, j).PutValue(U16String(reinterpret_cast<const char16_t*>(value.c_str())));
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
    range2.CopyData(range);

    U16String outputPath = outDir + u"CopyRangeData.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range data copied and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
