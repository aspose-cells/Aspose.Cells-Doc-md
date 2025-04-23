---
title: Возвращение диапазона значений с помощью AbstractCalculationEngine с Node.js через C++
linktitle: Возвращение Диапазона Значений с Использованием AbstractCalculationEngine
description: В этой статье представлена абстрактная система расчетов, которая возвращает диапазон значений в Excel с помощью библиотеки Aspose.Cells для Node.js через C++. Узнайте, как загрузить или создать файл Excel и сохранить измененный файл на диск.
keywords: Aspose.Cells, Excel, абстрактный движок расчетов, возвращающий значения, Node.js через C++, пользовательские функции
type: docs
weight: 55
url: /ru/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine), который используется для реализации определяемых пользователем или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В данной статье будет объяснено, как вернуть диапазон значений из [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

Следующий код демонстрирует использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) и возвращает диапазон значений через его метод.

Создайте класс с функцией *calculateCustomFunction*. Этот класс реализует [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

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

Теперь используйте вышеуказанную функцию в своей программе

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
