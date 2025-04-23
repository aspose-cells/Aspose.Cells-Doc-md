---
title: Tri des données avec C++
linktitle: Tri des données
type: docs
weight: 130
url: /fr/cpp/sort-data-of-excel/
description: Apprenez comment trier des données en utilisant l’API Aspose.Cells for C++.
keywords: Trier les données par ordre croissant ou décroissant, trier les données en fonction de la couleur de fond
---

{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Il permet aux utilisateurs d'ordonner les données pour les rendre plus faciles à scanner. Aspose.Cells permet aux développeurs de trier les données de la feuille de calcul par ordre alphabétique ou numérique, ce qui fonctionne de la même manière que Microsoft Excel pour trier les données.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

## **Trier les données avec Aspose.Cells**

Aspose.Cells fournit la classe [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) utilisée pour trier les données par ordre croissant ou décroissant. La classe a des membres importants, par exemple, des propriétés comme Key1 ... Key3 et Order1 ... Order3. Ces membres sont utilisés pour définir les clés triées et spécifier l'ordre de tri des clés.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), les cellules de la feuille de calcul sous-jacente.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après l'exécution du code ci-dessous, les données sont triées correctement.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si vous souhaitez trier *de gauche à droite*, utilisez l'attribut [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Tri des données avec couleur de fond**

Excel propose des fonctionnalités pour trier les données en fonction de la couleur de fond. La même fonctionnalité est fournie en utilisant Aspose.Cells en utilisant DataSorter où [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor peut être utilisé dans [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) pour trier les données en fonction de la couleur de fond. Toutes les cellules qui contiennent la couleur spécifiée dans le [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), la fonction sont placées en haut ou en bas en fonction du paramètre SortOrder et l'ordre des autres cellules n'est pas du tout modifié.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/cpp/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/cpp/specifying-sort-warning-while-sorting-data/)
