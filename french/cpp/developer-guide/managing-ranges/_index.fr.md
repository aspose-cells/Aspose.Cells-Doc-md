---
title: Gérer des plages avec C++
linktitle: Plages
type: docs
weight: 105
url: /fr/cpp/managing-ranges/
description: Apprenez à gérer des plages dans les fichiers Excel en utilisant Aspose.Cells avec C++. Créez, modifiez et stylisez des plages de manière programmatique.
---

## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection de zone à la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans la cellule "A1" d'Excel, puis faire glisser jusqu'à la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Plage".

## **Gestion des plages à l'aide de Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Placer une valeur dans les cellules de la plage**

Imaginons que vous avez une plage de cellules qui s'étend sur A1:C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées de manière séquentielle : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définir le style des cellules de la plage**

L'exemple suivant montre comment définir le style des cellules de la plage.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Obtenir la région actuelle de la plage**

CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle. 

La région actuelle est une plage délimitée par une combinaison de lignes vierges et de colonnes vierges. En lecture seule.

Dans Excel, vous pouvez obtenir la région actuelle en :
1. Sélectionnez une zone (plage1) avec la boîte de souris.
2. Cliquez sur "Accueil - Modification - Recherche et sélection - Atteindre une spécificité - Région actuelle", ou utilisez "Ctrl+Maj+*", vous verrez qu'Excel vous aide automatiquement à sélectionner une zone (plage2), maintenant vous l'avez fait, la plage2 est la région actuelle de la plage1.

En utilisant Aspose.Cells, vous pouvez utiliser la propriété "Range.CurrentRegion" pour effectuer la même fonction.

Veuillez télécharger le fichier de test suivant, l'ouvrir dans Excel, utiliser la boîte de souris pour sélectionner une zone "A1:D7", puis cliquer sur "Ctrl+Maj+*", vous verrez que la zone "A1:C3" est sélectionnée.

[current_region.xlsx](current_region.xlsx)

Veuillez exécuter l'exemple suivant pour voir comment cela fonctionne dans Aspose.Cells :

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/cpp/autofill-ranges/)
- [Copier des plages de cellules d'Excel](/cells/fr/cpp/copy-ranges-of-Excel/)
- [Copier uniquement les données de la plage](/cells/fr/cpp/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/cpp/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/cpp/copy-range-style-only/)
- [Créer l'union de la plage](/cells/fr/cpp/create-union-range/)
- [Couper et coller la plage](/cells/fr/cpp/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/cpp/delete-ranges-from-Excel/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/cpp/insert-ranges-to-Excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/cpp/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/cpp/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées en fonction du classeur et de la feuille de calcul](/cells/fr/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/cpp/search-and-replace-data-in-a-range/)
