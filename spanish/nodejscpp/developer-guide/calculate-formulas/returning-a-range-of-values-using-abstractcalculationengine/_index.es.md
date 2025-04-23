---
title: Devolver un rango de valores usando AbstractCalculationEngine con Node.js vía C++
linktitle: Devolver un rango de valores utilizando AbstractCalculationEngine
description: Este artículo introduce un motor de cálculo abstracto que devuelve un rango de valores en Excel usando la biblioteca Aspose.Cells para Node.js vía C++. Aprende a cargar o crear un archivo de Excel y guardar el archivo modificado en disco.
keywords: Aspose.Cells, Excel, motor de cálculo abstracto que devuelve valores Node.js vía C++, funciones personalizadas
type: docs
weight: 55
url: /es/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) que se utiliza para implementar funciones personalizadas que no son compatibles con Microsoft Excel como funciones integradas.

Este artículo explicará cómo devolver el rango de valores desde [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

El siguiente código demuestra el uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) y devuelve el rango de valores a través de su método.

Crea una clase con una función *calculateCustomFunction*. Esta clase implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

Ahora usa la función anterior en tu programa

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
