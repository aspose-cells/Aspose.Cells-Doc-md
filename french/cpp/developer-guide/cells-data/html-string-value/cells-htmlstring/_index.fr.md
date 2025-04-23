---
title: Gérer la chaîne HTML des cellules avec C++
linktitle: Gérer les chaînes HTML des cellules
type: docs
weight: 600
url: /fr/cpp/manage-cells-html-string/
description: Apprenez à gérer la chaîne HTML des cellules via l API Aspose.Cells for C++.
keywords: Ajouter une chaîne HTML à l intérieur de la cellule, Définir une chaîne HTML à l intérieur de la cellule, Ajouter une chaîne HTML, Obtenir la chaîne HTML de la cellule, Gérer les chaînes HTML des cellules
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez définir des données stylisées pour une cellule spécifique, vous pouvez attribuer une chaîne HTML à cette cellule. Bien sûr, vous pouvez également obtenir la chaîne HTML de la cellule. Aspose.Cells offre cette fonctionnalité. Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Obtenir et définir une chaîne html en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Obtenir la cellule spécifique dans la première feuille de calcul.
1. Définir une chaîne html dans la cellule.
1. Obtenir une chaîne html de la cellule.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Sortie générée par le code d'exemple

La capture d'écran suivante montre la sortie du code d'exemple ci-dessus.

![todo:image_alt_text](htmlstring.png)
