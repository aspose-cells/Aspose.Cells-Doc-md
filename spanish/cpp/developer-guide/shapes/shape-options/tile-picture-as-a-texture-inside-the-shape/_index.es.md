---
title: Imagen de mosaico como textura dentro de la forma con C++
linktitle: Colocar imagen como textura dentro de la forma
type: docs
weight: 1700
url: /es/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Aprende cómo mosaico una imagen como textura dentro de una forma usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando la imagen es pequeña y no cubre toda la superficie de la forma sin perder su calidad, entonces tiene la opción de colocarla como textura. Colocar como textura llena la superficie de la forma con una imagen pequeña repitiéndola como si fueran azulejos.

## **Colocar imagen como textura dentro de la forma**

Puede llenar la superficie de la forma con alguna imagen y colocarla como textura utilizando la propiedad [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) y configurándola en **true**. Consulte el siguiente código de ejemplo, su [archivo de Excel de muestra](46465050.xlsx) así como la captura de pantalla para su referencia.

## **Captura de pantalla**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
