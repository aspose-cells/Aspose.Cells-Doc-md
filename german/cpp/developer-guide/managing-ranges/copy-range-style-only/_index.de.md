---
title: Nur Bereichsstil mit C++ kopieren
linktitle: Nur Bereichsstil kopieren
type: docs
weight: 620
url: /de/cpp/copy-range-style-only/
description: Lernen Sie, wie man nur den Stil eines Bereichs in Excel mit Aspose.Cells und C++ kopiert.
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/cpp/copy-range-data-only/) und [Bereichsdaten mit Stil kopieren](/cells/de/cpp/copy-range-data-with-style/) erklären, wie Daten aus einem Bereich auf einen anderen kopiert werden, entweder nur die Daten oder inklusive Formatierung. Es ist auch möglich, nur die Formatierung zu kopieren. Dieser Artikel zeigt wie.

{{% /alert %}} 

Dieses Beispiel erstellt ein Arbeitsblatt, füllt es mit Daten und kopiert nur den Stil eines Bereichs.

1. Erstellen Sie einen Bereich.
1. Erstellen Sie ein [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Erstellen Sie einen zweiten Zellenbereich.
1. Kopieren Sie die Formatierung des ersten Bereichs in den zweiten Bereich.

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
