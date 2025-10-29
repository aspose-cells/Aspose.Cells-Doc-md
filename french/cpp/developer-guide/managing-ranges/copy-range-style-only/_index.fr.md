---
title: Copier uniquement le style de la plage avec C++
linktitle: Copier uniquement le style de la plage
type: docs
weight: 620
url: /fr/cpp/copy-range-style-only/
description: Apprenez comment copier uniquement le style d une plage dans Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

[Copier uniquement les données de la plage](/cells/fr/cpp/copy-range-data-only/) et [Copier les données de la plage avec style](/cells/fr/cpp/copy-range-data-with-style/) expliquent comment copier des données d'une plage à une autre en solo ou entièrement avec la mise en forme. Il est aussi possible de copier uniquement la mise en page. Cet article montre comment.

{{% /alert %}} 

Cet exemple crée un classeur, le remplit de données et copie uniquement le style d'une plage.

1. Créer une plage.
1. Créer un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) avec des attributs de mise en forme spécifiés.
1. Appliquer la mise en forme de style à la plage.
1. Créer une deuxième plage de cellules.
1. Copier la mise en forme de la première plage vers la deuxième plage.

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
