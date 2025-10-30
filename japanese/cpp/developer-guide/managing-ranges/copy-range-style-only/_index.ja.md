---
title: C++を使用した範囲のスタイルのみコピー
linktitle: スタイルのみをコピーします。
type: docs
weight: 620
url: /ja/cpp/copy-range-style-only/
description: Aspose.Cellsを使ってExcelの範囲のスタイルのみをコピーする方法を学びます。
---

{{% alert color="primary" %}}

[データだけのコピー](/cells/ja/cpp/copy-range-data-only/)と[スタイル付きのコピー](/cells/ja/cpp/copy-range-data-with-style/)は、セル範囲から他の範囲へデータをコピーする方法と、書式を保持してコピーする方法を説明しています。フォーマットだけをコピーすることも可能です。こちらの方法もご参照ください。

{{% /alert %}} 

この例では、ワークブックを作成し、データで埋め、範囲のスタイルのみをコピーします。

1. 範囲を作成します。
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)を作成します。
1. 範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
最初の範囲の書式を2番目の範囲にコピーします。

```c++
#include <iostream>
#include <string>
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

    Range range2 = cells.CreateRange(u"C10", u"E13");
    range2.CopyStyle(range);

    U16String outputPath = outDir + u"copyrangestyle.out.xls";
    workbook.Save(outputPath);

    std::cout << "Range style copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
