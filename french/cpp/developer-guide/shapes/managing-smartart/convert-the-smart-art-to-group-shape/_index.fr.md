---
title: Convertir le Smart Art en Groupe de Formes avec C++
linktitle: Convertir l Art Smart en une Forme de Groupe
type: docs
weight: 200
url: /fr/cpp/convert-the-smart-art-to-group-shape/
description: Apprenez comment convertir une forme Smart Art en Groupe de Formes en utilisant Aspose.Cells for C++ et accéder aux parties individuelles du groupe de formes.
---

## **Scénarios d'utilisation possibles**

Vous pouvez convertir la forme de l'Art Smart en une forme de groupe en utilisant la méthode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/). Cela vous permettra de manipuler la forme de l'Art Smart comme une forme de groupe. Par conséquent, vous aurez accès aux parties ou formes individuelles de la forme de groupe.

## **Convertir l'Art Smart en une Forme de Groupe**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541793.xlsx) contenant une forme Smart Art comme montré dans cette capture d'écran. Il convertit ensuite la forme Smart Art en groupe de formes et affiche la propriété Shape::IsGroup. Veuillez voir la sortie de la console du code d'exemple ci-dessous.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
