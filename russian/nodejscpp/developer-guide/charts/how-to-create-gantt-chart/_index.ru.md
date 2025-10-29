---
title: Как создать диаграмму Ганта с помощью Node.js через C++
linktitle: Как создать диаграмму Ганта
type: docs
weight: 72
url: /ru/nodejs-cpp/how-to-create-gantt-chart/
description: Узнайте, как создать диаграмму Ганта с API Aspose.Cells for Node.js via C++.
keywords: Node.js создает диаграмму Ганта, добавляет диаграмму Ганта, вставляет диаграмму Ганта
---

## **Что такое диаграмма Ганта**

Диаграмма Ганта — это тип графика в виде столбцовой диаграммы, которая иллюстрирует график проекта. Она показывает даты начала и окончания различных элементов проекта. Каждый элемент или задача представлена столбцом, длина которого соответствует его продолжительности. Диаграммы Ганта также показывают зависимости между задачами, позволяя менеджерам видеть последовательность выполнения задач. Они широко используются в управлении проектами для планирования, расписания и отслеживания проектов.

## **Как создать диаграмму Ганта в Excel**

Вы можете создать диаграмму Ганта в Excel, следуя этим шагам:
1. Добавьте данные для диаграммы Ганта. 
<br>
<img src="00.png" width=50% />
1. Выберите данные и перейдите в Вставка -> Графики -> Вставить столбчатую или линейчатую диаграмму -> Сложенная гистограмма. В нашем примере это B1:B7, затем вставьте **Сложенную гистограмму**.
<br>
<img src="1.png" width=50% />

1. Выберите диаграмму, **Выберите данные** -> **Добавить**, установите **Название ряда** и **Значения ряда** согласно примеру.
<br>
<img src="2.png" width=50% />

1. Выберите диаграмму, отредактируйте **Метки горизонтальной (категорийной) оси**.
<br>
<img src="3.png" width=50% />

1. **Форматировать ось** по оси Y, выберите **Обратный порядок категорий**.
1. Выберите **синие серии** и установите **Заливка -> Нет заливки**.
1. **Форматировать ось** по оси X, установите **Минимум** и **Максимум** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Добавьте метки данных** для диаграммы, и вы получите диаграмму Ганта.
<br>
<img src="0.png" width=50% />


## **Как добавить диаграмму Ганта в Aspose.Cells**
Пожалуйста, посмотрите следующий пример кода. Он загружает [пробный Excel-файл](sample.xlsx), содержащий некоторые данные. Затем он создает сложенную столбчатую диаграмму на основе исходных данных и устанавливает соответствующие свойства. В конце он сохраняет рабочую книгу в [формате XLSX](result.xlsx). Следующий скриншот показывает созданную с помощью Aspose.Cells диаграмму Ганта в выходном Excel-файле.
<br>
<img src="5.png" width=60% />

### **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
