---
title: Как добавить сводную диаграмму (PivotChart) с помощью Aspose.Cells for Node.js via C++
linktitle: Сводная диаграмма
type: docs
weight: 100
url: /ru/nodejs-cpp/how-to-add-pivot-chart/
description: Как добавить сводную диаграмму с помощью Aspose.Cells for Node.js via C++.
keywords: Сводная диаграмма Node.js через C++
---
## Что такое сводная диаграмма

Сводная диаграмма — это визуальное представление данных в сводной таблице. Сводные диаграммы предоставляют способ суммировать, анализировать, исследовать и показывать сводные данные. Вот некоторые ключевые особенности и аспекты сводных диаграмм:

1. Динамическое представление данных: сводные диаграммы автоматически обновляются при изменениях в сводной таблице. Если добавить или удалить поля, диаграмма обновится соответственно.

1. Интерактивность: сводные диаграммы интерактивны, позволяют пользователю фильтровать, сортировать и углубляться в данные. Это облегчает исследование различных аспектов набора данных.

1. Гибкая разметка: пользователи могут изменять раскладку сводного графика, перетаскивая поля, что обеспечивает гибкость в визуализации данных.

1. Различные типы графиков: сводные диаграммы можно создавать с помощью различных типов графиков, таких как гистограммы, линейные графики, круговые диаграммы и другие, в зависимости от характера данных и нужных инсайтов.

1. Суммирование: сводные диаграммы суммируют большие объемы данных и могут отображать итоги, средние значения, подсчеты или другие сводные статистики.

1. Фильтрация: они предоставляют функции фильтрации, позволяющие отображать только данные, соответствующие определенным критериям.

<br>
Сводные диаграммы широко используются в бизнес-аналитике и анализе данных для предоставления ясного и краткого визуального обзора сложных наборов данных. Это мощный инструмент для принятия решений, основанных на данных.

## Как добавить сводную диаграмму с помощью Aspose.Cells for Node.js via C++

### **Добавление сводной таблицы**

Для создания сводной таблицы с помощью Aspose.Cells for Node.js via C++:

1. Добавьте данные в лист с помощью метода `putValue` объекта Cell. Также можно использовать файл шаблона, предварительно заполненный данными. Эти данные будут использованы как источник данных для сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод `add` коллекции `PivotTables`.
1. Получите новый объект PivotTable из коллекции `PivotTables`, передав его индекс. Используйте любой из объектов сводной таблицы, инкапсулированных в объекте PivotTable, для управления таблицей.

Приведены примеры кода ниже.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Добавление сводной диаграммы**

Для создания сводной диаграммы с помощью Aspose.Cells for Node.js via C++:

1. Добавьте диаграмму.
1. Установите свойство `PivotSource` диаграммы, чтобы оно ссылалось на существующую сводную таблицу в таблице.
1. Задайте другие атрибуты.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
