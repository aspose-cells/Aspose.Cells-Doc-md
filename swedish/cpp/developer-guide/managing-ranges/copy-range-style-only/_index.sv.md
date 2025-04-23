---
title: Kopiera endast områdets stil med C++
linktitle: Kopiera endast stilområde
type: docs
weight: 620
url: /sv/cpp/copy-range-style-only/
description: Lär dig hur du bara kopierar stilen i ett område i Excel med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

[Kopiera endast data i område](/cells/sv/cpp/copy-range-data-only/) och [Kopiera data med stil](/cells/sv/cpp/copy-range-data-with-style/) förklarar hur man kopierar data från ett område till ett annat på egen hand eller komplett med formatering. Det är också möjligt att kopiera enbart formateringen. Denna artikel visar hur.

{{% /alert %}} 

Detta exempel skapar en arbetsbok, fyller den med data och kopierar endast stil från ett intervall.

1. Skapa ett område.
1. Skapa ett [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en andra cellintervall.
1. Kopiera det första områdets formatering till det andra området.

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
