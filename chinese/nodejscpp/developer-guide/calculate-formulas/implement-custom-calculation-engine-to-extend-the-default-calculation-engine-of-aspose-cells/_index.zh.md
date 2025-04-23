---
title: 使用Node.js的C++实现自定义计算引擎，以扩展Aspose.Cells的默认计算引擎
linktitle: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
description: 本文介绍如何通过使用 C++ 版 Aspose.Cells 库在 Node.js 中实现自定义计算引擎，从而扩展默认的计算引擎。加载现有的 Excel 文件或创建新文件，使用提供的方法并保存修改后的 Excel 文件。
keywords: Aspose.Cells，Excel，自定义计算引擎，Node.js via C++
type: docs
weight: 80
url: /zh/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **实现自定义计算引擎**

Aspose.Cells具有强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认的计算引擎，从而为您提供更大的动力和灵活性。

在实现此功能中使用了以下属性和类。

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

以下代码实现了自定义计算引擎。它实现了接口 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)，其中包含一个 [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-) 方法。该方法会对所有公式调用。在此方法中，我们捕获 **TODAY** 函数并在系统日期基础上加一天。因此，如果当前日期是 2023/07/27，则自定义引擎会将 TODAY() 计算为 2023/07/28。

### **编程示例**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **结果**

请检查上述示例代码的控制台输出；使用自定义引擎后，单元格 A1 的日期时间值应比未使用该引擎时的结果晚一天。

### **相关文章**

{{% alert color="primary" %}}

[无需在工作表中编写即自定义函数的直接计算](/cells/zh/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
