---
title: Calcular fórmulas con Node.js vía C++
linktitle: Calcular Fórmulas
description: Este artículo presenta cómo utilizar la biblioteca Aspose.Cells para calcular fórmulas en Microsoft Excel usando Node.js vía C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para calcular la fórmula y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, fórmulas, cálculos, Cálculo directo de fórmulas, calcular fórmulas repetidamente, agregar fórmulas en Node.js vía C++
type: docs
weight: 125
url: /es/nodejs-cpp/calculate-formulas/
---

## **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. No solo puede recalcular fórmulas importadas de plantillas de diseñador, sino que también soporta calcular los resultados de fórmulas añadidas en tiempo de ejecución.

Aspose.Cells soporta la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel (Leer [una lista de las funciones soportadas por el motor de cálculo](/cells/es/nodejs-cpp/supported-formula-functions/)). Esas funciones pueden ser usadas a través de las APIs o hojas de cálculo de diseñador. Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de base de datos, búsqueda y referencia.

Utiliza las propiedades [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) o los métodos [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comienza la cadena con un signo igual (=) como cuando creas una fórmula en Microsoft Excel y usa una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de fórmulas, el usuario puede llamar al método [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que procesa todas las fórmulas incrustadas en un archivo Excel. O bien, el usuario puede llamar al método [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) que procesa todas las fórmulas incrustadas en una hoja. O también, puede llamar al método [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) que procesa la fórmula de una sola celda:

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Importante saber para las Fórmulas**

{{% alert color="primary" %}}

La propiedad **Formula** y los métodos **setFormula(...)** de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) funcionan de manera diferente a los métodos **calculate** de las clases [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) y [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). La propiedad **Formula** y los métodos **setFormula(...)** simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo real. Para obtener el resultado de las fórmulas, por favor llama a los métodos **calculate**.

{{% /alert %}}

## **Cálculo directo de fórmulas**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. Además de calcular las fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular directamente los resultados de las fórmulas.

A veces, necesitas calcular los resultados de una fórmula directamente sin agregarla a una hoja de cálculo. Los valores de las celdas usadas en la fórmula ya existen en una hoja de cálculo, y todo lo que necesitas es encontrar el resultado de esos valores en base a alguna fórmula de Excel sin añadir la fórmula en una hoja.

Puedes usar las APIs del motor de cálculo de fórmulas de Aspose.Cells para [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) los resultados de esas fórmulas sin agregarlas a la hoja de cálculo:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

El código anterior produce la siguiente salida:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Cómo Calcular Fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente mientras modifica solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Importante saber**

{{% alert color="primary" %}}

Por defecto, la cadena de cálculo está deshabilitada. Debido a que crear la cadena también requiere más tiempo, el primer cálculo de fórmulas ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) puede consumir más tiempo de CPU y memoria en comparación con calcular fórmulas sin cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento por defecto (calcular la fórmula directamente sin crear una cadena de cálculo) debería ser la mejor opción.

{{% /alert %}}

## **Temas avanzados**
- [Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel](/cells/es/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Cálculo de la función IFNA utilizando Aspose.Cells](/cells/es/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmulas de matriz de tablas de datos](/cells/es/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Cálculo de las funciones MINIFS y MAXIFS de Excel 2016](/cells/es/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Disminuir el tiempo de cálculo del método Cell.calculate](/cells/es/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detección de referencia circular](/cells/es/nodejs-cpp/detecting-circular-reference/)
- [Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo](/cells/es/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar un motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrumpir o cancelar el cálculo de fórmulas de una hoja de cálculo](/cells/es/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Devolver un rango de valores utilizando AbstractCalculationEngine](/cells/es/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Configurar el modo de cálculo de fórmulas de una hoja de cálculo](/cells/es/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Usando la función FormulaText en Aspose.Cells](/cells/es/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
