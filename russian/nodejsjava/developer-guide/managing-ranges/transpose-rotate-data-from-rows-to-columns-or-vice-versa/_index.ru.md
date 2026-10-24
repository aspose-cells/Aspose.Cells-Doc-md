---
title: Транспонирование диапазона
linktitle: Транспонирование диапазона
description: Эта статья объясняет, как транспонировать или поворачивать данные из строк в столбцы или наоборот в файлах Excel с помощью Aspose.Cells for Node.js via Java, используя три разных подхода.
keywords: Aspose.Cells, библиотека Node.js via Java, электронная таблица, транспонирование диапазона, поворот данных, функция TRANSPOSE, формула динамического массива, формула массива, Excel TRANSPOSE, строки в столбцы
type: docs
weight: 80
url: /ru/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java поддерживает транспонирование (поворот) данных, при котором строки становятся столбцами, а столбцы — строками, тремя разными способами. Первый подход использует метод `Range.transpose()` для изменения данных на месте и работает во всех версиях Excel. Второй подход применяет `Cell.setDynamicArrayFormula()` для записи современной формулы динамического массива `=TRANSPOSE(...)`, которая автоматически заполняет соседние ячейки в Excel 365 или Excel 2021. Третий подход использует `Cell.setArrayFormula()` для записи классической формулы массива CSE (Ctrl+Shift+Enter), совместимой с предыдущими версиями Excel. В этой статье каждый подход рассматривается пошагово и сопровождается полными примерами кода.
{{% /alert %}}

