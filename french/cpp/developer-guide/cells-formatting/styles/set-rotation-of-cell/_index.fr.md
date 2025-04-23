---
title: Comment faire pivoter le texte d une cellule avec C++
linktitle: Comment faire pivoter le texte de la cellule
type: docs
weight: 80
url: /fr/cpp/how-to-rotate-text-of-cell/
description: Code C++ pour faire pivoter le texte d’une cellule avec l’API Aspose.Cells for C++
keywords: c++ faire pivoter le texte d une cellule, c++ faire pivoter le texte de la cellule dans le classeur de manière programmatique, définir l’angle de rotation de la cellule par programmation dans le classeur, c++ comment faire pivoter le texte d’une cellule dans excel
---

## **Faire pivoter le texte de la cellule dans Aspose.Cells**

Aspose.Cells est un composant C++ puissant qui permet aux développeurs de travailler avec des feuilles de calcul Excel de manière programmatique. L'une des fonctionnalités fournies par Aspose.Cells est la capacité de faire pivoter les cellules, permettant de personnaliser l’orientation du texte et d’améliorer la présentation visuelle de vos données. Dans ce document, nous explorerons comment faire pivoter des cellules avec Aspose.Cells.

## **Comment faire pivoter le texte d'une cellule dans Excel**
Pour faire pivoter une cellule dans Excel, vous pouvez suivre les étapes suivantes :
1. Ouvrez Excel et sélectionnez la cellule ou la plage de cellules que vous souhaitez faire pivoter.
1. Cliquez avec le bouton droit sur la(des) cellule(s) sélectionnée(s) et choisissez "Format de cellule" dans le menu contextuel. Vous pouvez également accéder à l'onglet "Accueil" dans le ruban Excel, cliquer sur le menu déroulant "Format" dans le groupe "Cellules" et sélectionner "Format de cellule".
1. Dans la boîte de dialogue "Format de cellule", accédez à l'onglet "Alignement".
1. Sous la section "Orientation", vous verrez les options pour faire pivoter le texte. Vous pouvez directement saisir l'angle de rotation souhaité en degrés dans la zone "Degrés". Les valeurs positives font pivoter le texte dans le sens inverse des aiguilles d'une montre, et les valeurs négatives le font pivoter dans le sens des aiguilles d'une montre.
<br>
![todo:image_alt_text](alignment.png)
1. Une fois que vous avez sélectionné la rotation souhaitée, cliquez sur "OK" pour appliquer les modifications. La(des) cellule(s) sélectionnée(s) sera(seront) maintenant pivotée(s) en fonction de l'angle de rotation ou de l'orientation choisi(e).

## **Comment faire pivoter le texte d'une cellule en utilisant l'API Aspose.Cells**

La propriété [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) facilite la rotation des cellules. Pour faire pivoter les cellules dans Aspose.Cells, vous devez suivre ces étapes :
1. Charger le classeur Excel
<br>
Tout d'abord, vous devez charger le classeur Excel en utilisant Aspose.Cells. Vous pouvez utiliser la classe Workbook pour ouvrir un fichier Excel existant ou en créer un nouveau. 

1. Accéder à la feuille de calcul
<br>
Une fois le classeur chargé, vous devez accéder à la feuille de calcul où vous souhaitez faire pivoter les cellules. Vous pouvez accéder à la feuille de calcul soit par son index, soit par son nom. 

1. Faire pivoter le texte de la cellule
<br>
Maintenant que vous avez accès à la feuille de calcul, vous pouvez faire pivoter les cellules en modifiant l'objet Style des cellules désirées. L'objet Style vous permet de définir diverses options de mise en forme, y compris la rotation. 

1. Enregistrer le classeur
<br>
Après avoir fait pivoter les cellules, vous pouvez enregistrer le classeur modifié dans un fichier ou un flux en utilisant la méthode Save.

## **Exemple de code C++**

Veuillez consulter le code suivant, il crée un objet classeur et définit différents angles de rotation pour plusieurs cellules. La capture d'écran montre le résultat après l'exécution du code exemple.
<br>
<img src="rotation.png" width=80% />

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
