---
title: Comment insérer une image dans une cellule avec C++
linktitle: Comment insérer une image dans une cellule
type: docs
weight: 130
url: /fr/cpp/how-to-insert-picture-in-cell/
description: Découvrez comment insérer une image dans une cellule avec Aspose.Cells en utilisant C++.
keywords: Comment insérer une image dans une cellule, insérer une image sur des cellules, placer une image dans une cellule, placer une image sur des cellules, comment placer une image dans une cellule, comment placer une image sur des cellules, passer de l image dans la cellule à l image sur les cellules, passer de l emplacement dans la cellule à l emplacement sur les cellules.
---

## **Scénarios d'utilisation possibles**
L'image ajoute une touche de luminosité à votre feuille de calcul et offre une représentation visuelle du contenu. Elle facilite également la compréhension des données et la génération d'insights. Bien que vous ayez pu utiliser des images dans Excel depuis de nombreuses années, la fonctionnalité permettant que les images deviennent des valeurs de cellule réelles n’a été activée que récemment. Même si la disposition du dessin est modifiée, elle restera attachée aux données. Vous pouvez l'utiliser dans des tableaux, trier, filtrer, l'inclure dans des formules, etc. !

## **Comment insérer une image dans une cellule en utilisant Excel**
Pour insérer une image dans une cellule d'Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer dans la cellule**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="1.png" width=60% />
3. Sélectionnez l'image et insérez-la dans une cellule.
<br>
<img src="8.png" width=60% />

## **Comment insérer une image sur des cellules en utilisant Excel**
Pour insérer une image sur des cellules dans Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer sur des cellules**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="2.png" width=60% />
3. Sélectionnez l'image et insérez-la sur des cellules.
<br>
<img src="3.png" width=60% />

## **Comment passer de l'image dans la cellule à l'image sur les cellules en utilisant Excel**
Vous pouvez facilement passer de **l'image dans la cellule** à **l'image sur les cellules**. Veuillez suivre ces étapes :
1. Cliquez avec le bouton droit sur la cellule et sélectionnez **Image dans la cellule** > **Placer sur des cellules**. 
<br>
<img src="4.png" width=60% />
2. Le résultat après le changement est le suivant :
<br>
<img src="5.png" width=60% />

## **Comment passer de l'image sur les cellules à l'image dans la cellule en utilisant Excel**
Vous pouvez facilement passer de **l'image sur les cellules** à **l'image dans la cellule**. Veuillez suivre ces étapes :
1. Cliquez avec le bouton droit sur l'image et sélectionnez **Placer dans la cellule**. 
<br>
<img src="6.png" width=60% />
2. Le résultat après le changement est le suivant :
<br>
<img src="7.png" width=60% />

## **Comment insérer une image dans une cellule en utilisant C++**
Insérer une image dans une cellule en utilisant Aspose.Cells. Veuillez consulter le code d'exemple suivant. Après avoir exécuté l'exemple de code, une image sera insérée dans une cellule.
1. Instancier un objet Workbook. 
2. Obtenez la cellule où vous souhaitez insérer l'image.
3. Définissez la propriété Cell.EmbeddedImage. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

## **Code d'exemple**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
