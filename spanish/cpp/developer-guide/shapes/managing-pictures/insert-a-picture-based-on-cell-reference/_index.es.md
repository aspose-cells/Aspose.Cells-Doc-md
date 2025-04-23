---
title: Inserte una imagen basada en la referencia de celda con C++
linktitle: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/cpp/insert-a-picture-based-on-cell-reference/
description: Aprenda cómo insertar una imagen basada en la referencia de celda usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells soporta mostrar el contenido de una celda de hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Debido a que la celda o rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico. Agrega una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Especifica el rango de celdas usando el atributo [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) del objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Ejemplo de código

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
