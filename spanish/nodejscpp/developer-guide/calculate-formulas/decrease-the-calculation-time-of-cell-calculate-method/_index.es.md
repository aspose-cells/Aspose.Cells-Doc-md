---  
title: Reducir el tiempo de cálculo del método Cell.Calculate con Node.js vía C++  
linktitle: Reducir el tiempo de cálculo del método Cell.Calculate  
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para reducir el tiempo de cálculo de los métodos de cálculo de celdas en Excel usando Node.js vía C++.  
keywords: Aspose.Cells, Excel, métodos de cálculo de celdas, optimización, rendimiento, reducción del tiempo de cálculo, Node.js vía C++  
type: docs  
weight: 100  
url: /es/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Escenarios de uso posibles**

Normalmente, recomendamos a los usuarios llamar al método [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) una vez y luego obtener los valores calculados de las celdas individuales. Pero a veces, los usuarios no quieren calcular todo el libro de trabajo. Solo quieren calcular una sola celda. Aspose.Cells proporciona la propiedad [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), que puedes establecer en **false** para disminuir significativamente el tiempo de cálculo de celdas individuales. Cuando la propiedad recursiva está establecida en **true**, entonces se recalculan todos los dependientes de las celdas en cada llamada. Sin embargo, cuando la propiedad recursiva es **false**, las celdas dependientes se calculan solo una vez y no se recalculan en llamadas subsiguientes.

## **Disminuir el tiempo de cálculo del método Cell.calculate()**

El código de muestra a continuación ilustra el uso de la propiedad [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). Por favor, ejecuta este código con el archivo de Excel de muestra dado y verifica su salida en la consola. Encontrarás que establecer la propiedad recursiva en **false** ha disminuido significativamente el tiempo de cálculo. También lee los comentarios para entender mejor esta propiedad.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Set the calculation option, set recursive true or false as per parameter
const opts = new AsposeCells.CalculationOptions();
opts.setRecursive(rec);

// Start stop watch            
const start = process.hrtime();

// Calculate cell A1 one million times
for (let i = 0; i < 1000000; i++) {
ws.getCells().get("A1").calculate(opts);
}

// Stop the watch
const end = process.hrtime(start);

// Calculate elapsed time in seconds
const estimatedTime = end[0] + end[1] / 1e9;

// Print the elapsed time in seconds
console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior cuando se ejecuta con el archivo de Excel de muestra en nuestra máquina. Ten en cuenta que tu salida puede diferir, pero el tiempo transcurrido después de establecer la propiedad recursiva en **false** siempre será menor que al establecerla en **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
