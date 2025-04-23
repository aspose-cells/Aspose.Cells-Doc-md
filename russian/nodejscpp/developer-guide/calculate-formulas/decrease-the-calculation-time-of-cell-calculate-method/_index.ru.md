---  
title: Снизить время вычислений метода Cell.Calculate с помощью Node.js через C++  
linktitle: Уменьшить время вычисления метода Cell.Calculate  
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для уменьшения времени вычислений методов расчёта в Excel через Node.js через C++.  
keywords: Aspose.Cells, Excel, методы расчёта ячеек, оптимизация, производительность, сокращение времени вычислений, Node.js через C++  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Возможные сценарии использования**

Обычно мы рекомендуем пользователям вызывать метод [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) один раз, а затем получать рассчитанные значения для отдельных ячеек. Но иногда пользователи не хотят вычислять всю рабочую книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells предоставляет свойство [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), которое можно установить в **false** для значительного сокращения времени вычисления отдельных ячеек. Когда рекурсивное свойство установлено в **true**, все зависимые ячейки пересчитываются при каждом вызове. Однако, если свойство рекурсии установлено в **false**, зависимые ячейки вычисляются один раз и не пересчитываются при последующих вызовах.

## **Снизить время вычисления метода Cell.calculate()**

 Следующий пример кода показывает использование свойства [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). Пожалуйста, выполните этот код с использованием данного [примера файла excel](5113710.xlsx) и проверьте его вывод в консоль. Вы увидите, что установка рекурсивного свойства в **false** значительно снизила время вычислений. Также прочтите комментарии для лучшего понимания этого свойства.

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

## **Вывод в консоль**

Это вывод консоли приведенного выше примера кода при выполнении с использованием данного [образца excel файла](5113710.xlsx) на нашей машине. Обратите внимание, ваш вывод может отличаться, но затраченное время после установки свойства рекурсии в **false** всегда будет меньше, чем при установке его в **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

