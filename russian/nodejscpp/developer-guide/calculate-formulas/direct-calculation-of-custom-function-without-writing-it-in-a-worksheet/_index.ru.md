---
title: Прямой расчет пользовательской функции без записи ее в рабочий лист с помощью Node.js через C++
linktitle: Прямой расчет пользовательской функции без записи ее в рабочий лист
description: В этой статье описывается, как использовать библиотеку Aspose.Cells для прямого вычисления пользовательских функций в Microsoft Excel без записи функции в лист с помощью Node.js через C++. Загрузите существующий файл Excel или создайте новый, выполните вычисление пользовательской функции и сохраните измененный файл.
keywords: Aspose.Cells, Excel, пользовательские функции, прямые вычисления, Node.js через C++, без необходимости писать, рабочие листы
type: docs
weight: 90
url: /ru/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Прямой расчет пользовательской функции без записи ее на лист**

Эта тема объясняет, как напрямую вычислить ваши пользовательские функции, не записывая их предварительно в лист. Пожалуйста, используйте метод [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) для этой цели.

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, иллюстрирующим использование этого метода. Мы использовали пользовательскую функцию MyCompany.CustomFunction() и рассчитываем ее значение как "Aspose.Cells." сами, после чего это значение автоматически конкатенируется со значением ячейки A1, которая равна "Добро пожаловать в " движком расчета, и окончательное рассчитанное значение возвращается как "Добро пожаловать в Aspose.Cells.". Как видно из кода, мы не писали нашу пользовательскую функцию где-либо на рабочем листе, и она рассчитывается напрямую нашей собственной пользовательской логикой.

### **Пример программирования**

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

### **Вывод в консоль**

Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализация пользовательского движка вычислений для расширения стандартного движка Aspose.Cells](/cells/ru/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
