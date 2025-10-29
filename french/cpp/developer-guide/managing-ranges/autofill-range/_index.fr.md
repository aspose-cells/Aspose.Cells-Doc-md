---
title: Auto remplissage d une plage de fichiers Excel avec C++
linktitle: Plage de remplissage automatique
type: docs
weight: 105
url: /fr/cpp/autofill-ranges/
description: Apprenez comment effectuer une opération de remplissage automatique dans une plage spécifiée d un fichier Excel en utilisant Aspose.Cells avec C++.
---

## **Effectuer un remplissage automatique dans la plage spécifiée dans Excel**

Dans Excel, sélectionnez une plage, déplacez la souris dans le coin inférieur droit, et faites glisser le "+" pour remplir automatiquement les données.

## **Remplir automatiquement les plages avec Aspose.Cells**

L'exemple suivant montre comment effectuer une opération d'AutoRemplissage sur une Plage. Voici le fichier d'exemple qui peut être téléchargé pour tester cette fonctionnalité :

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
