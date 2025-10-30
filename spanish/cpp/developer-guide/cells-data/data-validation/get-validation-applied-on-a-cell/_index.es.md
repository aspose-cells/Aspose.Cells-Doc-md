---
title: Obtener validación aplicada a una celda con C++
linktitle: Obtener validación aplicada en una celda
type: docs
weight: 200
url: /es/cpp/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con C++.
keywords: aplicar validación de celda en Excel con C++, aplicar validación en una celda en Excel con C++, aplicar validación en Excel con C++, validación de celda en Excel con C++, C++ aplicar validación en celda en Excel, C++ aplicar validación en una celda en Excel, validación de celda en Excel con C++, validación de celda con C++
---

{{% alert color="primary" %}}

Puede usar Aspose.Cells para obtener la validación aplicada a una celda. Aspose.Cells proporciona el método [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) para este fin. Si no hay validación aplicada en la celda, devuelve nulo.

De manera similar, puede usar el método [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

## Código en C++ para obtener la validación aplicada en una celda

El siguiente ejemplo de código muestra cómo obtener la validación aplicada en una celda.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access its first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Access the validation applied on this cell
    Validation validation = cell.GetValidation();

    // Read various properties of the validation
    std::cout << "Reading Properties of Validation" << std::endl;
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Type: " << static_cast<int>(validation.GetType()) << std::endl;
    std::cout << "Operator: " << static_cast<int>(validation.GetOperator()) << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Artículos relacionados

- [Validación de datos](/cells/es/cpp/data-validation/)
{{< app/cells/assistant language="cpp" >}}
