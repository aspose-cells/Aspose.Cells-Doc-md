---
title: Agregar celdas a la ventana de observación de fórmulas de Microsoft Excel con C++
linktitle: Agregar celdas a la ventana de vigilancia de fórmulas
description: Aprende cómo usar Aspose.Cells for C++ para agregar celdas a la ventana de observación de fórmulas en Excel. Carga o crea un archivo de Excel, manipula celdas, establece fórmulas y guarda el archivo modificado.
keywords: Aspose.Cells, Excel, Ventana de Observación de Fórmulas, Celdas, Agregar, C++
type: docs
weight: 60
url: /es/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Escenarios de uso posibles**

La ventana de observación de Excel es una herramienta útil para monitorear fácilmente los valores de las celdas y sus fórmulas en una ventana. Puedes abrir la *Ventana de Observación* en Microsoft Excel haciendo clic en *Fórmulas > Ventana de Observación*. Tiene un botón *Agregar Observación* que se puede usar para agregar celdas para inspección. De manera similar, puedes usar el método [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) para agregar celdas a la *Ventana de Observación* usando la API de Aspose.Cells.

## **Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel**

El siguiente código de ejemplo establece la fórmula de las celdas C1 y E1 y las agrega a la Ventana de Observación. Luego guarda el libro como un [archivo de Excel de salida](67338481.xlsx). Si abres el archivo de Excel de salida y ves la *Ventana de Observación*, verás ambas celdas como se muestra en esta captura de pantalla.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
