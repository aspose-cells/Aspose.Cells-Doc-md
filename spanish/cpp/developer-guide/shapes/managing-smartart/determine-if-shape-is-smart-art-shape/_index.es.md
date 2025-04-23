---
title: Determinar si una forma es una forma Smart Art con C++
linktitle: Determinar si la Forma es una Forma de Arte Inteligente
type: docs
weight: 400
url: /es/cpp/determine-if-shape-is-smart-art-shape/
description: Aprenda cómo determinar si una forma es una forma Smart Art usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Las Formas de Arte Inteligente son formas especiales en Microsoft Excel que permiten crear diagramas complejos automáticamente. Puedes saber si la forma es una forma de arte inteligente o una forma normal usando la propiedad [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/).

## **Determinar si la Forma es una Forma de Arte Inteligente**

El siguiente código de muestra carga el [archivo Excel de muestra](55541792.xlsx) que contiene una forma de arte inteligente como se muestra en esta captura de pantalla. Luego imprime el valor de la propiedad [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) de la primera forma. Consulte la salida de la consola del código de muestra a continuación.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
