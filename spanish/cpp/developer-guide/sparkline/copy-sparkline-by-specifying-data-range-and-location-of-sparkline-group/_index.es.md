---
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de Sparkline con C++
linktitle: Copiar Sparkline especificando el rango de datos y la ubicación
type: docs
weight: 300
url: /es/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aprenda cómo copiar sparklines especificando el rango de datos y la ubicación usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel le permite copiar una sparkline especificando el rango de datos y la ubicación de un grupo de sparkline. Aspose.Cells soporta esta funcionalidad.

{{% /alert %}}

Para copiar una minigráfica en otras celdas en Microsoft Excel:

1. Seleccione la celda que contiene la miniatura.
1. Seleccione **Editar datos** en la sección de **Miniatura** de la pestaña **Diseño**.
1. Seleccione **Editar ubicación y datos de grupo**.
1. Especifique el rango de datos y la ubicación.
1. Haz clic en **Aceptar**.

Aspose.Cells proporciona el método `SparklineCollection.Add(rangoDeDatos, fila, columna)` para especificar un rango de datos y una ubicación en un grupo de sparklines. El siguiente código de ejemplo carga el archivo de Excel de origen como se muestra en la captura de pantalla anterior, luego accede al primer grupo de sparklines y añade rangos de datos y ubicaciones en el grupo. Finalmente, escribe el archivo de Excel de salida en el disco, que también se muestra en la captura de pantalla anterior.

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
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
