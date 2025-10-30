---
title: Reutilización de objetos de estilo con C++
linktitle: Reutilización de Objetos de Estilo
description: En Aspose.Cells for C++, mediante la creación y uso de objetos de estilo reutilizables, puede simplificar la gestión de estilos y mejorar la eficiencia del código. Nuestra guía le ayudará a aprovechar las ventajas de los objetos de estilo reutilizables e implementarlos en su aplicación.
keywords: Aspose.Cells for C++, Reutilización de objetos de estilo, Gestión de estilos, Eficiencia del código, Estilos reutilizables, Desarrollo de aplicaciones, Referencia API, Código de ejemplo, Descargar, Soporte.
type: docs
weight: 3000
url: /es/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Reutilizar objetos de estilo puede ahorrar memoria y hacer que un programa sea más rápido.

{{% /alert %}}

Para aplicar un formato a un gran rango de celdas en una hoja de cálculo:

1. Cree un objeto de estilo.
1. Especifique los atributos.
1. Aplique el estilo a las celdas en el rango.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Debido a que el enfoque [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) utiliza mucha menos memoria y es eficiente, la propiedad Cell.Style más antigua que consumía mucha memoria innecesaria, se eliminó con el lanzamiento de Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
