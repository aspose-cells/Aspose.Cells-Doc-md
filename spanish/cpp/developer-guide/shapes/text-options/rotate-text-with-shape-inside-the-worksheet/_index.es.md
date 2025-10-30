---
title: Rotar texto con forma dentro de la hoja de cálculo con C++
linktitle: Rotar texto con forma
type: docs
weight: 1300
url: /es/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aprenda a controlar la rotación del texto con formas en hojas de cálculo de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puede agregar texto dentro de cualquier forma utilizando Microsoft Excel. Si agrega una forma usando la muy antigua Microsoft Excel 2003, entonces el texto no rotará con la forma. Sin embargo, si agrega una forma usando versiones más recientes de Microsoft Excel, como 2007, 2010, 2013 o 2016, el texto rotará con la forma. Puede controlar si el texto debe rotar con la forma o no usando la propiedad [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/). El valor predeterminado de esta propiedad es **true**, lo que significa que el texto rotará con la forma. Si lo configura como **false**, el texto no rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716896.xlsx) que contiene una forma de triángulo, y su texto rota con la forma. Si abre el archivo de Excel de muestra en Microsoft Excel y rota la forma del triángulo, el texto también rotará con ella. Luego el código establece la propiedad [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) en **false** y lo guarda como el [archivo de Excel de salida](64716897.xlsx). Si ahora abre el archivo de Excel de salida en Microsoft Excel y rota la forma del triángulo, el texto no rotará con ella. Por favor, vea la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra como referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
