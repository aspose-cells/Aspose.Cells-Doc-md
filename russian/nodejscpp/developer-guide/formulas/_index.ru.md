---
title: Управление формулами Excel файлов с помощью Node.js через C++
linktitle: Формулы
type: docs
weight: 122
url: /ru/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Узнайте, как управлять формулами Excel с помощью Aspose.Cells for Node.js via C++. Aspose.Cells легко получает, устанавливает и вычисляет формулы Excel.
keywords: Как вычислять формулы в Node.js через C++, Формулы и функции с помощью Node.js через C++, Управление встроенными функциями Node.js через C++, Использование надстроечных функций с помощью Node.js через C++, Использование массивных формул через Node.js через C++, Использование формулы R1C1 в Node.js через C++.
---

## **Введение**

Одной из привлекательных особенностей Microsoft Excel является его способность обрабатывать данные с помощью формул и функций. В Excel встроен набор функций и формул, который помогает пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, облегчающих расчет значений для разработчиков. Aspose.Cells поддерживает дополнения функций, а также формулы массива и R1C1.

## **Как использовать формулы и функции**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент в коллекции Cells представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые классом [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), подробно обсуждаемым ниже.

- Использование встроенных функций.
- Использование функций дополнений.
- Работа с массивными формулами.
- Создание формулы R1C1.

## **Как использовать встроенные функции**

Встроенные функции и формулы предоставляются в виде готовых функций для ускорения работы разработчиков. Ознакомьтесь с [списком поддерживаемых встроенных функций](/cells/ru/nodejs-cpp/supported-formula-functions/). Функции перечислены в алфавитном порядке. В будущем будет поддерживаться больше функций.

Aspose.Cells поддерживает большинство формул и функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или [дизайнерский лист / шаблон таблицы](/cells/ru/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает большой набор математических, строковых, логических, дат/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) для добавления формулы в ячейку. **Сложные формулы**, например

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. Применяя формулу к ячейке, всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

В приведенном ниже примере к первой ячейке каталога [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) применяется сложная формула. Формула использует встроенную **Функцию IF**, предоставленную Aspose.Cells.

```javascript
const path = require("path");
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

## **Как использовать функции дополнений**

Может быть необходимо включить в excel пользовательские формулы, которые мы хотим включить в виде добавления. При установке функции cell.Formula встроенные функции работают хорошо, однако требуется установить пользовательские функции или формулы, используя функции дополнений.

Aspose.Cells предоставляет возможности для регистрации функций добавления с помощью [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). После этого, когда мы устанавливаем cell.Formula = anyFunctionFromAddIn, итоговый файл Excel содержит вычисленное значение из функции AddIn.

Для регистрации функции добавления в приведенном ниже образце кода следует загрузить файл XLAM. Аналогично, файл вывода "test_udf.xlsx" можно загрузить для проверки вывода.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Как использовать массивную формулу**

Массивные формулы – это формулы, которые принимают массивы в качестве аргументов для функций, составляющих формулу. Когда массивная формула отображается, она окружена фигурными скобками ({}).

Некоторые функции Microsoft Excel возвращают массивы значений. Для вычисления нескольких результатов с помощью массивной формулы введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

Возможно применить массивную формулу к ячейке, вызвав метод класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-). Метод [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) принимает следующие параметры:

- **Массивная Формула**, массивная формула.
- **Количество строк**, количество строк для заполнения результата массивной формулы.
- **Количество столбцов**, количество столбцов для заполнения результата массивной формулы.

```javascript
const path = require("path");
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

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Как использовать формулу R1C1**

Добавить формулу со ссылкой стиля **R1C1** в ячейку с помощью свойства [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Продвинутые темы**
- [Предшественники и зависимые](/cells/ru/nodejs-cpp/precedents-and-dependents/)
- [Установка внешних ссылок в формулах](/cells/ru/nodejs-cpp/set-external-links-in-formulas/)
- [Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки](/cells/ru/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Установка формулы для именованного диапазона](/cells/ru/nodejs-cpp/setting-formula-for-named-range/)
- [Установка формул - уведомление для пользователей не на английском языке](/cells/ru/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Установка общей формулы](/cells/ru/nodejs-cpp/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}
