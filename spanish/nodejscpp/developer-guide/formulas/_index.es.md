---
title: Gestión de fórmulas de archivos de Excel con Node.js a través de C++
linktitle: Fórmulas
type: docs
weight: 122
url: /es/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Aprende cómo gestionar las fórmulas de archivos de Excel a través de Aspose.Cells for Node.js via C++. Aspose.Cells puede obtener, establecer y calcular fórmulas de archivos de Excel de manera sencilla.
keywords: Cómo calcular fórmulas en Node.js a través de C++, Fórmulas y funciones usando Node.js a través de C++, Gestión de funciones integradas en Node.js a través de C++, Cómo usar funciones de complemento con Node.js a través de C++, Cómo usar fórmulas de matriz en Node.js a través de C++, Cómo usar fórmulas R1C1 en Node.js a través de C++.
---

## **Introducción**

Una de las funciones más atractivas de Microsoft Excel es su capacidad de procesar datos con fórmulas y funciones. Microsoft Excel ofrece un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también soporta funciones de complemento. Además, Aspose.Cells soporta fórmulas de matriz y R1C1.

## **Cómo Usar Fórmulas y Funciones**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección Cells representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Es posible aplicar fórmulas a celdas utilizando propiedades y métodos ofrecidos por la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), discutidos con más detalle a continuación.

- Usar funciones incorporadas.
- Usar funciones de complemento.
- Trabajar con fórmulas de matriz.
- Crear una fórmula R1C1.

## **Cómo Usar Funciones Incorporadas**

Las funciones o fórmulas integradas se proporcionan como funciones prediseñadas para reducir esfuerzos y tiempo del desarrollador. Consulta [una lista de funciones integradas](/cells/es/nodejs-cpp/supported-formula-functions/) soportadas por Aspose.Cells. Las funciones están listadas en orden alfabético. Se soportarán más funciones en el futuro.

Aspose.Cells soporta la mayoría de las fórmulas o funciones ofrecidas por Microsoft Excel. Los desarrolladores pueden usar estas fórmulas a través de la API o [diseñador de hojas de cálculo](/cells/es/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells soporta un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, bases de datos, búsqueda y referencia.

Utilice la propiedad [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) para agregar una fórmula a una celda. **Las fórmulas complejas**, por ejemplo

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son compatibles en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

En el ejemplo a continuación, se aplica una fórmula compleja a la primera celda de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la hoja de cálculo. La fórmula utiliza una función integrada de **SI** proporcionada por Aspose.Cells.

```javascript
const path = require("path");
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

## **Cómo Usar Funciones de Complemento**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Al configurar la función de celda.Formula, las funciones incorporadas funcionan bien, sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones de complemento.

Aspose.Cells proporciona funciones para registrar funciones de complemento utilizando [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Posteriormente, cuando establecemos cell.Formula = anyFunctionFromAddIn, el archivo de Excel de salida contiene el valor calculado de la función de complemento.

A continuación, se deberá descargar el archivo XLAM para registrar la función del complemento en el código de muestra siguiente. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar el resultado.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Cómo usar fórmulas de matriz**

Las fórmulas de matriz son fórmulas que toman matrices, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}).

Algunas funciones de Microsoft Excel devuelven matrices de valores. Para calcular múltiples resultados con una fórmula de matriz, introduzca la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

Es posible aplicar una fórmula de matriz a una celda llamando al método [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). El método [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) toma los siguientes parámetros:

- **Fórmula de matriz**, la fórmula de matriz.
- **Número de filas**, el número de filas para poblar el resultado de la fórmula de matriz.
- **Número de columnas**, el número de columnas para poblar el resultado de la fórmula de matriz.

```javascript
const path = require("path");
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

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Cómo usar la fórmula de R1C1**

Agregue una fórmula de estilo de referencia **R1C1** a una celda con la propiedad [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Temas avanzados**
- [Precedentes y Dependientes](/cells/es/nodejs-cpp/precedents-and-dependents/)
- [Establecer vínculos externos en fórmulas](/cells/es/nodejs-cpp/set-external-links-in-formulas/)
- [Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas](/cells/es/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Estableciendo fórmula para rango con nombre](/cells/es/nodejs-cpp/setting-formula-for-named-range/)
- [Establecer fórmulas - Aviso para usuarios no angloparlantes](/cells/es/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Establecer fórmula compartida](/cells/es/nodejs-cpp/setting-shared-formula/)
- [Especificar el número máximo de filas de la fórmula compartida](/cells/es/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel soportadas](/cells/es/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}
