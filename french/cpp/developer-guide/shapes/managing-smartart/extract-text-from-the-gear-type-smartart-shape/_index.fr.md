---
title: Extraire le texte de la forme SmartArt de type Engrenage avec C++
linktitle: Extraire du texte de la forme SmartArt de type équipement
type: docs
weight: 500
url: /fr/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Apprenez comment extraire du texte des formes SmartArt de type Engrenage dans Excel en utilisant Aspose.Cells for C++ avec un guide étape par étape et des exemples de code.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for C++ peut extraire le texte de la forme SmartArt de type Engrenage. Pour y parvenir, suivez ces étapes :
1. Convertir la forme SmartArt en groupe de formes en utilisant la méthode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4).
2. Récupérer toutes les formes individuelles composant le groupe de formes en utilisant la méthode [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
3. Parcourir chaque forme individuelle et en extraire le texte en utilisant la méthode [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **Extraire du texte de la forme SmartArt de type équipement**

Le code d'exemple suivant charge un [fichier Excel d'exemple](67338483.xlsx) contenant une forme SmartArt de type Engrenage et en extrait le texte de ses formes individuelles. Consultez la sortie de la console ci-dessous pour voir les résultats.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
