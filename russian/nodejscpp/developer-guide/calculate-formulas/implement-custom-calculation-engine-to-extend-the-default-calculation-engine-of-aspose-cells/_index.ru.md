---
title: Реализуйте пользовательский движок вычислений для расширения стандартного Aspose.Cells с помощью Node.js через C++
linktitle: Реализация собственного расчетного механизма для расширения стандартного расчетного механизма Aspose.Cells
description: В этой статье описывается, как расширить стандартный движок расчетов в Node.js, реализовав пользовательский движок с использованием библиотеки Aspose.Cells для Node.js через C++. Загрузите существующий файл Excel или создайте новый, воспользуйтесь предоставляемыми методами и сохраните измененный файл.
keywords: Aspose.Cells, Excel, пользовательский движок расчетов, Node.js через C++
type: docs
weight: 80
url: /ru/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Следующий код реализует пользовательский движок расчетов. Он реализует интерфейс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine), который содержит метод [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата 27/07/2023, то пользовательский движок будет вычислять TODAY() как 28/07/2023.

### **Пример программирования**

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

### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше примера кода; значение (дата и время) A1 с пользовательским движком должно быть на один день позже результата без него.

### **Связанная статья**

{{% alert color="primary" %}}

[Прямой расчет пользовательской функции без записи ее в рабочий лист](/cells/ru/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
