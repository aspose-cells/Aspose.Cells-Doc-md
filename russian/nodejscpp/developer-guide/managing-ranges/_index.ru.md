---
title: Управление диапазонами с помощью Node.js через C++
linktitle: Диапазоны
type: docs
weight: 105
url: /ru/nodejs-cpp/managing-ranges/
description: Узнайте, как управлять диапазонами в Excel с помощью Aspose.Cells for Node.js via C++. Создавайте диапазоны, задавайте значения, стили и выполняйте различные операции.
---

## **Введение**

В Excel можно выделять несколько ячеек с помощью рамки мыши; выбранный набор ячеек называется "Диапазон".

Например, вы можете кликнуть левой кнопкой мыши по ячейке "A1" в Excel, а затем протащить до ячейки "C4". Этот прямоугольный участок также можно легко создать как объект с помощью Aspose.Cells for Node.js via C++.

Вот как создать диапазон, вставить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## **Управление диапазонами с помощью Aspose.Cells for Node.js via C++**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

### **Создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Поместить значение в ячейки диапазона**

Предположим, что у вас есть диапазон ячеек, который расширяется от A1 до C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Установить стиль ячеек диапазона**

Следующий пример показывает, как установить стиль ячеек диапазона.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Получить текущий регион диапазона**

CurrentRegion - это свойство, которое возвращает объект Range, представляющий текущий регион. 

Текущий регион - это диапазон, ограниченный любой комбинацией пустых строк и столбцов. Только для чтения.

В Excel текущий регион можно получить следующим образом:
1. Выберите область (диапазон1) с помощью мыши.
2. Нажмите "Главная - Редактирование - Поиск и выделение - Перейти специальное - Текущий регион", или используйте "Ctrl+Shift+*", вы увидите, как Excel автоматически поможет вам выбрать область (диапазон2). Теперь вы это сделали, диапазон2 является Текущим регионом диапазона1.

Пожалуйста, скачайте следующий тестовый файл, откройте его в Excel, с помощью мыши выделите область "A1:D7", затем нажмите "Ctrl+Shift+*", вы увидите выделенной область "A1:C3".

[current_region.xlsx](current_region.xlsx)

Теперь запустите следующий пример, чтобы увидеть, как он работает в Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/nodejs-cpp/autofill-ranges/)
- [Копирование диапазонов в Excel](/cells/ru/nodejs-cpp/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/nodejs-cpp/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/nodejs-cpp/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/nodejs-cpp/copy-range-style-only/)
- [Создать объединенный диапазон](/cells/ru/nodejs-cpp/create-union-range/)
- [Вырезать и вставить диапазон](/cells/ru/nodejs-cpp/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/nodejs-cpp/delete-ranges-from-Excel/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Вставить диапазоны](/cells/ru/nodejs-cpp/insert-ranges-to-Excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Создать именованные диапазоны с учетом книги и листа](/cells/ru/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/nodejs-cpp/search-and-replace-data-in-a-range/)
