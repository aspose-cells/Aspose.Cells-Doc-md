---
title: Spécifier un avertissement de tri lors du tri des données avec C++
linktitle: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/cpp/specifying-sort-warning-while-sorting-data/
description: Apprenez comment spécifier un avertissement de tri lors du tri de données en utilisant l API Aspose.Cells for C++.
keywords: Ajouter un avertissement de tri lors du tri des données, définir un avertissement de tri lors du tri des données, sélectionner un avertissement de tri lors du tri des données.
---

## **Scénarios d'utilisation possibles**

Veuillez considérer ces données textuelles, c'est-à-dire {11, 111, 22}. Ces données textuelles sont triées parce que, en termes de texte, 111 vient avant 22. Mais si vous voulez trier ces données non pas comme du texte mais comme des chiffres, alors elles deviendront {11, 22, 111} car numériquement 111 vient après 22. Aspose.Cells fournit la propriété {0} pour résoudre ce problème. Veuillez définir cette propriété à **true** et vos données textuelles seront triées comme des données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles ressemblant à des données numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Code d'exemple**

Le code d'exemple suivant illustre l'utilisation de la propriété [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/) comme expliqué précédemment. Veuillez consulter son [fichier Excel d'exemple](43352075.xlsx) et son [fichier Excel de sortie](43352076.xlsx) pour plus d'aide.

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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
