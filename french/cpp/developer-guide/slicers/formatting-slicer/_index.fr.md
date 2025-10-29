---
title: Mise en forme du segment avec C++
linktitle: Formatage de la trancheuse
type: docs
weight: 20
url: /fr/cpp/formatting-slicer/
description: Formatage de coupeurs dans Microsoft Excel en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez formater le coupeur dans Microsoft Excel en réglant son nombre de colonnes ou en définissant son style, etc. Aspose.Cells vous permet également de faire cela en utilisant les propriétés [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) et [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## **Formatage d'un tronçonneur**

Veuillez voir le code suivant ; il charge le [fichier Excel d'exemple](67338473.xlsx) contenant un coupeur. Il accède au coupeur, règle le nombre de colonnes et le type de style, puis l'enregistre en tant que [fichier Excel de sortie](67338474.xlsx). La capture d'écran montre à quoi ressemble le coupeur après l'exécution du code exemple.

![todo:image_alt_text](formatting-slicer_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
