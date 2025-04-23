---
title: Как создать динамическую прокручиваемую диаграмму с помощью Node.js через C++
linktitle: Как создать динамическую прокручивающуюся диаграмму
description: Узнайте, как создать динамическую прокручиваемую диаграмму с использованием Aspose.Cells for Node.js via C++. Наш пошаговый гид покажет, как реализовать плавные переходы данных и автоматическую прокрутку для непрерывного и актуального отображения.
keywords: Aspose.Cells для Node.js, динамическая прокручиваемая диаграмма, переходы данных, плавная прокрутка, непрерывное отображение, обновление визуализации.
type: docs
weight: 75
url: /ru/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Возможные сценарии использования**
Динамическая прокручивающаяся диаграмма - это тип графического представления, используемого для отображения данных, меняющихся со временем. Она предназначена для предоставления видео в реальном времени данных, позволяя пользователям отслеживать непрерывные обновления и тренды. Диаграмма непрерывно обновляется при добавлении новых данных, автоматически прокручиваясь, чтобы показывать самую последнюю информацию.

Динамические прокручивающиеся диаграммы широко используются в различных отраслях, таких как финансы, анализ фондового рынка, отслеживание погоды и аналитика социальных медиа. Они позволяют пользователям визуализировать и анализировать паттерны данных и принимать обоснованные решения на основе информации в реальном времени.

Эти диаграммы обычно интерактивны, позволяя пользователю увеличивать или уменьшать масштаб, прокручивать исторические данные и регулировать временные интервалы. Они часто поддерживают несколько серий данных, обеспечивая комплексный обзор различных метрик и их взаимосвязей.

В целом, динамические прокручивающиеся диаграммы - это ценные инструменты для мониторинга и анализа временных рядов данных, способствуя принятию решений в реальном времени и улучшая возможности визуализации данных.

## **Используйте Aspose.Cells для создания динамической прокручиваемой диаграммы**
В следующих параграфах мы покажем, как создать динамическую прокручиваемую диаграмму с использованием Aspose.Cells for Node.js via C++. Мы представим пример кода, а также созданный на основании этого файла Excel.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Прокручивающейся Диаграммы](DynamicScrollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Примечания**
В сгенерированном файле вы можете работать со строкой прокрутки, в то время как диаграмма динамически подсчитывает последние 10 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Вы можете попробовать изменить число "10" на "15" в ячейке "Sheet1!$H$20", и динамическая диаграмма подсчитает последние 15 наборов данных. Теперь мы успешно создали динамическую прокручиваемую диаграмму с помощью Aspose.Cells for Node.js via C++.
