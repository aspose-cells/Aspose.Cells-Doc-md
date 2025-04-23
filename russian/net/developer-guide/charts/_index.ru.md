---
title: Создание и управление диаграммой
description: Узнайте, как использовать Aspose.Cells for .NET для создания диаграмм в Microsoft Excel. Наш руководство продемонстрирует различные типы диаграмм, которые можно создать, а также как настроить их внешний вид и форматирование.
keywords: Aspose.Cells for .NET, создание диаграммы, Microsoft Excel, типы диаграмм, настройка, внешний вид, форматирование.
linktitle: Диаграммы
type: docs
weight: 130
url: /ru/net/creating-charts/
description: Создать диаграмму в CSharp для файлов Excel и ODS.
keywords: создать диаграмму, составить график 
---

{{% alert color="primary" %}}

С помощью Aspose.Cells можно добавлять различные типы диаграмм в электронные таблицы. Aspose.Cells предоставляет множество гибких объектов диаграмм. В этой теме обсуждаются объекты диаграмм Aspose.Cells.

{{% /alert %}}

## **Создание диаграмм**

### **Простое создание диаграммы**
Создание диаграммы с Aspose.Cells с помощью следующих примеров кода:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Вещи, которые нужно знать для создания диаграммы**

Прежде чем создавать диаграммы, важно понимать некоторые основные концепции, которые полезны при создании диаграмм с использованием Aspose.Cells.

#### **Объекты диаграммирования**

Aspose.Cells предоставляет специальный набор классов в пространстве имен [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts), используемых для создания диаграмм, поддерживаемых Aspose.Cells. Эти классы используются для создания **объектов диаграммирования**, которые выступают в качестве строительных блоков диаграммы. Объекты диаграммирования перечислены ниже:

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

Добавьте любой тип диаграммы на лист, используя коллекцию [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts). Каждый элемент в коллекции [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) представляет объект [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart). Объект [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) инкапсулирует все остальные объекты построения диаграмм, необходимые для настройки внешнего вида диаграммы. В следующем разделе показано, как использовать несколько базовых объектов построения диаграмм для создания простой диаграммы.

### **Создание диаграммы с использованием Aspose.Cells**

**Шаги:**

1. Добавьте некоторые данные в ячейки листа с помощью метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) объекта [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Это будет использоваться в качестве источника данных для диаграммы.
1. Добавьте диаграмму на лист, вызвав метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) коллекции [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection), инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
1. Укажите тип диаграммы с помощью перечисления [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).
   Например, приведенный ниже пример использует значение [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) в качестве типа диаграммы.
1. Получите доступ к новому объекту [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) из коллекции [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection), передав его индекс.
1. Используйте любой объект построения диаграмм, инкапсулированный в объекте [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart), для управления диаграммой.
   В приведенном ниже примере используется объект построения диаграммы [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) для указания источника данных диаграммы.

При добавлении исходных данных на диаграмму источник данных может быть диапазоном ячеек (например, "A1:C3"), или последовательностью непрерывных ячеек (например, "A1, A3, A5"), или последовательностью значений (например, "1,2,3").

Эти общие шаги позволяют создать любой тип диаграммы. Используйте различные объекты построения диаграмм для создания различных диаграмм.

С помощью Aspose.Cells можно создать множество различных типов диаграмм. Все стандартные диаграммы, поддерживаемые Aspose.Cells, предварительно определены в перечислении с именем [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Линейная диаграмма**

В предыдущем примере, просто изменение [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) на *Line* создает линейную диаграмму. Полный исходный код предоставлен ниже. При выполнении кода на лист добавляется линейная диаграмма.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Пузырьковая диаграмма**

Для создания диаграммы пузырьков нужно установить [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) на [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) и задать несколько дополнительных свойств, таких как BubbleSizes, Values и XValues. При выполнении следующего кода на лист добавляется диаграмма пузырьков.

#### **Диаграмма линии с маркерами данных**

Для создания диаграммы линии с маркерами данных [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) должно быть установлено на *ChartType.LineWithDataMarkers*, и необходимо задать несколько дополнительных свойств, таких как область заднего плана, маркеры серии, значения и XValues. При выполнении следующего кода на лист добавляется диаграмма линии с маркерами данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Продвинутые темы**
- [Чтение и манипулирование диаграммами Excel 2016](/cells/ru/net/read-and-manipulate-excel-2016-charts/)
- [Управление осями диаграмм Excel](/cells/ru/net/chart-axes/)
- [Настройка внешнего вида диаграммы](/cells/ru/net/setting-chart-appearance/)
- [Типы диаграмм](/cells/ru/net/chart-types/)
- [Настройка диаграмм](/cells/ru/net/customizing-charts/)
- [Установить источник данных для диаграммы](/cells/ru/net/data-formatting-in-charts/)
- [Управление подписями данных диаграмм Excel](/cells/ru/net/insert-datalabels-to-chart/)
- [Генерировать диаграмму с помощью обработки умных маркеров](/cells/ru/net/generate-chart-by-processing-smart-markers/)
- [Получить лист диаграммы](/cells/ru/net/get-worksheet-of-the-chart/)
- [Управление легендой диаграмм Excel](/cells/ru/net/chart-legend/)
- [Управление позицией, размером и дизайном диаграммы](/cells/ru/net/manipulate-position-size-and-designer-chart/)
- [Создание круговой диаграммы с линиями](/cells/ru/net/creating-pie-chart-with-leader-lines/)
- [Фигуры в диаграммах](/cells/ru/net/controls-in-charts/)
- [Управление заголовками диаграмм Excel](/cells/ru/net/chart-and-axis-titles/)
- [Отображение диаграммы](/cells/ru/net/chart-rendering/)
- [Получить текст уравнения линии тренда диаграммы](/cells/ru/net/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="csharp" >}}
