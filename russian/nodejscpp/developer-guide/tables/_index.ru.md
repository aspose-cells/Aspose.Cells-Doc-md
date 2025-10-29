---
title: Создавайте и управляйте таблицами в файлах Microsoft Excel с помощью Node.js через C++
linktitle: Таблицы
type: docs
weight: 150
url: /ru/nodejs-cpp/create-and-format-table/
description: Вставляйте, изменяйте размер, редактируйте, удаляйте и форматируйте таблицы Excel с использованием Aspose.Cells for Node.js via C++.
---

## **Создать таблицу**

Одним из преимуществ электронных таблиц является возможность создания различных типов списков, например, списков телефонов, списков задач, списков транзакций, активов или обязательств. Несколько пользователей могут вместе работать с созданием и поддержкой различных списков.

Aspose.Cells поддерживает создание и управление списками.

### **Преимущества объекта списка**

Существует несколько преимуществ при преобразовании списка данных в фактический объект списка

- Новые строки и столбцы автоматически включаются.
- Итоговая строка внизу списка легко добавляется для отображения SUM, AVERAGE, COUNT и т. д.
- Добавленные столбцы справа автоматически включаются в объект списка.
- Графики, основанные на строках и столбцах, будут автоматически расширены.
- Именованные диапазоны, присвоенные строкам и столбцам, будут автоматически расширены.
- Список защищен от случайного удаления строк и столбцов.

### **Создание объекта списка с использованием Microsoft Excel**

- Выбор диапазона данных для создания объекта List
- Это отображает диалоговое окно Создания списка.
- Реализация объекта List для данных и указание итоговой строки (выберите **Данные**, затем **Список**, затем **Итоговая строка**).

### **Использование API Aspose.Cells**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий набор свойств и методов для управления рабочим листом. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) в рабочем листе, используйте коллекцию [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) — это, по существу, объект класса [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), который дополнительно предоставляет метод [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) для добавления объекта List и указания диапазона ячеек для этого списка.

В соответствии с указанным диапазоном ячеек объект List создается с помощью Aspose.Cells. Используйте атрибуты (например, [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--) и т.д.) класса [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) для управления списком.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/), используя API Aspose.Cells, как и в предыдущем разделе с Microsoft Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Форматирование таблицы**

Для управления и анализа группы связанных данных можно преобразить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию у каждого столбца в таблице включена фильтрация в строке заголовка, чтобы можно было быстро фильтровать или сортировать данные объекта списка. Можно добавить всю строку (специальная строка в списке, предоставляющая выбор агрегатных функций, полезных для работы с числовыми данными) к объекту списка, предоставляющую раскрывающийся список агрегатных функций для каждой ячейки всей строки. Aspose.Cells предоставляет возможности для создания и управления списками (или таблицами).

### **Форматирование объекта списка**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий набор свойств и методов для управления рабочими листами. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) в рабочем листе, используйте коллекцию [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) — это объект класса [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), который предоставляет метод [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) для добавления объекта List и указания диапазона ячеек. В соответствии с указанным диапазоном ячеек, в рабочем листе создается [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) с помощью Aspose.Cells. Используйте атрибуты (например, [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) класса [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) для форматирования таблицы по вашему требованию.

Пример ниже добавляет тестовые данные в рабочий лист, создает [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) и применяет к нему стандартные стили. Поддерживаются стили [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) от Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Продвинутые темы**
- [Преобразовать таблицу в ODS](/cells/ru/nodejs-cpp/convert-table-to-ods/)
- [Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным](/cells/ru/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Чтение и запись таблицы с источником данных из запроса к таблице](/cells/ru/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Установите комментарий таблицы или объекта списка внутри листа.](/cells/ru/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Таблицы и диапазоны](/cells/ru/nodejs-cpp/tables-and-ranges/)

{{< app/cells/assistant language="nodejs-cpp" >}}
