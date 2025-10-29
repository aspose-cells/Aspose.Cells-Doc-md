---  
title: 通过Node.js使用C++降低Cell.Calculate方法的计算时间  
linktitle: 减少Cell.Calculate方法的计算时间  
description: 本文介绍如何使用Aspose.Cells库，通过Node.js的C++，减少Excel中单元格计算方法的计算时间。  
keywords: Aspose.Cells，Excel，单元格计算方法，优化，性能，减少计算时间，Node.js通过C++  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **可能的使用场景**

通常，我们建议用户调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)方法一次，然后获取每个单元格的计算值。但有时，用户不想计算整个工作簿。他们只想计算单个单元格。Aspose.Cells提供了[**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)属性，你可以将其设置为**false**，以显著减少单个单元格的计算时间。当递归属性设置为**true**时，所有依赖单元格每次调用时都会重新计算；当递归属性为**false**时，依赖的单元格只计算一次，后续调用不再重新计算。

## **减少Cell.calculate()方法的计算时间**

以下示例代码演示了[**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)属性的用法。请使用给定的[示例Excel文件](5113710.xlsx)执行此代码，并查看控制台输出。你会发现，将递归属性设置为**false**显著减少了计算时间。也请阅读注释以更好理解此属性。

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

## **控制台输出**

这是上述示例代码使用给定的[示例Excel文件](5113710.xlsx)在我们的机器上执行时的控制台输出。请注意，你的输出可能不同，但将递归属性设置为**false**后的耗时始终会少于设置为**true**。

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
