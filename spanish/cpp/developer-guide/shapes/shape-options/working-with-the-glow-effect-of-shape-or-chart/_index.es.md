---
title: Trabajar con el efecto de resplandor de forma o gráfico con C++
linktitle: Trabajar con el efecto de resplandor de la forma o el gráfico
type: docs
weight: 240
url: /es/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Aprende cómo trabajar con el efecto de resplandor de formas o gráficos usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) junto con la clase [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) para trabajar con el efecto de resplandor de la forma o gráfico. La clase [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) contiene las siguientes propiedades que se pueden configurar para lograr diferentes resultados según los requisitos de la aplicación.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Trabajando con el Efecto de Resplandor de Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115407.xlsx) y accede a la primera forma en la primera hoja de trabajo y configura las subpropiedades de la propiedad [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) y luego guarda el libro en [archivo de Excel de salida](5115414.xlsx).

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
