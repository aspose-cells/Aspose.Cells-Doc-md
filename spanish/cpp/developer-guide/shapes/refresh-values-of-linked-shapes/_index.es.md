---
title: Actualiza los valores de formas enlazadas con C++
linktitle: Actualizar valores de formas vinculadas
type: docs
weight: 3200
url: /es/cpp/refresh-values-of-linked-shapes/
description: Aprende cómo actualizar los valores de formas enlazadas en archivos de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, tienes una forma vinculada en tu archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells si quieres guardar tu libro de trabajo en formato XLS o XLSX. Sin embargo, si deseas guardar tu libro de trabajo en formato PDF o HTML, entonces tendrás que llamar al método [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

La siguiente captura muestra el archivo Excel fuente usado en el ejemplo de código a continuación. Tiene una imagen enlazada a las celdas A1 a E4. Cambiaremos el valor de la celda B4 con Aspose.Cells y luego llamaremos al método [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) para actualizar el valor de la imagen y guardarla en formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puedes descargar el [archivo Excel fuente](95584291.xlsx) y el [PDF de salida](95584292.pdf) desde los enlaces proporcionados.

### Código C++ para actualizar los valores de formas enlazadas

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
