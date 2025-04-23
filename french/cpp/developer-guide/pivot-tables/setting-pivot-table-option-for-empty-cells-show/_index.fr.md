---
title: Configurer l option du tableau croisé dynamique  Pour les cellules vides, afficher avec C++
linktitle: Définir l option du tableau croisé dynamique  Afficher les cellules vides
type: docs
weight: 40
url: /fr/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Apprenez comment définir l option "Pour les cellules vides, afficher" dans les tableaux croisés dynamiques avec Aspose.Cells en C++.
---

{{% alert color="primary" %}}

Vous pouvez définir différentes options de tableau croisé dynamique à l'aide d'Aspose.Cells. L'une de ces options est "Afficher pour les cellules vides". En définissant cette option, toutes les cellules vides dans un tableau croisé dynamique s'affichent en tant que chaîne spécifiée.

{{% /alert %}}

## **Définition de l'option de tableau croisé dynamique dans Microsoft Excel**

Pour trouver et définir cette option dans Microsoft Excel :

1. Sélectionnez un tableau croisé dynamique et faites un clic droit.
1. Sélectionnez **Options du tableau croisé dynamique**.
1. Sélectionnez l'onglet **Mise en page et format**.
1. Sélectionnez l'option **Afficher pour les cellules vides** et spécifiez une chaîne.

## **Définition de l'option de tableau croisé dynamique à l'aide d'Aspose.Cells**

Aspose.Cells propose les propriétés [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) et [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) pour définir l'option de tableau croisé dynamique "Afficher pour les cellules vides".

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
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articles Connexes

- [Formatage du tableau croisé dynamique](/cells/fr/cpp/formatting-pivot-table/)
