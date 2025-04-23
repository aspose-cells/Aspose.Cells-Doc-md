---
title: Enviar forma al frente o atrás dentro de la hoja de cálculo con C++
linktitle: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 3400
url: /es/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aprende cómo cambiar la posición del orden Z de las formas en una hoja de cálculo utilizando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando hay varias formas presentes en la misma ubicación, su visibilidad se determina por sus posiciones en el orden Z. Aspose.Cells proporciona el método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/), que cambia la posición del orden Z de la forma. Si deseas enviar una forma al fondo, usarás un número negativo como -1, -2, -3, etc. Si deseas traer una forma al frente, usarás un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El siguiente código de ejemplo demuestra el uso del método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/). Por favor, vea el [archivo de Excel de muestra](50528330.xlsx) utilizado en el código y el [archivo de Excel de salida](50528331.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarse.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
