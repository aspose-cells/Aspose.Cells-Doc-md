---
title: Создавайте и управляйте диаграммами с помощью Node.js через C++
linktitle: Диаграммы
description: Узнайте, как использовать Aspose.Cells для Node.js для создания диаграмм в Microsoft Excel. Наше руководство покажет различные типы диаграмм и способы настройки их внешнего вида и форматирования.
keywords: Aspose.Cells для Node.js, Создание диаграмм, Microsoft Excel, Типы диаграмм, Настройка, Внешний вид, Форматирование.
type: docs
weight: 130
url: /ru/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

С помощью Aspose.Cells можно добавлять различные типы диаграмм в электронные таблицы. Aspose.Cells предоставляет множество гибких объектов диаграмм. В этой теме обсуждаются объекты диаграмм Aspose.Cells.

{{% /alert %}}

## **Создание диаграмм**

### **Простое создание диаграммы**
Создание диаграммы с Aspose.Cells с помощью следующих примеров кода:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Вещи, которые нужно знать для создания диаграммы**

Перед созданием диаграмм важно понять некоторые базовые концепции, которые помогают при создании диаграмм с помощью Aspose.Cells.

#### **Объекты диаграммирования**

Ниже перечислены объекты для построения диаграмм:

- Series, один набор данных в диаграмме.
- Axis, ось диаграммы.
- Chart, одна диаграмма Excel.
- ChartArea, область диаграммы на листе.
- ChartDataTable, таблица данных диаграммы.
- ChartFrame, объект рамки в диаграмме.
- ChartPoint, одна точка в наборе данных диаграммы.
- ChartPointCollection, коллекция, содержащая все точки в одном наборе данных.
- Charts, коллекция объектов Chart.
- DataLabels, коллекция всех объектов DataLabel для указанного набора данных.
- FillFormat, формат заливки для формы.
- Floor, основание 3D-диаграммы.
- Legend, легенда диаграммы.
- Line, линия диаграммы.
- SeriesCollection, коллекция объектов Series.
- TickLabels, метки делений, связанные с метками делений на оси диаграммы.
- Название, заголовок диаграммы или оси.
- Линия тренда, линия тренда на диаграмме.
- Коллекция линий тренда, коллекция всех объектов линии тренда для указанной серии данных.
- Стены, стены 3D-диаграммы.

#### **Использование объектов построения диаграмм**

Как уже упоминалось, все объекты построения диаграмм являются экземплярами соответствующих классов и обладают конкретными свойствами и методами для выполнения определенных задач. Используйте объекты построения диаграмм для создания диаграмм.

Добавьте любую диаграмму на лист с помощью коллекции [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--). Каждый элемент коллекции [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) представляет объект [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/). Объект [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) инкапсулирует все другие объекты для настройки внешнего вида диаграммы. Следующий раздел показывает, как использовать несколько базовых объектов диаграмм для создания простой диаграммы.

### **Создание диаграммы с использованием Aspose.Cells**

**Шаги:**

1. Добавьте данные в ячейки листа с помощью метода [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) объекта [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/).
   Это будет использоваться в качестве источника данных для диаграммы.
1. Добавьте диаграмму на лист, вызвав метод [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) коллекции [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection), инкапсулированный в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/).
1. Укажите тип диаграммы с помощью перечисления [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).
   Например, ниже используется значение [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) как тип диаграммы.
1. Получите новый объект [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) из коллекции [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection), передав его индекс.
1. Используйте любой из объектов диаграмм, инкапсулированных в объекте [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/), для управления диаграммой.
   Ниже используется объект [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) для указания источника данных диаграммы.

При добавлении исходных данных в диаграмму источник данных может быть диапазоном ячеек (например, "A1:C3"), последовательностью несмежных ячеек (например, "A1, A3, A5") или последовательностью значений (например, "1,2,3").

Эти общие шаги позволяют создать любой тип диаграммы. Используйте различные объекты построения диаграмм для создания различных диаграмм.

