---
title: Вычисление формул с помощью Node.js через C++
linktitle: Расчет формул
description: В этой статье описывается, как использовать библиотеку Aspose.Cells для вычисления формул в Microsoft Excel через Node.js через C++. Загрузив существующий файл Excel или создав новый, мы можем использовать предоставленные Aspose.Cells методы для вычисления формулы и получения результата. В конце мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, формулы, вычисления, прямое вычисление формулы, повторное вычисление формул, добавление формул через Node.js через C++
type: docs
weight: 125
url: /ru/nodejs-cpp/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells встроен движок вычисления формул. Он может не только пересчитывать импортированные из шаблонов Excel формулы, но и поддерживает вычисление результатов добавленных формул в режиме выполнения.

Aspose.Cells поддерживает большинство формул или функций, характерных для Microsoft Excel (смотрите [список поддерживаемых функций движком вычислений](/cells/ru/nodejs-cpp/supported-formula-functions/)). Эти функции можно использовать через API или в дизайнерских таблицах. Aspose.Cells поддерживает большой набор математических, строковых, логических, дата/время, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) или методы [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Чтобы вычислить результаты формул, пользователь может вызвать метод [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который обрабатывает все встроенные формулы в файле Excel. Или пользователь может вызвать метод [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), который обрабатывает все формулы внутри листа. Или пользователь может также вызвать метод [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), который обрабатывает формулу одной ячейки:

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Важно знать о формулах**

{{% alert color="primary" %}}

Свойство **Formula** и методы **setFormula(...)** класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) работают иначе, чем методы **calculate** классов [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) и [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Свойство **Formula** и методы **setFormula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, вызовите методы **calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда нужно вычислить результаты формул напрямую, не добавляя их в лист. Значения ячеек, используемых в формуле, уже существуют в листе, и все, что нужно — это найти результат этих значений на основе формулы Microsoft Excel без добавления самой формулы в лист.

Можно использовать API движка вычислений формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) для получения результатов таких формул без добавления их в лист:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Приведенный выше код производит следующий вывод:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Как рассчитать формулы повторно**

Если в рабочей книге много формул и необходимо повторно вычислять их при изменении только части, может быть полезно включить цепочку вычислений формул: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Создание цепочки занимает дополнительное время, поэтому первый расчет формул ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) может потреблять больше ресурсов процессора и памяти по сравнению с вычислением без цепочки. Если повторный расчет формул не требуется, лучше оставить поведение по умолчанию (без цепочки).

{{% /alert %}}

## **Продвинутые темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени вычисления метода Cell.calculate](/cells/ru/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклических ссылок](/cells/ru/nodejs-cpp/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прерывание или отмена расчета формул книги](/cells/ru/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Установка режима расчета формул книги](/cells/ru/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
