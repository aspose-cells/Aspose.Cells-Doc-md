---
title: Obtener valor de cadena de celda con y sin formato con C++
linktitle: Obtener valor de cadena de celda
type: docs
weight: 240
url: /es/cpp/get-cell-string-value-with-and-without-formatting/
description: Aprende cómo obtener el valor de cadena de una celda con y sin formato a través de la API Aspose.Cells for C++.
keywords: Obtener el valor de cadena de la celda con o sin formato, recuperar el valor de cadena de la celda con o sin formato, obtener el valor de cadena de la celda con o sin formato
---

{{% alert color="primary" %}}

Aspose.Cells proporciona un método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) que puede usarse para obtener el valor de cadena de la celda con o sin ningún formato. Supón que tienes una celda con valor 0.012345 y la formateaste para mostrar solo dos decimales. Entonces, mostrará como 0.01 en Excel. Puedes recuperar los valores de cadena tanto como 0.01 como 0.012345 usando el método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Este método toma el enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) con los siguientes valores:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- Estrategia de Formato de Valor de Celda::Cadena de Visualización
- Estrategia de Formato de Valor de Celda::Ninguno

{{% /alert %}}

El siguiente código de ejemplo explica el uso del método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
