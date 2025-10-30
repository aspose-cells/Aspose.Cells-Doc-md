---
title: Convertir el Smart Art a forma agrupada con C++
linktitle: Convertir el Arte Inteligente en Forma de Grupo
type: docs
weight: 200
url: /es/cpp/convert-the-smart-art-to-group-shape/
description: Aprenda cómo convertir una forma Smart Art en Forma Agrupada usando Aspose.Cells for C++ y acceder a las partes individuales del grupo de formas.
---

## **Escenarios de uso posibles**

Puedes convertir la forma de arte inteligente en una forma de grupo usando el método [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/). Te permitirá manejar la forma de arte inteligente como una forma de grupo. En consecuencia, tendrás acceso a las partes o formas individuales de la forma de grupo.

## **Convertir el Arte Inteligente en Forma de Grupo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](55541793.xlsx) que contiene una forma de smart art como se muestra en esta captura de pantalla. Luego convierte la forma de smart art en forma de grupo e imprime la propiedad Shape::IsGroup. Consulta la salida en consola del código de ejemplo a continuación.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
