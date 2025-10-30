---
title: Trabajar con la Formatting 3D de forma o gráfico con C++
linktitle: Trabajar con el Formato ThreeD de la Forma o Gráfico
type: docs
weight: 250
url: /es/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Aprende cómo manipular el formato 3D de formas o gráficos usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) junto con la clase [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) para trabajar con el formato 3D de formas o gráficos. La clase [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) contiene diferentes propiedades que se pueden configurar para lograr diferentes resultados según los requisitos de la aplicación.

## **Trabajar con el Formato ThreeD de la Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115419.xlsx) y accede a la primera forma en la primera hoja de trabajo. Luego configura las subpropiedades de la propiedad [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) y guarda el libro en el [archivo de Excel de salida](5115410.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
