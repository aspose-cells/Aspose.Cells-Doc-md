---
title: Supprimer les lignes et colonnes vides dans une feuille de calcul avec C++
linktitle: Supprimer les lignes et colonnes vides dans une feuille de calcul
type: docs
weight: 300
url: /fr/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Supprimer les lignes et colonnes vides dans une feuille de calcul à l aide d Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Il est possible de supprimer toutes les lignes et colonnes vides d'une feuille de calcul. Cela est utile, par exemple, lors de la génération d'un fichier PDF à partir d'un fichier Microsoft Excel et que vous souhaitez ne convertir que les lignes et colonnes contenant des données ou des objets liés.

Utilisez les méthodes Aspose.Cells suivantes pour supprimer les lignes et colonnes vides :

1. Pour supprimer les lignes vides, utilisez la méthode [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/). Veuillez noter que, pour les lignes vides qui seront supprimées, il est non seulement nécessaire que [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) soit vrai, mais il ne doit également y avoir aucun commentaire visible défini pour une quelconque cellule de ces lignes, et aucun tableau croisé dynamique dont la plage intersecte avec elles.
2. Pour supprimer des colonnes vides, utilisez la méthode [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/).

{{% /alert %}}

## Code C++ pour supprimer des lignes vides

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Code C++ pour supprimer des colonnes vides

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
