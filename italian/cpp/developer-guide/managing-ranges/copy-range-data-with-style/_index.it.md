---
title: Copia i dati dell intervallo con stile in C++
linktitle: Copia intervallo dati con stile.
type: docs
weight: 610
url: /it/cpp/copy-range-data-with-style/
description: Copia i dati dell intervallo inclusi gli stili delle celle usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Copia solo i dati dell'intervallo](/cells/it/cpp/copy-range-data-only/) spiegato come copiare i dati delle celle tra intervalli. Questo articolo dimostra come copiare gli intervalli mantenendo i loro stili di formattazione usando Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells fornisce classi e metodi per lavorare con gli intervalli inclusi [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), e [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Questo esempio dimostra come:

1. Creare una cartella di lavoro
1. Popolare le celle con dati
1. Creare un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Creare e configurare un oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)
1. Applicare stili all'intervallo
1. Creare un secondo intervallo
1. Copiare dati formattati tra intervalli

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
