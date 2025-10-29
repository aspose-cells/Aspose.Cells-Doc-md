---
title: Comment contrôler la barre d onglets de feuilles avec C++
linktitle: Comment contrôler la barre d onglets de feuilles
type: docs
weight: 600
url: /fr/cpp/how-to-control-sheet-tab-bar/
description: Apprenez à contrôler la barre d onglets de la feuille via l API Aspose.Cells for C++.
keywords: Comment contrôler la barre d onglets de feuilles, Opérer la barre d onglets de feuilles, Définir la barre d onglets de feuilles, Contrôler la barre d onglets de feuilles. 
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez ajuster l'affichage de la barre de l'Excel, vous devez savoir comment contrôler la barre d'onglets, comme la masquer ou l'afficher, modifier la largeur de la barre d'onglets, spécifier le premier onglet visible, etc. Aspose.Cells supporte ces fonctionnalités. Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Comment contrôler la barre d'onglets de la feuille avec Aspose.Cells for C++**
Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Affichez l'onglet de feuille et définissez la largeur de la barre d'onglets.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aperçu du fichier résultat:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
