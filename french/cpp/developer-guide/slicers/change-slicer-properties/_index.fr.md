---
title: Modifier les propriétés du segment dans C++
linktitle: Changer les propriétés de la trancheuse
type: docs
weight: 70
url: /fr/cpp/change-slicer-properties/
description: Modifiez les propriétés d un segment dans les fichiers Excel avec Aspose.Cells et C++.
---

## **Scénarios d'utilisation possibles**

Il peut arriver que vous souhaitiez changer les propriétés de la trancheuse telles que son emplacement ou sa hauteur de ligne. Aspose.Cells vous offre la possibilité de mettre à jour ces propriétés.

## **Modifier les propriétés du segmentateur**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite la trancheuse en fonction de la première colonne et modifie ses propriétés telles que la hauteur de ligne, la largeur, l'impression, le titre, etc. Il enregistre le classeur sous forme de [fichier Excel de sortie](outputChangeSlicerProperties.xlsx).

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
