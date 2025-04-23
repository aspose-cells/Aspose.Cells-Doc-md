---
title: Obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne avec C++
linktitle: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/cpp/get-max-index-in-row-and-column/
description: Découvrez comment obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne via l’API Aspose.Cells for C++.
keywords: Obtenir l indice de colonne maximal dans la rangée, obtenir l indice de rangée maximal dans la colonne, obtenir l indice de colonne de données maximal dans la rangée, obtenir l indice de rangée de données maximal dans la colonne.
---

## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler certaines données sur les lignes ou colonnes, vous devez connaître la plage de données des lignes et colonnes. Aspose.Cells offre cette fonction. Pour obtenir l’indice de la colonne maximale d’une ligne, vous pouvez obtenir les propriétés [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) et [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), puis utiliser la propriété [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) pour obtenir l’indice de la colonne maximale et l’indice de la colonne contenant le plus de données. Mais pour obtenir l’indice de la ligne maximale et l’indice de la dernière ligne de données d’une colonne, vous devez créer une plage sur cette colonne, parcourir cette plage pour trouver la dernière cellule, puis obtenir l’attribut [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) de cette cellule.

Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Obtenir l'indice de colonne maximal dans la rangée et l'indice de rangée maximal dans la colonne en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Obtenir l'attribut [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Obtenir l'attribut [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) sur la cellule.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
