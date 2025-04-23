---
title: Как создать динамическую диаграмму с выпадающим списком с помощью Node.js через C++
linktitle: Как создать динамическую диаграмму с выпадающим списком
description: Узнайте, как создать динамическую диаграмму, которая обновляется в зависимости от выбора в выпадающем списке, используя Aspose.Cells for Node.js via C++. Наш пошаговый гид покажет, как интегрировать выпадающий список в вашу диаграмму для гибкой визуализации данных.
keywords: Aspose.Cells for Node.js via C++, динамическая диаграмма, выпадающий список, визуализация данных, интеграция, гибкая визуализация.
type: docs
weight: 76
url: /ru/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Возможные сценарии использования**
Динамическая диаграмма с выпадающим списком в Excel - мощный инструмент, позволяющий пользователям создавать интерактивные диаграммы, которые могут динамически обновляться на основе выбранных данных. Эта функция особенно полезна в ситуациях, где необходимо проанализировать несколько наборов данных или сравнить различные сценарии.

Одно из распространенных применений динамической диаграммы с выпадающим списком - в финансовом анализе. Например, компания может иметь несколько наборов финансовых данных для разных лет или отделов. Используя выпадающий список, пользователи могут выбрать конкретный набор данных, который они хотят проанализировать, и диаграмма автоматически обновится, чтобы отобразить соответствующую информацию. Это позволяет легко сравнивать и идентифицировать тенденции или закономерности.

Еще одно применение - в продажах и маркетинге. У компании может быть данные о продажах различных товаров или регионов. С помощью динамической диаграммы с выпадающим списком пользователи могут выбрать конкретный товар или регион из выпадающего списка, и диаграмма будет динамически обновляться, чтобы показать результаты продаж для выбранной опции. Это помогает определить лучшие области или продукты и принимать решения на основе данных.

В заключение, динамическая диаграмма с выпадающим списком в Excel обеспечивает гибкий и интерактивный способ визуализации и анализа данных. Он ценен в ситуациях, где необходимо сравнивать несколько наборов данных или изучать различные сценарии, что делает его универсальным инструментом для финансового анализа, продаж и маркетинга, а также многих других приложений.

## **Используйте Aspose Cells для создания динамической диаграммы с выпадающим списком**
В следующих параграфах мы покажем, как создать динамическую диаграмму с выпадающим списком с использованием Aspose.Cells for Node.js via C++. Мы представим пример кода, а также созданный на основании этого кода файл Excel.

## **Образец кода**
Следующий образец кода сгенерирует файл [Динамическая диаграмма с выпадающим списком](DynamicChartWithDropdownlist.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Примечания**
В сгенерированном файле диаграмма динамически будет подсчитывать данные для выбранного месяца. Это делается с помощью формулы "OFFSET" в образцовом коде:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Вы можете попробовать изменить значение выпадающего списка в ячейке "Лист1!$A$10", и вы увидите динамическое изменение диаграммы. Теперь мы успешно создали динамическую диаграмму с выпадающим списком с использованием Aspose.Cells.
