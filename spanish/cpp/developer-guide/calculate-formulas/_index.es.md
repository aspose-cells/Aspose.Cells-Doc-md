---
title: Calcular fórmulas con C++
linktitle: Calcular Fórmulas
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para calcular fórmulas en Microsoft Excel con C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para calcular la fórmula y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, fórmulas, cálculos, Cálculo Directo de Fórmula, Calcular Fórmulas repetidamente, agregar fórmulas.
type: docs
weight: 125
url: /es/cpp/calculate-formulas/
---

## **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. No solo puede recalcular fórmulas importadas de plantillas de diseñador, sino que también soporta calcular los resultados de fórmulas añadidas en tiempo de ejecución.

Aspose.Cells soporta la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel (Lee [una lista de las funciones soportadas por el motor de cálculo](/cells/es/cpp/supported-formula-functions/)). Estas funciones pueden usarse a través de las APIs o hojas de cálculo de diseñador. Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de bases de datos, de búsqueda y referencia.

Utiliza las propiedades [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) o los métodos [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comienza la cadena con un signo igual (=) como cuando creas una fórmula en Microsoft Excel y usa una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de fórmulas, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que procesa todas las fórmulas incrustadas en un archivo de Excel. O, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), que procesa todas las fórmulas incrustadas en una hoja. O, el usuario puede también llamar al método [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), que procesa la fórmula de una celda.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Importante saber para las Fórmulas**

{{% alert color="primary" %}}

La propiedad **GetFormula** y los métodos **SetFormula(...)** de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) funcionan de manera diferente a los métodos **Calculate** de las clases [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) y [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). La propiedad **GetFormula** y los métodos **SetFormula(...)** simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, por favor llama a los métodos **Calculate**.

{{% /alert %}}

## **Cálculo directo de fórmulas**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. Además de calcular las fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular directamente los resultados de las fórmulas.

A veces, necesitas calcular los resultados de una fórmula directamente sin agregarla a una hoja de cálculo. Los valores de las celdas usadas en la fórmula ya existen en una hoja de cálculo, y todo lo que necesitas es encontrar el resultado de esos valores en base a alguna fórmula de Excel sin añadir la fórmula en una hoja.

Puedes usar las APIs del motor de cálculo de fórmulas de Aspose.Cells para [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) los resultados de esas fórmulas sin agregarlas a la hoja de cálculo:

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

El código anterior produce la siguiente salida:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Cómo calcular fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Importante saber**

{{% alert color="primary" %}}

Por defecto, la cadena de cálculo está deshabilitada. Porque crear la cadena también requiere tiempo adicional, la primera vez que se calculan fórmulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) puede consumir más tiempo de procesamiento de CPU y memoria en comparación con calcular fórmulas sin una cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular la fórmula directamente sin crear una cadena de cálculo) debería ser la mejor opción.

{{% /alert %}}

## **Temas Avanzados**
- [Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel](/cells/es/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Cálculo de la función IFNA utilizando Aspose.Cells](/cells/es/cpp/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmulas de matriz de tablas de datos](/cells/es/cpp/calculation-of-array-formula-of-data-tables/)
- [Cálculo de las funciones MINIFS y MAXIFS de Excel 2016](/cells/es/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Reducir el tiempo de cálculo del método Cell.Calculate](/cells/es/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo](/cells/es/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar un motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Devolver un rango de valores utilizando AbstractCalculationEngine](/cells/es/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Configurar el modo de cálculo de fórmulas de una hoja de cálculo](/cells/es/cpp/setting-formula-calculation-mode-of-workbook/)
- [Usando la función FormulaText en Aspose.Cells](/cells/es/cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
