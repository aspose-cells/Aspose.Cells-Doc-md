---
title: Définir la bordure de plage avec C++
type: docs
weight: 600
url: /fr/cpp/set-range-border/
description: Apprenez à définir les bordures de plage avec Aspose.Cells en C++.
---

## **Scénarios d'utilisation possibles**
Lorsque vous souhaitez définir la bordure d’une plage, vous n’avez pas besoin de définir chaque cellule individuellement. Vous pouvez définir la bordure sur toute la plage. Aspose.Cells offre cette fonctionnalité. Cet article fournit un exemple de code utilisant Aspose.Cells pour définir la bordure de plage.

## **Définir la bordure de la plage dans Excel**
Pour définir la bordure d'une plage dans Excel, vous pouvez suivre ces étapes :
1. Sélectionnez la plage de cellules sur laquelle vous souhaitez appliquer la bordure.
2. Dans l'onglet « Accueil » du ruban, localisez le groupe « Police ».
3. Dans le groupe « Police », cliquez sur le bouton déroulant « Bordures ».
<br>
<img src="border.png" />
4. Choisissez le type de bordure que vous souhaitez appliquer parmi les options du menu déroulant. Vous pouvez choisir parmi les styles de bordure prédéfinis ou personnaliser votre propre bordure.
5. Une fois que vous avez sélectionné le style de bordure souhaité, la bordure sera appliquée à la plage de cellules sélectionnée.

## **Définir la bordure de la plage en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Créer un classeur.
2. Ajouter des données aux cellules de la première feuille de calcul.
3. Créer un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Définir la bordure intérieure de la plage.
5. Définir la bordure extérieure de la plage.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
