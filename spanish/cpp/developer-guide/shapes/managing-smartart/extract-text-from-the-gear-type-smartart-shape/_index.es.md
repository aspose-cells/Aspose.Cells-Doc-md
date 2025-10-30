---
title: Extraer texto de la forma SmartArt de tipo engranaje con C++
linktitle: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 500
url: /es/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aprenda cómo extraer texto de formas de SmartArt de tipo engranaje en Excel usando Aspose.Cells for C++ con orientación paso a paso y ejemplos de código.
---

## **Escenarios de uso posibles**

Aspose.Cells for C++ puede extraer texto de la forma de SmartArt de tipo engranaje. Para lograrlo, siga estos pasos:
1. Convertir la forma de SmartArt en forma de grupo usando el método [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4).
2. Recuperar todas las formas individuales que forman la forma de grupo usando el método [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
3. Iterar a través de cada forma individual y extraer el texto usando el método [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de ejemplo carga un [archivo de Excel de muestra](67338483.xlsx) que contiene una forma de SmartArt de tipo engranaje y extrae texto de sus formas individuales. Consulte la salida en consola a continuación para obtener los resultados.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
