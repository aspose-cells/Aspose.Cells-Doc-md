---
title: 无需在工作表中编写函数即可用Node.js通过C++直接计算自定义函数
linktitle: 直接计算自定义函数，无需先将其编写在工作表中
description: 本文介绍如何通过Node.js的C++使用Aspose.Cells库，直接在Microsoft Excel中计算自定义函数，无需在工作表中编写函数。加载现有Excel文件或创建新文件，计算自定义函数，然后保存修改后的文件。
keywords: Aspose.Cells，Excel，自定义函数，直接计算，Node.js通过C++，无需写入工作表
type: docs
weight: 90
url: /zh/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **在不将其写入工作表的情况下直接计算自定义函数**

本主题介绍如何在不先写入工作表的情况下直接计算自定义函数。请使用[**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-)方法实现此目的。

请参阅以下示例代码，演示了如何使用此方法。我们使用了一个名为 MyCompany.CustomFunction() 的自定义函数，并且通过自己的自定义逻辑计算其值为 "Aspose.Cells."，然后该值由计算引擎自动地与单元格 A1 的值 "Welcome to " 进行连接，最终计算的值返回为 "Welcome to Aspose.Cells."。从代码中可以看到，我们并未在工作表中编写自定义函数，而是直接通过我们自己的自定义逻辑进行计算。

### **编程示例**

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

### **控制台输出**

以下是上面示例代码的控制台输出。

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎，扩展Aspose.Cells的默认计算引擎](/cells/zh/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
