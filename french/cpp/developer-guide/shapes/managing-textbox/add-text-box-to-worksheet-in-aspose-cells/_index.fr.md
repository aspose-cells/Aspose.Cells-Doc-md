---
title: Comment ajouter/inclure une boîte de texte dans la feuille de calcul avec C++
linktitle: Ajouter une zone de texte à une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Comment ajouter/inclure une boîte de texte dans la feuille de calcul dans Aspose.Cells avec C++.
keywords: Ajouter/insérer une zone de texte dans une feuille de calcul Excel avec Aspose
---

## Ajouter une zone de texte à une feuille de calcul dans Excel

Dans le programme Excel (version 07 et supérieure), il y a deux endroits où vous pouvez insérer des zones de texte. L'un dans "insert-shapes", l'autre en haut à droite du menu "Insert".

### Méthode 1 :

![1](1.png)

### Méthode 2 :

![2](2.png)

## Comment créer

Vous pouvez créer des zones de texte à texte horizontal ou vertical.

- Sélectionner l'option correspondant (horizontal ou vertical)
- Cliquez sur la page avec le bouton gauche de la souris
- Maintenez le bouton gauche enfoncé et faites glisser une distance sur la page
- Relâchez le bouton gauche

Maintenant, vous avez une zone de texte.

## Ajouter une zone de texte à une feuille de calcul dans Aspose.Cells

Lorsque vous devez insérer en masse des zones de texte dans la feuille de calcul, la méthode d'insertion manuelle est évidemment une catastrophe. Si cela vous dérange, je pense que ce document vous aidera. [Aspose.Cells](https://products.aspose.com/cells/) fournit une API pour effectuer facilement des insertions en masse dans votre code.

Le code d'exemple suivant crée une zone de texte.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vous obtiendrez un fichier similaire à [fichier résultat](result.xlsx). Dans ce fichier, vous verrez ce qui suit :

![](52449.png)
