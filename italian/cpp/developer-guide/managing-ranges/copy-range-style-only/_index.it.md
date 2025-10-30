---
title: Copia solo il stile dell intervallo con C++
linktitle: Copia solo lo stile dell intervallo
type: docs
weight: 620
url: /it/cpp/copy-range-style-only/
description: Impara come copiare solo lo stile di un intervallo in Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

[Copia solo i dati dell'intervallo](/cells/it/cpp/copy-range-data-only/) e [Copia i dati dell'intervallo con stile](/cells/it/cpp/copy-range-data-with-style/) spiegato come copiare i dati da un intervallo a un altro da solo o completo di formattazione. È anche possibile copiare solo la formattazione. Questo articolo mostra come.

{{% /alert %}} 

Questo esempio crea un workbook, lo popola con dati e copia solo lo stile di un intervallo.

1. Crea un intervallo.
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) con attributi di formattazione specificati.
1. Applica la formattazione di stile all'intervallo.
1. Crea un secondo intervallo di celle.
1. Copia la formattazione del primo intervallo al secondo.

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
