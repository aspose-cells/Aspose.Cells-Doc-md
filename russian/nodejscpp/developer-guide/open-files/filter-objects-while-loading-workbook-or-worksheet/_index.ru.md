---
title: Фильтрация объектов при загрузке Рабочей книги или Листья с помощью Node.js через C++
linktitle: Фильтрование объектов при загрузке книги Excel или листа
type: docs
weight: 330
url: /ru/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Узнайте, как фильтровать данные при загрузке рабочих книг или листьев, используя Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) при фильтрации данных из книги. Но если вы хотите фильтровать данные из отдельных листов, вам придется переопределить метод [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-). Укажите подходящее значение из перечисления [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) при создании или работе с [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter).

Перечисление [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) имеет следующие возможные значения.

- Все
- Настройки книги
- Пустая ячейка
- Булева ячейка
- Данные ячейки
- Ошибка ячейки
- Числовая ячейка
- Строковая ячейка
- Значение ячейки
- Chart
- Условное форматирование
- Проверка данных
- Определенные имена
- Свойства документа
- Формула
- Гиперссылки
- ОбъединеннаяОбласть
- СводнаяТаблица
- Настройки
- Фигура
- ДанныеЛиста
- НастройкиЛиста
- Структура
- Стиль
- Таблица
- VBA
- XmlMap

## **Фильтрование объектов при загрузке книги Excel**
Приведенный ниже образец кода демонстрирует, как фильтровать диаграммы из книги Excel. Пожалуйста, проверьте [образец excel файла](5115258.xlsx), использованный в этом коде, и [выходной PDF](5115257.pdf), сгенерированный им. Как видно из выходного PDF, все диаграммы были отфильтрованы из книги Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **Фильтрование объектов при загрузке Листа**
Приведенный ниже образец кода загружает [исходный файл Excel](5115255.xlsx) и фильтрует следующие данные из его листов, используя пользовательский фильтр.

- Он фильтрует Диаграммы из листа с именем NoCharts.
- Он фильтрует формы из листа с именем NoShapes.
- Он фильтрует Условное форматирование из листа с именем NoConditionalFormatting.

После загрузки [исходного файла Excel](5115255.xlsx) с пользовательским фильтром он берет изображения со всех листов один за другим. Здесь представлены изображения для вашего ознакомления. Как видно, на первом изображении нет диаграмм, на втором - нет фигур, на третьем - нет условного форматирования.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

Вот как использовать класс CustomLoadFilter согласно именам листов.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
