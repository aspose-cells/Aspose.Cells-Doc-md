---
title: Déterminer si la forme est une forme Smart Art avec C++
linktitle: Déterminer si la forme est une forme de l Art Smart
type: docs
weight: 400
url: /fr/cpp/determine-if-shape-is-smart-art-shape/
description: Apprenez à déterminer si une forme est une forme Smart Art en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Les formes de l'Art Smart sont des formes spéciales dans Microsoft Excel qui permettent de créer automatiquement des diagrammes complexes. Vous pouvez savoir si la forme est une forme de l'Art Smart ou une forme normale en utilisant [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) propriété.

## **Déterminer si la forme est une forme de l'Art Smart**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541792.xlsx) contenant une forme de l'Art Smart comme indiqué dans cette capture d'écran. Ensuite, il affiche la valeur de la propriété [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) de la première forme. Veuillez consulter la sortie de la console du code d'exemple ci-dessous.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
