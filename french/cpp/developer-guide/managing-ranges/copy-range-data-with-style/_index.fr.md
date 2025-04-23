---
title: Copier les données de la plage avec style en C++
linktitle: Copier les données de la plage avec style
type: docs
weight: 610
url: /fr/cpp/copy-range-data-with-style/
description: Copier les données de la plage y compris les styles de cellules dans des fichiers Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Copier uniquement les données de la plage](/cells/fr/cpp/copy-range-data-only/) expliqué comment copier des données entre des plages. Cet article démontre comment copier des plages tout en préservant leurs styles de mise en forme en utilisant Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells fournit des classes et des méthodes pour travailler avec des plages, notamment [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) et [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Cet exemple montre comment :

1. Créer un classeur
1. Remplir les cellules avec des données
1. Créer un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Créer et configurer un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)
1. Appliquer des styles à la plage
1. Créer une seconde plage
1. Copier des données formatées entre des plages

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
