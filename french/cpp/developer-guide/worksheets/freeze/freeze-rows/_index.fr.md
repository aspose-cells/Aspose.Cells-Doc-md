---
title: Fixer la première ligne de la feuille Excel avec C++
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/cpp/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer de manière programmatique les lignes supérieures des feuilles de calcul Excel à l aide de la bibliothèque C++ avec l API Aspose.Cells.
keywords: Figer les premières lignes, Figer la première ligne.
---

## **Introduction**

Dans cet article, nous apprendrons comment figer la ou les premières lignes. Lorsque vous avez une grande quantité de données sous une entête commune, vous ne pouvez pas voir l'entête lorsque vous faites défiler la feuille de calcul. Vous pouvez figer la ou les premières lignes pour voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les lignes du haut.

## **Figer les rangées dans Excel**

**![Figer la rangée(s) supérieure(s) dans Excel](Freeze-Rows.png)**

1. Si vous souhaitez figer la ou les premières lignes, sélectionnez d'abord la ligne sous celle qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Figer la rangée supérieure.
4. Si vous faites défiler vers le bas, la première ligne reste toujours en vue en haut.

**![Ligne figée](Frozen-Row.png)**

Comme vous pouvez le voir, la première ligne est figée, et la première ligne reste toujours en haut de la vue lorsque vous faites défiler.

Figer des lignes vous permet de visualiser vos grandes données sans perdre la trace de l’étiquette de ligne.

## **Figer des lignes avec Aspose.Cells for C++**
Il est simple de figer la ou les lignes avec Aspose.Cells for C++. 
Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) pour figer la ou les lignes à la ligne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figez la première ligne avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Fichier Excel source d'exemple joint [échantillon](../Freeze.xlsx).
