---
title: Cacher et trier les données du tableau croisé dynamique avec C++
linktitle: Cacher et trier les données du tableau croisé dynamique
type: docs
weight: 120
url: /fr/cpp/pivot-table-hide-and-sort-data/
description: Apprenez comment cacher et trier les données dans les tableaux croisés dynamiques en utilisant Aspose.Cells avec C++.
---

## ** Cacher et trier les données du tableau croisé dynamique**
Aspose.Cells prend en charge la masquage et le tri des données dans le tableau croisé dynamique. Le code suivant démontre cette fonctionnalité en triant la colonne Score dans l'ordre décroissant, puis masque les lignes ayant un score inférieur à 60.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"PivotTableHideAndSortSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    CellArea dataBodyRange = pivotTable.GetDataBodyRange();
    int currentRow = 3;
    int rowsUsed = dataBodyRange.EndRow;

    // Sorting score in descending order
    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Hiding rows with score less than 60
    while (currentRow < rowsUsed)
    {
        Cell cell = worksheet.GetCells().Get(currentRow, 1);
        double score = cell.GetDoubleValue();
        if (score < 60)
        {
            worksheet.GetCells().HideRow(currentRow);
        }
        currentRow++;
    }

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the Excel file
    workbook.Save(outDir + u"PivotTableHideAndSort_out.xlsx");

    std::cout << "Pivot table hide and sort completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

 Les fichiers Excel source et de sortie utilisés dans l'extrait de code sont joints à titre de référence.

[Fichier source](96928093.xlsx)

[Fichier de sortie](96928094.xlsx)
