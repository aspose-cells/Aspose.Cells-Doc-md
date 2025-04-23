---
title: Настройка диаграмм
type: docs
weight: 15
url: /ru/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Создание диаграмм**

С помощью Aspose.Cells можно добавлять различные типы диаграмм в электронные таблицы. Aspose.Cells предоставляет множество гибких объектов диаграмм. В этой теме обсуждаются объекты диаграмм Aspose.Cells.

### **Простое создание диаграммы**

Просто создать диаграмму с Aspose.Cells с помощью следующих примеров кода:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Важные моменты для создания диаграммы**

Прежде чем создавать диаграммы, важно понимать некоторые основные концепции, которые полезны при создании диаграмм с использованием Aspose.Cells.

#### **Объекты диаграммирования**

Aspose.Cells предоставляет специальный набор классов, используемых для создания всех видов диаграмм. Эти классы используются для создания **объектов диаграммирования**, которые выступают в качестве строительных блоков диаграммы. Объекты диаграммирования перечислены ниже:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), ось диаграммы.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), одна диаграмма Excel.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), область диаграммы на листе.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), таблица данных диаграммы.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), объект рамки на диаграмме.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), одна точка в серии на диаграмме.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), коллекция, содержащая все точки одной серии.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), коллекция объектов [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart).
- DataLabels, подписи данных для указанного [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline) и т. д.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), формат заливки для формы.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), основание 3D-диаграммы.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), легенда диаграммы.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), линия диаграммы.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), коллекция объектов [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series).
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), представляет одну серию данных на диаграмме.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), метки делений, связанные с делениями оси диаграммы.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), заголовок диаграммы или оси.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), линия тренда на диаграмме.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), набор всех объектов Trendline для указанной серии данных.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), стены 3D-графика.

#### **Использование объектов построения диаграмм**

Как уже упоминалось, все объекты построения диаграмм являются экземплярами соответствующих классов и обладают конкретными свойствами и методами для выполнения определенных задач. Используйте объекты построения диаграмм для создания диаграмм.

Добавьте любой тип диаграммы на лист с использованием коллекции [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection). Каждый элемент в коллекции [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) представляет объект [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart). Объект [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) инкапсулирует все объекты диаграммирования, необходимые для настройки внешнего вида диаграммы. В следующем разделе показано, как использовать несколько основных объектов диаграммирования для создания простой диаграммы.

### **Создание простой диаграммы**

