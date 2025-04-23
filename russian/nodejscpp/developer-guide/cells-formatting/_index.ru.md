---
title: Форматировать ячейки с помощью Node.js через C++
description: Узнайте, как форматировать и стилизовать ячейки в Aspose.Cells for Node.js via C++, включая форматирование чисел, даты, стиль шрифта и другие параметры стиля ячейки. Наш гид поможет вам создавать привлекательные и профессиональные таблицы.
keywords: Aspose.Cells for Node.js via C++, форматирование ячеек, стилизация, формат чисел, формат дат, стиль шрифта, опции стиля ячейки, электронная таблица, создание, профессиональный вид, форматировать строки и столбцы.
linktitle: Форматировать ячейки
type: docs
weight: 120
url: /ru/nodejs-cpp/cells-formatting/
---

## **Введение**

{{% alert color="primary" %}}

Aspose.Cells предоставляет методы [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) и [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) класса [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), используемые для получения/установки стилей форматирования ячейки. Также Aspose.Cells предоставляет класс [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{% /alert %}}

## **Как форматировать ячейки с помощью методов GetStyle и SetStyle**

Применить различные виды стилей форматирования на ячейки для установки цветов фона или переднего плана, границ, шрифтов, горизонтальных и вертикальных выравниваний, уровня отступа, направления текста, угла поворота и многое другое.

### **Как использовать методы GetStyle и SetStyle**

Если разработчикам нужно применять разные стили форматирования к разным ячейкам, то лучше получить [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) ячейки с помощью метода [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--), указать атрибуты стиля и затем применить форматирование с помощью метода [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-). Ниже приведён пример, демонстрирующий этот подход для различных форматов ячейки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Как использовать объект стиля для форматирования различных ячеек**

Если разработчикам нужно применять одинаковый стиль оформления к разным ячейкам, они могут использовать объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Следуйте приведённым ниже шагам для использования объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style):

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), вызвав его метод [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)
2. Получите доступ к новосозданному объекту [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)
3. Установите желаемые свойства/атрибуты объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) для применения нужных настроек форматирования
4. Назначьте сконфигурированный объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) нужным ячейкам

Этот подход может значительно повысить эффективность ваших приложений и сэкономить память.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Как использовать предопределенные стили Microsoft Excel 2007**

Если вам необходимо применить различные стили форматирования для Microsoft Excel 2007, примените стили с использованием API Aspose.Cells. Приведен пример, демонстрирующий этот подход к применению предопределенного стиля к ячейке.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Как форматировать выбранные символы в ячейке**

Работа со настройками шрифта объясняет, как форматировать текст в ячейках, но это объясняет только, как форматировать весь содержимое ячейки. Что, если вы хотите отформатировать только выбранные символы?

Это также поддерживается в Aspose.Cells. В этой теме объясняется, как эффективно использовать эту функцию.

### **Как форматировать выбранные символы**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получать доступ к каждому листу Excel. Лист Excel представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Класс [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) предоставляет метод [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-), который имеет следующие параметры для выбора диапазона символов внутри ячейки:

- **Индекс начала**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество выбираемых символов.

Метод [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) возвращает экземпляр класса [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting), что позволяет разработчикам форматировать символы аналогично ячейке, как показано в примере кода ниже. В выходном файле, в ячейке A1, слово 'Visit' будет отформатировано шрифтом по умолчанию, а 'Aspose!' — жирным и синим цветом.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Если вы заинтересованы в форматировании части богатого текста в ячейке, используйте методы [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) и [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Метод [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) предназначен для доступа к частям текста, а затем исправления могут выполняться с помощью метода [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-), в то время как метод **Get** возвращает массив объектов [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting), которые можно редактировать для задания различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., а **Set** можно использовать для применения изменений.

{{% /alert %}}

## **Как форматировать строки и столбцы**

Иногда разработчику требуется применить одно и то же форматирование на строки или столбцы. Применение форматирования к ячейкам одну за другой часто занимает больше времени и не является хорошим решением.
Для решения этой проблемы Aspose.Cells предоставляет простой и быстрый способ, который подробно рассматривается в данной статье.

### **Форматирование строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получать доступ к каждому листу Excel. Лист Excel представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Коллекция [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) содержит коллекцию [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--).

### **Как форматировать строку**

Каждый элемент коллекции [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) представляет объект [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row). Объект [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) предлагает метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-), используемый для установки форматирования строки. Для применения одинакового форматирования к строке используйте объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Ниже показаны шаги, как это сделать.

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) в класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), вызвав его метод [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--).
2. Установите свойства объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) для применения настроек форматирования.
3. Включите соответствующие атрибуты для объекта [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).
4. Назначьте сконфигурированный объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) объекту [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Как форматировать столбец**

Коллекция [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) также предоставляет коллекцию [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--). Каждый элемент в коллекции [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) представляет объект [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column). Аналогично объекту [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), объект [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) также предлагает метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) для форматирования столбца.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Продвинутые темы**
- [Настройки выравнивания](/cells/ru/nodejs-cpp/cells-alignment-settings/)
- [Настройки границ](/cells/ru/nodejs-cpp/cells-border-settings/)
- [Установить условные форматы для файлов Excel и ODS.](/cells/ru/nodejs-cpp/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/nodejs-cpp/excel-themes-and-colors/)
- [Настройки заливки](/cells/ru/nodejs-cpp/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/nodejs-cpp/cells-font-settings/)
- [Форматирование ячеек листа в книге Excel](/cells/ru/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Реализация системы дат 1904 года](/cells/ru/nodejs-cpp/implement-1904-date-system/)
- [Объединение и разъединение ячеек](/cells/ru/nodejs-cpp/merging-and-unmerging-cells/)
- [Настройки чисел](/cells/ru/nodejs-cpp/cells-number-settings/)
- [Получение и установка стиля ячеек](/cells/ru/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

