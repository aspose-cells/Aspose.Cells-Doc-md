---
title: Annuler le gel des lignes ou des colonnes de la feuille de calcul Excel avec C++
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment dégeler de manière programmatique les lignes, colonnes ou volets des feuilles de calcul Excel en utilisant l’API Aspose.Cells for C++.
keywords: Dégeler les volets, dégeler des lignes, dégeler des colonnes, dégeler la fenêtre.
---

## **Introduction**

Dans cet article, nous apprendrons comment débloquer les lignes, colonnes et volets dans les feuilles de calcul Excel. Si les feuilles de calcul dans les fichiers Excel sont gelées, parfois nous souhaitons débloquer la feuille ou ajuster les lignes, colonnes ou volets gelés.

## **Dans Excel**

1. Cliquez sur l'onglet **Affichage** > **Figer les volets** > **Libérer les volets**.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**

## **Débloquer les lignes, colonnes ou volets avec Aspose.Cells for C++**
Il est simple de débloquer les volets avec Aspose.Cells for C++. Utilisez la méthode [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) pour débloquer les volets.

1. Construisez un objet `Workbook` pour ouvrir le fichier gelé.
2. Débloquez les volets en utilisant la méthode `Worksheet.UnFreezePanes()`.
3. Enregistrez le fichier.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Fichier Excel source joint (Frozen.xlsx).
