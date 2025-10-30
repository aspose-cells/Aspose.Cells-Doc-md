---
title: Calcular fórmulas con Golang mediante C++
linktitle: Calcular Fórmulas
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para calcular fórmulas en Microsoft Excel con Golang mediante C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para calcular la fórmula y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, fórmulas, cálculos, Cálculo Directo de Fórmula, Calcular Fórmulas repetidamente, agregar fórmulas.
type: docs
weight: 125
url: /es/go-cpp/calculate-formulas/
---

## **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. No solo puede recalcular fórmulas importadas de plantillas de diseñador, sino que también soporta calcular los resultados de fórmulas añadidas en tiempo de ejecución.

Aspose.Cells soporta la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel (Lee [una lista de las funciones soportadas por el motor de cálculo](/cells/es/cpp/supported-formula-functions/)). Estas funciones pueden usarse a través de las APIs o hojas de cálculo de diseñador. Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de bases de datos, de búsqueda y referencia.

Utiliza las propiedades [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) o los métodos [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comienza la cadena con un signo igual (=) como cuando creas una fórmula en Microsoft Excel y usa una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de fórmulas, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que procesa todas las fórmulas incrustadas en un archivo de Excel. O, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), que procesa todas las fórmulas incrustadas en una hoja. O, el usuario puede también llamar al método [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), que procesa la fórmula de una celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Importante saber para las Fórmulas**

{{% alert color="primary" %}}

La propiedad **GetFormula** y los métodos **SetFormula(...)** de la clase [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) funcionan de manera diferente a los métodos **Calculate** de las clases [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) y [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). La propiedad **GetFormula** y los métodos **SetFormula(...)** simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, por favor llama a los métodos **Calculate**.

{{% /alert %}}

## **Cálculo directo de fórmulas**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. Además de calcular las fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular directamente los resultados de las fórmulas.

A veces, necesitas calcular los resultados de una fórmula directamente sin agregarla a una hoja de cálculo. Los valores de las celdas usadas en la fórmula ya existen en una hoja de cálculo, y todo lo que necesitas es encontrar el resultado de esos valores en base a alguna fórmula de Excel sin añadir la fórmula en una hoja.

Puedes usar las APIs del motor de cálculo de fórmulas de Aspose.Cells para [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) a [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) los resultados de esas fórmulas sin agregarlas a la hoja de cálculo:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
El código anterior produce la siguiente salida:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Cómo calcular fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Importante saber**

{{% alert color="primary" %}}

Por defecto, la cadena de cálculo está deshabilitada. Porque crear la cadena también requiere tiempo adicional, la primera vez que se calculan fórmulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) puede consumir más tiempo de procesamiento de CPU y memoria en comparación con calcular fórmulas sin una cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular la fórmula directamente sin crear una cadena de cálculo) debería ser la mejor opción.

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