## **Introduction**
Транспонирование диапазона означает его поворот таким образом, чтобы строки становились столбцами, а столбцы — строками, то есть данные отражались относительно главной диагонали. В Microsoft Excel эту операцию выполняет функция рабочего листа `TRANSPOSE`, концептуальное описание которой приведено в [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Этот подход можно программно применить к диапазону ячеек, что полезно во многих сценариях бизнес-аналитики и отчетности.
- Изменение ориентации квартальных или годовых отчетов, в которых кварталы обычно располагаются по горизонтали, а регионы — по вертикали, или наоборот.
- Изменение ориентации осей на панелях мониторинга или диаграммах, чтобы временной ряд располагался по вертикали, а не по горизонтали.
- Изменение структуры данных, импортированных из внешних систем, чтобы они соответствовали макету, ожидаемому последующей аналитикой или шаблонами отчетов.
Чтобы сделать последующие примеры наглядными, в каждом из них используется небольшая таблица продаж по регионам и кварталам. В демонстрационной рабочей книге эта таблица занимает диапазон **A1:D5**, при этом **A1** оставлена пустой как левый верхний элемент, **B1:D1** содержит заголовки регионов, а **A2:A5** — заголовки кварталов.
| Регион           | Европа      | Азия       | Северная Америка |
|------------------|-------------|------------|-------------------|
| Кв. 1            | 21704714    | 8774099    | 12094215          |
| Кв. 2            | 17987034    | 12214447   | 10873099          |
| Кв. 3            | 19485029    | 14356879   | 15689543          |
| Кв. 4            | 22567894    | 15763492   | 17456723          |
Затем в статье представлены три разных способа транспонирования этих данных с помощью Aspose.Cells for Node.js via Java. Каждый способ подходит для определенной версии Excel и сценария использования.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
Используйте этот подход, если требуется транспонировать данные без применения функции рабочего листа `TRANSPOSE`. Он работает во **всех версиях Excel** и не зависит от динамических массивов, поэтому является наиболее совместимым вариантом. Этот подход идеален, когда нужны только итоговые транспонированные значения и исходную формулу `TRANSPOSE` не требуется сохранять в рабочей книге.

### **API used**
`Range.transpose()` — экземплярный метод класса `com.aspose.cells.Range`. При его вызове диапазон изменяется на месте путем перестановки строк и столбцов, поэтому строки становятся столбцами, а столбцы — строками. Метод непосредственно изменяет исходные ячейки, не записывая формулу.

### **Steps**
1. Откройте исходную рабочую книгу в формате `.xlsx`, задав `LoadOptions` с помощью вызова `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Получите первый рабочий лист из рабочей книги с помощью `workbook.getWorksheets().get(0)`.
3. Получите доступ к коллекции ячеек рабочего листа через `worksheet.getCells()`.
4. Создайте исходный диапазон **A1:D5** с помощью вызова `cells.createRange("A1:D5")`.
5. Вызовите `source.transpose()`, чтобы повернуть диапазон на месте, переставив строки и столбцы.
6. Сохраните рабочую книгу с помощью `workbook.save(outputFile)`.
После транспонирования исходный диапазон начальной ячейки содержит повернутые данные. Первая строка содержит значения (пусто, **Европа**, **Азия**, **Северная Америка**), а первый столбец — (пусто, **Кв. 1**, **Кв. 2**, **Кв. 3**, **Кв. 4**). Каждый исходный столбец с данными о продажах становится строкой транспонированного диапазона.

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.XLSX);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Используйте этот подход, если требуется сохранить формулу `=TRANSPOSE(A1:D5)` как активную формулу в итоговой рабочей книге, чтобы результат автоматически обновлялся при изменении исходных данных, а итоговый файл Excel открывался в **Excel 365 / Excel 2021 или более поздней версии**, где поддерживаются динамические массивы и автоматическое заполнение области результата.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` — метод класса `com.aspose.cells.Cell`, который задает формулу ячейки как **формулу динамического массива**. Excel вычисляет формулу один раз и автоматически заполняет ею окружающие ячейки. Если третий параметр установлен в `true`, Aspose.Cells также вычисляет полученные значения при записи файла.

### **Steps**
1. Загрузите исходную рабочую книгу с помощью `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Получите первый рабочий лист и доступ к его коллекции `Cells`.
3. Поместите формулу динамического массива в ячейку **A6**, непосредственно под исходным диапазоном, с помощью вызова `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Аргумент `null` передает параметры `FormulaParseOptions` по умолчанию, а третий аргумент `true` указывает Aspose.Cells обработать формулу как динамический массив и вычислить ее, чтобы автоматически заполненные значения были записаны в рабочую книгу.
5. Сохраните рабочую книгу с помощью `workbook.save(outputFile)`.
Ячейка **A6** содержит формулу `=TRANSPOSE(A1:D5)`, а Excel автоматически заполняет ею область **A6:D10** — блок из 5 строк и 4 столбцов, соответствующий транспонированным данным.

{{% alert color="primary" %}}
Этот подход работает **только в Excel 365 / 2021 или более поздней версии**. Более старые версии Excel неправильно заполняют области формул динамических массивов.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.XLSX));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.XLSX);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Используйте этот подход, если требуется сохранить формулу `TRANSPOSE` в рабочей книге, но итоговый файл Excel может открываться в **более старых версиях (до 2021 года, включая 2019, 2016, 2013 и т. д.)**, где автоматическое заполнение динамических массивов не поддерживается. Классическая формула массива CSE (Ctrl+Shift+Enter) является совместимой с предыдущими версиями альтернативой, которую могут вычислять все версии Excel.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` — метод класса `com.aspose.cells.Cell`, который назначает **классическую формулу массива (CSE)** ячейке начальной области и задает размеры результирующего массива. Aspose.Cells записывает маркер формулы массива для нескольких ячеек, чтобы Excel вычислял формулу как единое выражение массива, заполняющее указанный диапазон.

### **Steps**
1. Загрузите исходную рабочую книгу, как описано в предыдущих подходах.
2. Получите первый рабочий лист и доступ к его коллекции `Cells`.
3. Вызовите `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Второй аргумент `4` задает количество строк целевого массива, а третий аргумент `5` — количество столбцов.
4. Сохраните рабочую книгу с помощью `workbook.save(outputFile)`.
Ячейка **A6** является начальной ячейкой формулы массива, а вычисленный массив занимает 4 строки и 5 столбцов, начиная с A6, что соответствует транспонированным размерам исходного диапазона A1:D5. Excel записывает единый маркер формулы массива по всему результирующему диапазону, чтобы более старые версии Excel правильно вычисляли формулу.

{{% alert color="primary" %}}
Формулы массива CSE — классический способ вычисления выражения `TRANSPOSE` в Excel, и этот подход совместим со всеми версиями Excel.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.XLSX));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| Подход | API / метод | Версия Excel | Формула сохранена? | Выходной диапазон |
|--------|-------------|--------------|---------------------|------------------|
| Подход 1 — транспонирование на месте | `Range.transpose()` | Все версии Excel | Нет (только значения) | Начальный диапазон, 5×4 |
| Подход 2 — формула динамического массива | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Да (динамическое заполнение) | Автоматически заполняется от начальной ячейки |
| Подход 3 — классическая формула массива (CSE) | `Cell.setArrayFormula` | Все версии Excel | Да (формула массива для нескольких ячеек) | Явный размер, 4×5 |
Используйте **Подход 1**, если необходимо быстро выполнить преобразование, совместимое со всеми версиями, и требуется записать в файл только транспонированные значения. Используйте **Подход 2**, если гарантированно используется современная версия Excel и формула должна оставаться активной и обновляться при изменении источника. Используйте **Подход 3**, если необходима максимальная совместимость с сохранением формулы во всех версиях Excel, включая старые выпуски, не поддерживающие динамические массивы.

## **Related Articles**
- [Рендеринг одноклеточного массива SmartMarker | Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Вставка изображения в ячейку](/cells/ru/nodejs-java/inserting-an-image-into-a-cell/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}