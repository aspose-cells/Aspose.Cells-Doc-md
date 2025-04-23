---
title: Fixer la ou les premières colonnes de la feuille Excel avec C++
linktitle: Geler les colonnes
type: docs
weight: 190
url: /fr/cpp/how-to-freeze-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment fixer les colonnes de gauche des feuilles Excel de manière programmatique en utilisant la bibliothèque C++ avec l API Aspose.Cells.
keywords: Fixer les colonnes de gauche, Fixer la ou les premières colonnes, Verrouiller la ou les colonnes
---

## **Introduction**

Dans cet article, nous apprendrons comment fixer la ou les premières colonnes. Lorsque vous avez une grande quantité de données dans une ligne, vous ne pouvez pas voir les colonnes de gauche lorsque vous faites défiler la feuille horizontalement. Vous pouvez fixer et verrouiller la ou les premières colonnes afin de voir cette partie figée même lorsque les autres données défilent. Vous pouvez facilement voir les en-têtes dans les colonnes de gauche.

## **Geler les colonnes dans Excel**

**![Geler la ou les premières colonnes dans Excel](freeze-columns.png)**

1. Si vous souhaitez fixer la ou les colonnes de gauche, sélectionnez d'abord la colonne sous la colonne qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Fixer la première colonne.
4. Si vous faites défiler vers le bas, la première colonne reste toujours visible à gauche.

**![Colonne figée](frozen-columns.png)**

Comme vous pouvez le voir, la 1ère colonne est figée, la première colonne reste toujours verrouillée en haut de la vue lorsque vous faites défiler horizontalement.

Fixer les colonnes vous permet de voir vos longues données sans suivre la première colonne.

## **Fixer les colonnes avec Aspose.Cells for C++**
Il est simple de fixer la ou les premières colonnes avec Aspose.Cells for C++. 
Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) pour figer la ou les colonnes à la colonne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Fixer la première colonne avec la méthode Worksheet.FreezePanes().
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

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Fichier Excel source [exemple joint](Freeze.xlsx).
