---
title: Nur Range Daten ohne Formatierung mit C++ kopieren
linktitle: Bereichsdaten nur kopieren
type: docs
weight: 600
url: /de/cpp/copy-range-data-only/
description: Erfahren Sie, wie Sie nur Range Daten ohne Formatierung mit Aspose.Cells und C++ kopieren.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Daten von einem Zellenbereich in einen anderen kopieren und nur die Daten, nicht die Formatierung. Aspose.Cells bietet diese Funktion an.

Dieser Artikel bietet einen Beispielcode, der Aspose.Cells verwendet, um einen Datenbereich zu kopieren.

{{% /alert %}}

Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) erstellen.
1. Erstellen Sie ein [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Einen weiteren Zellenbereich erstellen.
1. Kopieren Sie die Daten des ersten Bereichs in diesen zweiten Bereich.

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
