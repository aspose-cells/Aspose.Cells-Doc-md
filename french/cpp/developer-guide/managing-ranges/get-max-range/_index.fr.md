---
title: Obtenir la plage maximale dans une feuille de calcul avec C++
linktitle: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/cpp/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage maximale, la plage de données maximale et la plage de visualisation maximale des fichiers Excel avec la bibliothèque Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.

Lors de l'exportation d'une zone spécifiée en HTML et PDF, nous devons connaître la zone maximale.

Aspose.Cells for C++ propose différentes manières de trouver la plage maximale dans une feuille de calcul. 

{{% /alert %}} 

## **Obtenir la plage maximale**
Dans Aspose.Cells, si les objets [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) et [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) sont initialisés, ces lignes et colonnes seront comptabilisées jusqu'à la zone maximale, même s'il n'y a aucune donnée dans les lignes ou colonnes vides.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Obtenir la plage de données maximale**
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètre concernant les formes, les tableaux et les tableaux croisés dynamiques seront ignorés.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment rendre la plage d'affichage maximale en HTML :

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Voici le [fichier excel source](Book1.xlsx).