С помощью Aspose.Cells можно создавать множество различных типов диаграмм. Все стандартные диаграммы, поддерживаемые Aspose.Cells, предопределены в перечислении с именем [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Предопределенные типы диаграмм:

|**Типы графиков**|**Описание**|
| :- | :- |
|Column|Представляет диаграмму столбцов в кластере|
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
|Scatter|Представляет диаграмму рассеяния|
|ScatterConnectedByCurvesWithDataMarker|Представляет диаграмму рассеяния, соединенную кривыми, с маркерами данных|
|ScatterConnectedByCurvesWithoutDataMarker|Представляет диаграмму рассеяния, соединенную кривыми, без маркеров данных|
|ScatterConnectedByLinesWithDataMarker|Представляет диаграмму рассеяния, соединенную линиями, с маркерами данных|
|ScatterConnectedByLinesWithoutDataMarker|Представляет диаграмму рассеяния, соединенную линиями, без маркеров данных|
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
|SurfaceWireframe3D|Представляет жесткую 3D поверхностную диаграмму|
|SurfaceContour|Представляет контурную диаграмму|
|SurfaceContourWireframe|Представляет проволочную контурную диаграмму|
|Bubble|Представляет диаграмму пузырьков|
|Bubble3D|Представляет трехмерную диаграмму пузырьков|
|Cylinder|Представляет цилиндрическую диаграмму|
|CylinderStacked|Представляет стопку цилиндрических диаграмм|
|Cylinder100PercentStacked|Представляет 100% стопку цилиндрических диаграмм|
|CylindricalBar|Представляет цилиндрическую столбчатую диаграмму.|
|CylindricalBarStacked|Представляет стопку цилиндрических столбчатых диаграмм|
|CylindricalBar100PercentStacked|Представляет 100% стопку цилиндрических столбчатых диаграмм|
|CylindricalColumn3D|Представляет трехмерную цилиндрическую диаграмму|
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
|PyramidBar|Представляет пирамидальную столбчатую диаграмму|
|PyramidBarStacked|Представляет стопку пирамидальных столбчатых диаграмм|
|PyramidBar100PercentStacked|Представляет 100% стопку пирамидальных столбчатых диаграмм|
|PyramidColumn3D|Представляет 3D пирамидальную колонную диаграмму|
Для создания диаграммы с помощью Aspose.Cells:

1. Добавьте некоторые данные в ячейки листа с помощью метода [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) объекта [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).
   Это будет использоваться в качестве источника данных для диаграммы.
1. Добавьте график на лист, вызвав метод [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-) коллекции [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Укажите тип диаграммы с помощью перечисления [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).
   Например, в примере используется значение [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) в качестве типа графика.
1. Получите доступ к новому объекту [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) из коллекции [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), передав его индекс.
1. Используйте любой объект построения диаграмм, инкапсулированный в объекте [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), для управления диаграммой.
   В приведенном ниже примере используется объект построения диаграммы [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) для указания источника данных диаграммы.

При добавлении исходных данных на диаграмму источник данных может быть диапазоном ячеек (например, "A1:C3"), или последовательностью непрерывных ячеек (например, "A1, A3, A5"), или последовательностью значений (например, "1,2,3").

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных можно установить только диапазон сверху вниз. Например, "A1:C3" допустим, в то время как "C3:A1" недопустим.

{{% /alert %}}

Эти общие шаги позволяют создать любой тип диаграммы. Используйте различные объекты построения диаграмм для создания различных диаграмм.

При выполнении примерного кода на лист добавляется пирамидальный график, как показано на рисунке ниже.

**Пирамидальный график с его источником данных**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Чтобы создать график пузырьков, [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) должен быть установлен на [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE), и несколько дополнительных свойств, таких как BubbleSizes, Values и XValues, должны быть установлены соответственно. После выполнения следующего кода на лист добавляется график пузырьков, как показано на рисунке ниже.

**График пузырьков с его источником данных**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Диаграмма линии с маркерами данных**

Для создания линейного графика с маркерами данных [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) должен быть установлен на [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS), и несколько дополнительных свойств, таких как область фона, маркеры ряда, значения и XValues должны быть установлены соответственно. После выполнения следующего кода на лист добавляется линейный график с маркерами данных, как показано на рисунке ниже.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Создание настраиваемых диаграмм**

До сих пор, когда мы говорили о графиках, мы рассматривали стандартные графики, которые имеют свои стандартные настройки форматирования. Мы только определяем источник данных, устанавливаем несколько свойств, и график создается с его форматными настройками по умолчанию. Но Aspose.Cells также поддерживает создание пользовательских графиков, что позволяет разработчикам создавать графики с их собственными настройками форматирования.

### **Создание настраиваемых диаграмм**

Разработчики могут создавать пользовательские графики во время выполнения с помощью простого API Aspose.Cells.

График состоит из серии данных. Каждая серия данных в Aspose.Cells представлена объектом [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), в то время как объект [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) служит коллекцией объектов [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series). При создании пользовательского графика разработчики могут использовать различные типы графиков для различных серий данных (собранных в объекте [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)).

{{% alert color="primary" %}}

В настоящее время Aspose.Cells поддерживает только пользовательские графики, объединяющие круговые, линейные, столбчатые и столбчатые групповые графики, но в будущих версиях будет поддерживаться больше графиков. Для полного списка стандартных графиков, которые поддерживает Aspose.Cells, см. статью [Типы графиков](/cells/ru/java/chart-types/).

{{% /alert %}}

Приведенный ниже пример кода демонстрирует, как создать пользовательские графики. В этом примере мы собираемся использовать столбчатую диаграмму для первой серии данных и линейную диаграмму для второй серии. Результатом будет добавление столбчатой диаграммы, объединенной с линейной диаграммой, на лист.

**Пользовательская диаграмма, объединяющая столбцовую и линейную диаграммы**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Пример программирования**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Чтобы увидеть список поддерживаемых типов диаграмм, прочитайте статью [Типы диаграмм](/cells/ru/java/chart-types/).

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
