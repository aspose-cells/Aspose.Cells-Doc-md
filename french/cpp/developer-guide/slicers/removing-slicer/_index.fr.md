---
title: Suppression du coupeur avec C++
linktitle: Suppression de la trancheuse
type: docs
weight: 30
url: /fr/cpp/removing-slicer/
description: Apprenez comment supprimer les coupeurs dans les fichiers Excel de manière programmatique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez supprimer un coupeur dans Microsoft Excel, il suffit de le sélectionner et d'appuyer sur le bouton *Supprimer*. De même, si vous souhaitez le supprimer en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/). Cela supprimera le coupeur de la feuille de calcul.

## **Suppression du tronçonneur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338478.xlsx) qui contient une trancheuse existante. Il accède aux tranches et les supprime. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](67338477.xlsx). La capture d'écran suivante montre la trancheuse qui sera supprimée après l'exécution du code d'exemple.

![todo:image_alt_text](removing-slicer_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
