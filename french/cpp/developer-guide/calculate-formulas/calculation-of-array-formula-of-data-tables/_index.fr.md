---
title: Calcul de la formule matricielle des tables de données avec C++
linktitle: Calcul de la formule de tableau de données
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer les formules matricielles d une table de données dans Microsoft Excel avec C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour calculer la formule matricielle de la table de données et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, tableaux de données, formules matricielles, calculs, C++
type: docs
weight: 70
url: /fr/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Vous pouvez créer un tableau de données dans Microsoft Excel en utilisant Données > Analyse de scénarios > Table de données... Aspose.Cells vous permet maintenant de calculer la formule de tableau de données. Veuillez utiliser [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) comme d'habitude pour calculer n'importe quel type de formules.

{{% /alert %}}

Dans le code d'exemple suivant, nous avons utilisé le [fichier Excel source](5115535.xlsx). Si vous changez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies de couleur jaune deviendront 120 comme indiqué dans les images suivantes. Le code d'exemple génère le [PDF de sortie](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Voici le code d'exemple utilisé pour générer le [PDF de sortie](5115538.pdf) à partir du [fichier Excel source](5115535.xlsx). Veuillez lire les commentaires pour plus d'informations.

```cpp
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
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
