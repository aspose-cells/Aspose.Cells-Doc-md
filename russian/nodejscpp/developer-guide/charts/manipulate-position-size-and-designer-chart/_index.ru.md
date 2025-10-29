---
title: Манипуляции с позиционированием, размером и проектированием графика с помощью Node.js через C++
linktitle: Управление позицией, размером и оформлением диаграммы
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для эффективного управления положением, размером и разработкой графика в Microsoft Excel. Наш гид покажет, как настроить эти свойства для улучшения расположения и визуализации.
keywords: Aspose.Cells for Node.js via C++, Положение, Размер, График дизайнера, Microsoft Excel, Макет, Визуализация.
type: docs
weight: 45
url: /ru/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **Позиция и размер диаграммы**
Иногда вам нужно изменить положение или размер нового или существующего графика внутри листа. Aspose.Cells предоставляет свойство [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) для этого. Вы можете использовать его под-свойства для изменения размера графика с новым **высотой** и **шириной** или его позиционирования с помощью новых координат **X** и **Y**.

### **Управление позицией и размером диаграммы**
Чтобы изменить позицию диаграммы (координаты X, Y) или размер (высота, ширина), используйте эти свойства:

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

Следующий пример демонстрирует использование вышеуказанных API: он загружает существующую рабочую книгу с графиком на первом листе, затем изменяет размер и позицию графика с помощью Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Манипулирование дизайнерскими диаграммами**
Иногда необходимо манипулировать или изменять графики в шаблонных файлах. Aspose.Cells полностью поддерживает работу с содержимым и элементами дизайнерских графиков. Данные, содержимое графика, фоновое изображение и форматирование можно сохранять с точностью.

### **Манипулирование дизайнерскими диаграммами в файле-шаблоне**
Для управления дизайнерскими графиками в шаблонных файлах используйте API, связанные с графиками. Например, можно использовать свойство Worksheet.charts для получения существующей коллекции графиков в шаблоне.

#### **Создание диаграммы**
В следующем примере показано, как создать пирамидальную диаграмму. Позже мы будем изменять эту диаграмму.

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

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Изменение диаграммы**
В следующем примере показано, как изменить существующую диаграмму. В этом примере мы модифицируем созданную выше диаграмму. В полученном выводе обратите внимание, что метка даты одной точки данных установлена на 'Великобритания, 30K'.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Изменение линейной диаграммы в шаблоне конструктора**
В этом примере мы будем изменять линейную диаграмму. Мы добавим несколько рядов данных к существующей диаграмме и изменим цвета их линий.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
