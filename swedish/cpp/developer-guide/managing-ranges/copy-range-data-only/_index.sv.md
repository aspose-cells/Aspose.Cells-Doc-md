---
title: Kopiera endast data i området med C++
linktitle: Kopiera endast dataområde
type: docs
weight: 600
url: /sv/cpp/copy-range-data-only/
description: Lär dig hur du kopierar enbart data i ett område utan formatering med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver du kopiera data från en cellintervall till en annan, kopiera bara datan, inte formateringen. Aspose.Cells erbjuder den här funktionen.

Den här artikeln ger en exempelkod som använder Aspose.Cells för att kopiera ett datintervall.

{{% /alert %}}

Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa en [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).
1. Skapa ett [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en annan cellintervall.
1. Kopiera data från det första området till det andra området.

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
{{< app/cells/assistant language="cpp" >}}
