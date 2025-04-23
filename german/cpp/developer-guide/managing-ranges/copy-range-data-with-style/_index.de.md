---
title: Bereichsdaten mit Stil in C++ kopieren
linktitle: Bereichsdaten mit Format kopieren
type: docs
weight: 610
url: /de/cpp/copy-range-data-with-style/
description: Bereichsdaten einschließlich Zellformatierungen in Excel Dateien mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/cpp/copy-range-data-only/) erklärt, wie man Zellendaten zwischen Bereichen kopiert. Dieser Artikel demonstriert, wie man Zellbereiche beim Erhalt ihrer Formatierungen mit Aspose.Cells for C++ kopiert.

{{% /alert %}}

Aspose.Cells bietet Klassen und Methoden für die Arbeit mit Bereichen, einschließlich [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) und [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Dieses Beispiel demonstriert, wie man:

1. Ein Arbeitsbuch erstellt
1. Zellen mit Daten füllt
1. Ein [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) erstellt
1. Ein [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekt erstellt und konfiguriert
1. Stil auf den Bereich anwenden
1. Einen zweiten Bereich erstellen
1. Formatierten Daten zwischen Bereichen kopieren

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
