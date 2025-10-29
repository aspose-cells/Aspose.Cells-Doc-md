---  
title: Создавайте динамические диаграммы с помощью Node.js через C++  
linktitle: Создание динамических графиков  
description: Узнайте, как создавать динамические диаграммы в Aspose.Cells for Node.js via C++. Это руководство покажет, как динамически обновлять данные диаграммы, серии и форматирование в соответствии с вашими требованиями, позволяя визуально отображать изменяющиеся данные в ваших листах.  
keywords: Aspose.Cells для Node.js, построение графиков, динамические диаграммы, данные, серии, форматирование, листы, обновление.  
type: docs  
weight: 240  
url: /ru/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
Динамические (или интерактивные) диаграммы обладают способностью изменяться при изменении объема данных. Другими словами, динамические диаграммы могут автоматически отражать изменения, когда меняется источник данных. Для вызова изменения источника данных можно использовать опцию фильтрации таблиц Excel или использовать элемент управления, такой как комбо-бокс или раскрывающийся список.

В этой статье показано использование API Aspose.Cells for Node.js via C++ для создания динамических диаграмм с помощью обоих вышеупомянутых подходов.  
{{% /alert %}}  

## **Использование таблиц Excel**  

{{% alert color="primary" %}}  
Таблицы Excel называются ListObjects в контексте Aspose.Cells, поэтому мы будем использовать термин "ListObject" вместо "Таблица" для ясности. Подробнее о создании [ListObjects](/cells/ru/nodejs-cpp/create-and-format-table/) с помощью Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

ListObjects предоставляет встроенную функцию сортировки и фильтрации данных при взаимодействии с пользователем. Обе опции сортировки и фильтрации реализованы через выпадающие списки, автоматически добавляемые в строку заголовка [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). Благодаря этим функциям (сортировка и фильтрация), [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) кажется отличным вариантом для источника данных динамической диаграммы, потому что при изменении сортировки или фильтрации отображение данных в диаграмме будет обновляться в соответствии с текущим состоянием [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

Чтобы сделать демонстрацию более понятной, мы создадим [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) с нуля и будем идти по шагам, как описано ниже.

1. Создать пустой [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Получите [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) первого [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) в [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Вставить некоторые данные в ячейки.
1. Создайте [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) на основе вставленных данных.
1. Создайте [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) на основе диапазона данных [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Сохраните результат на диск.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Использование динамических формул**  

Если вы не хотите использовать [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) в качестве источника данных для динамической диаграммы, другой вариант — использовать функции Excel (или формулы) для создания динамического диапазона данных и контрол (например, ComboBox) для запуска изменения данных. В этом сценарии мы будем использовать функцию VLOOKUP для получения соответствующих значений на основе выбранного элемента ComboBox. При изменении выбора функция VLOOKUP обновит значение ячейки. Если диапазон ячеек использует функцию VLOOKUP, весь диапазон можно обновить при взаимодействии пользователя, поэтому его можно использовать как источник для динамической диаграммы.

Чтобы сделать демонстрацию понятной, мы создадим рабочую книгу с нуля и будем двигаться шаг за шагом, как описано ниже.

1. Создать пустой [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Получите [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) первого [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) в [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Вставьте данные в ячейки, создав именованный диапазон. Эти данные будут служить серией для динамической диаграммы.
1. Создайте [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) на основе ранее созданного именованного диапазона.
1. Вставьте еще данные в ячейки, которые будут служить источником для функции VLOOKUP.
1. Вставить функцию VLOOKUP (с соответствующими параметрами) в диапазон ячеек. Этот диапазон будет служить источником для динамической диаграммы.
1. Создайте [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) на основе диапазона, созданного на предыдущем шаге.
1. Сохраните результат на диск.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
