---
title: Cortar y pegar rango con C++
linktitle: Cortar y Pegar Rango
type: docs
weight: 130
url: /es/cpp/cut-and-paste-cells/
description: Aprende cómo cortar y pegar celdas dentro de una hoja de trabajo usando Aspose.Cells for C++.
---

## **Cortar y Pegar Celdas**

Aspose.Cells te permite cortar y pegar celdas dentro de una hoja de trabajo usando el método [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) acepta los siguientes parámetros:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): El rango de celdas que se van a cortar.
- Índice de Fila: El índice de la fila para insertar celdas.
- Índice de Columna: El índice de la columna para insertar celdas.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): La dirección de desplazamiento de las columnas.

El siguiente ejemplo muestra cómo cortar y pegar celdas dentro de una hoja de cálculo.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
