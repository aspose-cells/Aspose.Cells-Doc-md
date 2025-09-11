---
title: Returning a Range of Values using AbstractCalculationEngine with Node.js via C++
linktitle: Returning a Range of Values using AbstractCalculationEngine
description: This article introduces an abstract calculation engine that returns a range of values in Excel using the Aspose.Cells library for Node.js via C++. Learn to load or create an Excel file and save the modified file to disk.
keywords: Aspose.Cells, Excel, abstract calculation engine returning values Node.js via C++, custom functions
type: docs
weight: 55
url: /nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) class which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

This article will explain how to return the range of values from [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

The following code demonstrates the use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) class and returns the range of values via its method.

Create a class with a function *calculateCustomFunction*. This class implements [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

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

Now use the above function in your program

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
{{< app/cells/assistant language="nodejs-cpp" >}}