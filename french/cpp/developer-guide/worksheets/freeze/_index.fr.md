---
title: Geler les volets de la feuille Excel avec C++
linktitle: Geler les volets
type: docs
weight: 190
url: /fr/cpp/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez comment geler les volets des feuilles Excel de manière programmatique en utilisant la bibliothèque C++ avec l API Aspose.Cells.
keywords: Geler les volets, Geler la fenêtre.
---

## **Introduction**

Dans cet article, nous verrons comment geler les volets. Lorsque vous avez une grande quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille vers le bas. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets pour voir cette partie gelée même lorsque le reste des données est en cours de défilement. Vous pouvez facilement voir les en-têtes dans les premières lignes ou les premières colonnes. Geler et dégeler les volets ne modifient que la vue des données, sans changer les données elles-mêmes.

## **Dans Excel**

**![Geler les volets dans Excel](Freeze-panes.png)**

1. Si vous souhaitez geler les volets, geler les lignes et les colonnes, sélectionnez d'abord une cellule (par exemple B2).
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler les volets.
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne restent figées.

**![Fenêtres figées](Frozen-Panes.png)**

Comme vous pouvez le voir, la 1ère ligne et la colonne A sont figées, la deuxième ligne est 32, et la deuxième colonne visible est D.

Les fenêtres figées vous permettent de voir vos grandes données sans suivre les étiquettes de lignes ou de colonnes.

## **Figer les fenêtres avec Aspose.Cells for C++**
Il est simple de figer les fenêtres avec Aspose.Cells for C++. Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) pour figer les fenêtres à la cellule sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figer les fenêtres avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Fichier Excel source [exemple joint](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
