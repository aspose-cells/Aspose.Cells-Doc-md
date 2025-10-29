---
title: Comment contrôler la vue du classeur avec C++
linktitle: Comment contrôler la vue du classeur
type: docs
weight: 600
url: /fr/cpp/how-to-control-workbook-view/
description: Apprenez comment contrôler la vue du classeur en utilisant l API Aspose.Cells for C++.
keywords: Comment contrôler la vue du classeur, Définir la vue Excel, Opérer la vue du classeur, Définir la vue du classeur, Contrôler la vue Excel.
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez ajuster l'affichage des pages Excel, vous devez savoir comment contrôler chaque module, comme les barres de défilement horizontales et verticales, si vous souhaitez masquer les fichiers Excel ouverts, etc. Aspose.Cells offre cette fonctionnalité. Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.

- [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)
- [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)
- [**WorkbookSettings.IsHidden**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishidden/)
- [**WorkbookSettings.IsMinimized**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isminimized/)
- [**WorkbookSettings.GetWindowHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowheight/)
- [**WorkbookSettings.GetWindowWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowwidth/)
- [**WorkbookSettings.GetWindowLeft()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowleft/)
- [**WorkbookSettings.GetWindowTop()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowtop/)

## **Comment contrôler la vue du classeur en utilisant Aspose.Cells for C++**
Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Masquer les barres de défilement horizontales et verticales de la vue du classeur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
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

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    // Apply style to cell E10
    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    // Hide horizontal and vertical scrollbars
    workbook.GetSettings().SetIsHScrollBarVisible(false);
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

Aperçu du fichier résultat:
<br>
<image src="result.png" width="70%" />
{{< app/cells/assistant language="cpp" >}}
