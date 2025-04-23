---
title: Configuration de la formule partagée avec C++
linktitle: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/cpp/setting-shared-formula/
description: Apprenez à définir des formules partagées dans les feuilles de calcul Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans une feuille de calcul qui effectuera des calculs, cet article explique comment réaliser cette tâche avec Aspose.Cells.

{{% /alert %}}

## Paramétrage de formule partagée avec Aspose.Cells

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

|**Fichier d'entrée avec une colonne de données**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/). Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites soit ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0,09, A4*0,09, A5*0,09, etc.). Cela nécessite la mise à jour des références de cellule pour chaque ligne. Cela nécessite aussi que Aspose.Cells analyse chaque formule individuellement, ce qui peut prendre du temps pour de grands tableaux et des formules complexes. Cela ajoute également des lignes de code supplémentaires, bien que des boucles puissent les réduire quelque peu.

Une autre approche est d'utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
