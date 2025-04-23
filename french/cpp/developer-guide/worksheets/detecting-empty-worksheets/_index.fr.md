---
title: Détection des feuilles de calcul vides avec C++
linktitle: Détection de feuilles de calcul vides
type: docs
weight: 410
url: /fr/cpp/detecting-empty-worksheets/
description: Cet article vous montre un code expliquant comment détecter de manière programmatique les feuilles de calcul Excel vides en utilisant l API C++ avec la bibliothèque Aspose.Cells.
keywords: détecter une feuille de calcul vide c++, trouver une feuille Excel vide c++
---

## **Vérifier les cellules peuplées**

Les feuilles de calcul peuvent avoir une ou plusieurs cellules remplies de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans ce cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Tout ce que nous devons vérifier, ce sont les propriétés [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) ou [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). Si ces propriétés renvoient zéro ou des valeurs positives, cela signifie qu'une ou plusieurs cellules ont été remplies. Cependant, si l'une de ces propriétés renvoie -1, cela indique qu'aucune cellule n'a été remplie dans la feuille donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont un indice basé sur zéro, donc une cellule à la ligne 0 et la colonne 0 correspond à la première cellule de la feuille, qui est A1.

{{% /alert %}}

## **Vérifier les cellules initialisées vides**

Toutes les cellules qui ont des valeurs sont automatiquement initialisées. Cependant, il est possible qu'une feuille de calcul ait des cellules avec uniquement une mise en forme appliquée. Dans ce cas, les propriétés [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) ou [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) renverront -1, indiquant l'absence de valeurs remplies. Mais les cellules initialisées en raison de la mise en forme ne peuvent pas être détectées avec cette approche. Pour vérifier si une feuille de calcul a des cellules initialisées vides, il est conseillé d'utiliser la méthode `MoveNext` sur l'énumérateur obtenu à partir de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Si la méthode `MoveNext` renvoie **true**, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille.

## **Vérifier les formes**

Il est possible qu'une feuille donnée ne contienne aucune cellule remplie, mais qu'elle contienne des formes et des objets tels que des contrôles, des graphiques, des images, etc. Si nous devons vérifier si une feuille de calcul contient une forme, nous pouvons le faire en inspectant la propriété [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). Toute valeur positive indique la présence de forme(s) dans la feuille.

## **Exemple de programmation**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
