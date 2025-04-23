---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos con C++
linktitle: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende cómo verificar si el valor de la celda cumple con las reglas de validación de datos a través de la API Aspose.Cells for C++.
keywords: Obtener valor de validación de la celda, obtener valor de validación de la celda, verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Excel muestra un mensaje de error y solicita ingresar un número en el rango correcto. Si copias y pegas un número, por ejemplo 3, en la celda, Excel no realiza una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 

## **Introducción**
Aspose.Cells proporciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) para validar los valores de las celdas programáticamente. Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve **False**, de lo contrario, **True**.

El siguiente código de ejemplo ilustra cómo funciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). Primero, ingresa el valor 3 en C1. Debido a que esto no cumple con la regla de validación de datos, el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) devuelve **False**. Luego, ingresa el valor 15 en C1. Debido a que este valor cumple con la regla de validación de datos, el método devuelve **True**. De manera similar, devuelve **False** para el valor 30.

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Salida**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