С помощью Aspose.Cells можно создать множество различных типов диаграмм. Все стандартные диаграммы, поддерживаемые Aspose.Cells, предварительно определены в перечислении с именем [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

Предопределенные типы графиков:

|**Типы графиков**|**Описание**|
| :- | :- |
|Column|Представляет гистограмму с кластеризацией
|ColumnStacked|Представляет стопку гистограмму
|Column100PercentStacked|Представляет 100% стопку гистограмму
|Column3DClustered|Представляет 3D гистограмму с кластеризацией
|Column3DStacked|Представляет 3D стопку гистограмму
|Column3D100PercentStacked|Представляет 3D 100% стопку гистограмму
|Column3D|Представляет 3D гистограмму
|Bar|Представляет гистограмму с кластеризацией по горизонтали
|BarStacked|Представляет стопку гистограмму по горизонтали
|Bar100PercentStacked|Представляет 100% стопку гистограмму по горизонтали
|Bar3DClustered|Представляет 3D гистограмму с кластеризацией по горизонтали
|Bar3DStacked|Представляет 3D стопку гистограмму по горизонтали
|Bar3D100PercentStacked|Представляет 3D 100% стопку гистограмму по горизонтали
|Line|Представляет линейный график
|LineStacked|Представляет стопку линейный график
|Line100PercentStacked|Представляет 100% стопку линейный график
|LineWithDataMarkers|Представляет линейный график с маркерами данных
|LineStackedWithDataMarkers|Представляет стопку линейный график с маркерами данных
|Line100PercentStackedWithDataMarkers|Представляет собой 100% столбчатую диаграмму с маркерами данных|
|Line3D|Представляет собой 3D линейную диаграмму|
|Pie|Представляет собой круговую диаграмму|
|Pie3D|Представляет собой 3D круговую диаграмму|
|PiePie|Представляет собой круговую диаграмму с вложенной круговой диаграммой|
|PieExploded|Представляет собой взорванную круговую диаграмму|
|Pie3DExploded|Представляет собой 3D взорванную круговую диаграмму|
|PieBar|Представляет собой столбчатую диаграмму с вложенной круговой диаграммой|
|Scatter|Представляет собой точечную диаграмму|
|ScatterConnectedByCurvesWithDataMarker|Представляет собой точечную диаграмму, соединенную кривыми, с маркерами данных|
|ScatterConnectedByCurvesWithoutDataMarker|Представляет собой точечную диаграмму, соединенную кривыми, без маркеров данных|
|ScatterConnectedByLinesWithDataMarker|Представляет собой точечную диаграмму, соединенную линиями, с маркерами данных|
|ScatterConnectedByLinesWithoutDataMarker|Представляет собой точечную диаграмму, соединенную линиями, без маркеров данных|
|Area|Представляет собой зонную диаграмму|
|AreaStacked|Представляет собой стопку зонную диаграмму|
|Area100PercentStacked|Представляет собой 100% стопку зонную диаграмму|
|Area3D|Представляет собой 3D зонную диаграмму|
|Area3DStacked|Представляет собой 3D стопку зонную диаграмму|
|Area3D100PercentStacked|Представляет собой 3D 100% стопку зонную диаграмму|
|Doughnut|Представляет собой донат-диаграмму|
|DoughnutExploded|Представляет круговую диаграмму со сдвоенной дугой|
|Radar|Представляет радарную диаграмму|
|RadarWithDataMarkers|Представляет радарную диаграмму с маркерами данных|
|RadarFilled|Представляет заполненную радарную диаграмму|
|Surface3D|Представляет трехмерную поверхностную диаграмму|
|SurfaceWireframe3D|Представляет проволочную трехмерную поверхностную диаграмму|
|SurfaceContour|Представляет контурную диаграмму|
|SurfaceContourWireframe|Представляет проволочную контурную диаграмму|
|Bubble|Представляет диаграмму пузырьков|
|Bubble3D|Представляет трехмерную диаграмму пузырьков|
|Cylinder|Представляет цилиндрическую диаграмму|
|CylinderStacked|Представляет стопку цилиндрических диаграмм|
|Cylinder100PercentStacked|Представляет 100% стопку цилиндрических диаграмм|
|CylindericalBar|Представляет цилиндрическую столбчатую диаграмму|
|CylindericalBarStacked|Представляет стопку цилиндрических столбчатых диаграмм|
|CylindericalBar100PercentStacked|Представляет 100% стопку цилиндрических столбчатых диаграмм|
|CylindericalColumn3D|Представляет трехмерную цилиндрическую колоночную диаграмму|
|Cone|Представляет конусную диаграмму|
|ConeStacked|Представляет стопку конусных диаграмм|
|Cone100PercentStacked|Представляет 100% стопку конусных диаграмм|
|ConicalBar|Представляет коническую столбчатую диаграмму|
|ConicalBarStacked|Представляет стопку конических столбчатых диаграмм|
|ConicalBar100PercentStacked|Представляет 100% стопку конических столбчатых диаграмм|
|ConicalColumn3D|Представляет 3D коническую колонную диаграмму|
|Pyramid|Представляет пирамидальную диаграмму|
|PyramidStacked|Представляет стопку пирамидальных диаграмм|
|Pyramid100PercentStacked|Представляет 100% стопку пирамидальных диаграмм|
|PyramidBar|Представляет стопку пирамидальных столбчатых диаграмм|
|PyramidBarStacked|Представляет стопку пирамидальных столбчатых диаграмм|
|PyramidBar100PercentStacked|Представляет 100% стопку пирамидальных столбчатых диаграмм|
|PyramidColumn3D|Представляет 3D пирамидальную колонную диаграмму|
{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных можно установить только диапазон сверху влево до нижнего правого. Например, "A1:C3" - допустимо, а "C3:A1" - недопустимо.

{{% /alert %}}

#### **Пирамидальная диаграмма**

При выполнении примерного кода на листе добавляется пирамидальная диаграмма.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Линейная диаграмма**

В приведенном выше примере, просто изменив [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) на *Line*, создается линейная диаграмма. Полный источник приведен ниже. После выполнения кода, на лист добавится линейная диаграмма.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

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
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Пузырьковая диаграмма**

Чтобы создать пузырьковую диаграмму, необходимо установить [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) в [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype), а также задать несколько дополнительных свойств, таких как BubbleSizes, Values и XValues. После выполнения следующего кода, на лист добавится пузырьковая диаграмма.

#### **Диаграмма линии с маркерами данных**

Чтобы создать линию с маркером данных, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) должен быть установлен в *ChartType.LineWithDataMarkers*, а также задать дополнительные свойства, такие как фон, маркеры серии, Values и XValues. После выполнения следующего кода, на лист добавится диаграмма с линией и маркером данных.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Продвинутые темы**
- [Чтение и манипулирование диаграммами Excel 2016](/cells/ru/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Управление осями диаграмм Excel](/cells/ru/nodejs-cpp/chart-axes/)
- [Настройка внешнего вида диаграммы](/cells/ru/nodejs-cpp/setting-chart-appearance/)
- [Типы диаграмм](/cells/ru/nodejs-cpp/chart-types/)
- [Настройка диаграмм](/cells/ru/nodejs-cpp/customizing-charts/)
- [Установить источник данных для диаграммы](/cells/ru/nodejs-cpp/data-formatting-in-charts/)
- [Управление подписями данных диаграмм Excel](/cells/ru/nodejs-cpp/insert-datalabels-to-chart/)
- [Получить лист диаграммы](/cells/ru/nodejs-cpp/get-worksheet-of-the-chart/)
- [Управление легендой диаграмм Excel](/cells/ru/nodejs-cpp/chart-legend/)
- [Управление позицией, размером и дизайном диаграммы](/cells/ru/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Создание круговой диаграммы с линиями](/cells/ru/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Фигуры в диаграммах](/cells/ru/nodejs-cpp/controls-in-charts/)
- [Управление заголовками диаграмм Excel](/cells/ru/nodejs-cpp/chart-and-axis-titles/)
- [Отображение диаграммы](/cells/ru/nodejs-cpp/chart-rendering/)
- [Получить текст уравнения линии тренда диаграммы](/cells/ru/nodejs-cpp/get-equation-text-of-chart-trendline/)
