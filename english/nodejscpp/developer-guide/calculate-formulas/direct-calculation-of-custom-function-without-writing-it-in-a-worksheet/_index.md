---
title: Direct calculation of custom function without writing it in a worksheet with Node.js via C++
linktitle: Direct calculation of custom function without writing it in a worksheet
description: This article introduces how to use Aspose.Cells library to directly calculate custom functions in Microsoft Excel without writing the function in a worksheet using Node.js via C++. Load an existing Excel file or create a new one, calculate the custom function, and save the modified file.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, Node.js via C++, no need to write, worksheets
type: docs
weight: 90
url: /nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Direct calculation of custom function without writing it in a worksheet**

This topic explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) method for this purpose.

Please see the following sample code that illustrates the usage of this method. We have used a custom function named `MyCompany.CustomFunction()` and we calculate its value as `"Aspose.Cells."` ourselves; then this value is automatically concatenated with the value of cell A1, which is `"Welcome to "`, by the calculation engine, and the final calculated value returns as `"Welcome to Aspose.Cells."`. As you can see, we have not written our custom function anywhere in a worksheet, and it is calculated directly by our own custom logic.

### **Programming Sample**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **Console Output**

Below is the console output of the above sample code.

{{< highlight javascript >}}
Calculated Value: Welcome to Aspose.Cells.
{{< /highlight >}}

### **Related Article**

{{% alert color="primary" %}}
[Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
