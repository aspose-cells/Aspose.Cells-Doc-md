---
title: Copier uniquement les données de la plage avec C++
linktitle: Copier uniquement les données de la plage
type: docs
weight: 600
url: /fr/cpp/copy-range-data-only/
description: Apprenez comment copier uniquement les données de la plage sans mise en forme en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous devez copier des données d'une plage de cellules vers une autre, en copiant uniquement les données, pas la mise en forme. Aspose.Cells propose cette fonctionnalité.

Cet article fournit un code d'exemple qui utilise Aspose.Cells pour copier une plage de données.

{{% /alert %}}

Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Créer un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).
1. Créer un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) avec des attributs de mise en forme spécifiés.
1. Appliquer la mise en forme de style à la plage.
1. Créer une autre plage de cellules.
1. Copier les données de la première plage vers cette deuxième plage.

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
