---
title: Poblar datos primero por fila y luego por columna con C++
linktitle: Primero llenar datos por fila y luego por columna
type: docs
weight: 1000
url: /es/cpp/populate-data-first-by-row-then-by-column/
description: Aprende cómo poblar datos primero por fila y luego por columna mediante la API Aspose.Cells for C++.
keywords: Llenar datos primero por fila y luego por columna, insertar datos primero por fila y luego por columna, agregar datos primero por fila y luego por columna, inserción de datos de alto rendimiento, adición de datos de alto rendimiento
---

{{% alert color="primary" %}} 

Llenar una hoja de cálculo con datos primero por fila y luego por columna mejora el rendimiento general.

{{% /alert %}} 

Poner datos en la secuencia A1, B1, A2, B2 es más rápido que A1, A2, B1, B2. Si hay muchas celdas en una hoja de cálculo y sigues la segunda secuencia, es decir, estás llenando los datos fila por fila, este consejo puede hacer que el programa sea mucho más rápido.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
