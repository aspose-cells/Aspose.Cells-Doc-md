---
title: Supprimer les lignes en double dans une feuille de calcul avec C++
linktitle: Supprimer les lignes en double dans une feuille de calcul
type: docs
weight: 370
url: /fr/cpp/remove-duplicate-rows-in-a-worksheet/
description: Apprenez comment supprimer les lignes en double dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

La suppression des lignes en double est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Elle permet aux utilisateurs de supprimer les lignes en double dans une feuille de calcul, et vous pouvez choisir quelles colonnes vérifier pour les informations en double.

Aspose.Cells fournit la méthode `Cells::RemoveDuplicates()` à cet effet. Vous pouvez également définir `startRow`, `startColumn`, `endRow`, et `endColumn` pour sélectionner des colonnes.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
