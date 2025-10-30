---
title: Kopiera datat i ett område med stil i C++
linktitle: Kopiera dataområde med stil
type: docs
weight: 610
url: /sv/cpp/copy-range-data-with-style/
description: Kopiera data i ett område inklusive cellstilar i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Kopiera endast data i område](/cells/sv/cpp/copy-range-data-only/) förklarar hur man kopierar celldata mellan områden. Denna artikel visar hur man kopierar cellområden samtidigt som man bevarar deras formateringsstilar med hjälp av Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells tillhandahåller klasser och metoder för att arbeta med områden inklusive [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), och [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Detta exempel visar hur man:

1. Skapa en arbetsbok
1. Fyll celler med data
1. Skapa en [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Skapa och konfigurera ett [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objekt
1. Applicera stilar på området
1. Skapa ett andra område
1. Kopiera formaterad data mellan områden

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
