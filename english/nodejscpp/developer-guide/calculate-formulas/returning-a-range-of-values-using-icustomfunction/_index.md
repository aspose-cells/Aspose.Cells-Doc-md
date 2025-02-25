---
title: Returning a Range of Values using ICustomFunction with Node.js via C++
linktitle: Returning a Range of Values using ICustomFunction
description: This article describes how to use the Aspose.Cells library to return a range of values with ICustomFunction in Node.js via C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to get a range of values and return the result.
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values Node.js via C++
type: docs
weight: 50
url: /nodejs-cpp/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}
The [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction) is deprecated since the release of Aspose.Cells for Java 20.8. Please use the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) class. The use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) class is described in the following article.
[Returning a Range of Values using AbstractCalculationEngine](/cells/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/).
{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Cells provides [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction) interface which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement the [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction) interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return the range of values from [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction).
{{% /alert %}}

The following code implements [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction) and returns the range of values via its method.

Create a class with a function *CalculateCustomFunction*. This class implements [**ICustomFunction**](https://reference.aspose.com/cells/nodejs-cpp/icustomfunction).

```javascript
class CustomFunctionStaticValue {
    calculateCustomFunction(functionName, paramsList, contextObjects) {
        return [
            [new Date(2015, 5, 12, 10, 6, 30), 2],
            [3.0, "Test"]
        ];
    }
}
```

Now use the above function in your program

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();
const cells = wb.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.checkCell(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const copt = new AsposeCells.CalculationOptions();
copt.setCustomEngine(new CustomFunctionStaticValue());
wb.calculateFormula(copt);

// Save to xlsx by setting the calc mode to manual
wb.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
wb.save(path.join(dataDir, "output_out.xlsx"));

// Save to pdf
wb.save(path.join(dataDir, "output_out.pdf"));
```
