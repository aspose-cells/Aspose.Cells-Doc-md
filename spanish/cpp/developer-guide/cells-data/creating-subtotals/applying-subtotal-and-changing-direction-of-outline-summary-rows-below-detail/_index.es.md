---
title: Aplicando subtotal y cambiando la dirección de las filas de resumen del contorno debajo de los detalles con C++
linktitle: Aplicar subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
type: docs
weight: 100
url: /es/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aprenda cómo aplicar subtotal y cambiar la dirección de las filas de resumen del contorno debajo de los detalles usando la API Aspose.Cells for C++.
keywords: Aplicar subtotal, agregar subtotal, cambiar dirección del resumen de contorno de filas debajo del detalle, cambiar dirección del resumen de contorno de columnas a la derecha del detalle, crear subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
---

{{% alert color="primary" %}}

Este artículo explicará cómo aplicar subtotal a los datos y cambiar la dirección de las filas de resumen del contorno debajo de los detalles.

Puede aplicar subtotal a los datos usando el método [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/). Toma los siguientes parámetros:

- **ÁreaCelda** - El rango en el que aplicar el subtotal
- **AgruparPor** - El campo por el que agrupar, como un desplazamiento entero basado en cero
- **Función** - La función de subtotal
- **ListaTotal** - Una matriz de desplazamientos de campo basados en cero, que indica los campos a los que se añaden los subtotales.
- **Reemplazar** - Indica si reemplazar los subtotales actuales
- **Saltos de página** - Indica si agregar saltos de página entre grupos
- **Resumen debajo de los datos** - Indica si agregar resumen debajo de los datos.

Además, puedes controlar la dirección de las filas de resumen **Resumen debajo de los detalles** en contorno como se muestra en la siguiente captura usando la propiedad `Worksheet.Outline.SummaryRowBelow`. Puedes abrir esta configuración en Microsoft Excel usando **Datos > Contorno > Configuración**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Imágenes de los archivos de origen y salida

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de ejemplo. Como se puede ver, se ha aplicado un subtotal al rango A2:B11 y la dirección del contorno es resumen de filas debajo del detalle.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Código C++ para aplicar subtotal y cambiar la dirección de las filas de resumen del contorno

Aquí está el código de ejemplo para lograr el resultado mostrado anteriormente.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
