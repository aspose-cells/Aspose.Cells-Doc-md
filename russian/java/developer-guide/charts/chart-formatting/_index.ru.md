---
title: Форматирование диаграммы
type: docs
weight: 20
url: /ru/java/chart-formatting/
---

## **Настройка внешнего вида диаграммы**

В разделе [Типы диаграмм](/cells/ru/java/chart-types/) мы дали краткое введение в типы диаграмм и объекты диаграмм, предлагаемые Aspose.Cells.

В этой статье мы обсудим, как настроить внешний вид диаграмм, устанавливая ряд различных свойств:

- [Установка области диаграммы](/cells/ru/java/chart-formatting/#setting-chart-area).
- [Установка линий диаграммы](/cells/ru/java/chart-formatting/#setting-chart-lines).
- [Применение тем](/cells/ru/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Установка заголовков для диаграмм и осей](/cells/ru/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Работа с линиями сетки](/cells/ru/java/chart-formatting/#setting-major-gridlines).
- [Установка границ для задней и боковых стенок](/cells/ru/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Установка области диаграммы**

В диаграмме существуют различные типы областей, и Aspose.Cells предоставляет гибкость изменения внешнего вида каждой области. Разработчики могут применять различные настройки форматирования к области, изменяя ее передний план, фоновый цвет и формат заливки и т. д.

В приведенном ниже примере мы применили различные настройки форматирования к различным видам областей диаграммы. Эти области включают:

- Область построения
- Область диаграммы
- Область [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)
- Область одной точки в [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

После выполнения примерного кода на рабочем листе будет добавлена столбчатая диаграмма, показанная ниже:

**Столбчатая диаграмма с заполненными областями** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Установка линий диаграммы**

Разработчики также могут применять различные типы стилей к линиям или маркерам данных в [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), как показано ниже на примере. После выполнения примерного кода на рабочем листе добавляется столбчатая диаграмма, показанная ниже:

**Столбчатая диаграмма после применения стилей линий** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Применение тем Microsoft Excel 2007/2010 к диаграммам**

Разработчики могут применять различные темы и цвета Microsoft Excel к [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) и другим объектам диаграммы, как показано в примере ниже.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Настройка заголовков диаграмм или осей**

Вы можете использовать Microsoft Excel для установки заголовков диаграммы и ее осей в среде WYSIWYG, как показано ниже.

**Установка заголовков диаграммы и ее осей с помощью Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells также позволяет разработчикам устанавливать заголовки диаграммы и ее осей динамически. Все диаграммы и их оси содержат метод [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text), который можно использовать для установки их заголовков, как показано ниже в примере. После выполнения примерного кода на рабочем листе будет добавлена столбчатая диаграмма, показанная ниже:

**Столбчатая диаграмма после установки заголовков** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Настройка основных линий сетки**

#### **Скрытие основных линий сетки**

Разработчики могут контролировать видимость основных линий сетки с помощью метода [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) объекта [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line). После скрытия основных линий сетки столбчатая диаграмма, добавленная на лист, будет иметь следующий вид:

**Столбчатая диаграмма с скрытыми основными линиями сетки** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Изменение настроек основных линий сетки**

Разработчики могут контролировать не только видимость основных линий сетки, но и другие свойства, включая цвет и т.д. После установки цвета основных линий сетки, столбчатая диаграмма на листе будет иметь следующий вид:

**Столбчатая диаграмма с цветными основными линиями сетки** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Установка границ для задних и боковых стен**

С момента выпуска Microsoft Excel 2007 стены трехмерной диаграммы были разделены на две части: боковая стена и задняя стена, поэтому мы должны использовать два объекта [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), чтобы представить их отдельно, и вы можете получить к ним доступ, используя [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) и [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

Приведенный ниже пример показывает, как установить границу боковой стены, используя различные атрибуты.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Изменение позиции и размера диаграммы**

Иногда вы хотите изменить позицию или размер новой или существующей диаграммы на листе. Aspose.Cells предоставляет свойство [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) для этого. Вы можете использовать его подсвойства для изменения размера диаграммы с новыми **высотой** и **шириной** или для изменения позиции с новыми **X** и **Y** координатами.

### **Изменение позиции и размера диаграммы**

Чтобы изменить позицию диаграммы (координаты X, Y) и размер (высота, ширина), используйте эти свойства:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Приведенный ниже пример поясняет использование указанных выше свойств. Он загружает существующую книгу, в которой содержится диаграмма на первом листе. Затем изменяет размер и позицию диаграммы и сохраняет книгу.

Перед выполнением примера кода исходный файл выглядит следующим образом:

**Размер и положение диаграммы перед выполнением образца кода** 

![todo:image_alt_text](chart-formatting_7.png)

После выполнения выглядит вот так:

**Размер и положение диаграммы после выполнения образца кода** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Манипулирование дизайнерскими диаграммами**

Иногда вам может потребоваться изменить или модифицировать диаграммы в файлах шаблонов дизайнера. Aspose.Cells полностью поддерживает управление диаграммами дизайнера и их содержимым. Данные, содержимое диаграммы, фоновое изображение и форматирование могут быть сохранены с точностью.

### **Управление диаграммами дизайнера в файлах шаблонов**

Для управления диаграммами дизайнера в файле шаблона используйте все вызовы API, связанные с диаграммой. Например, используйте свойство [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts), чтобы получить существующую коллекцию диаграмм в файле шаблона.

#### **Создание диаграммы**

В следующем примере показано, как создать круговую диаграмму. Позже мы будем изменять эту диаграмму. Следующий вывод сгенерирован кодом.

**Входная круговая диаграмма** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Изменение диаграммы**

В следующем примере показано, как изменить существующую диаграмму. В этом примере мы изменяем созданную выше диаграмму. Следующий вывод сгенерирован кодом. Обратите внимание, что цвет заголовка диаграммы изменился с синего на черный, и 'England 30000' был изменен на 'United Kingdom, 30K'.

**Круговая диаграмма была изменена** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Изменение линейной диаграммы в шаблоне конструктора**

В этом примере мы будем изменять линейную диаграмму. Мы добавим несколько рядов данных к существующей диаграмме и изменим цвета их линий.

Сначала посмотрите на линейную диаграмму дизайнера.

**Входная линейная диаграмма** 

![todo:image_alt_text](chart-formatting_11.png)

Теперь мы управляем линейной диаграммой (которая находится в файле **linechart.xls**) с помощью следующего кода. Следующий вывод сгенерирован кодом.

**Измененная линейная диаграмма** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Использование мини-графиков**

Microsoft Excel 2010 позволяет анализировать информацию более чем когда-либо прежде. С его помощью пользователи могут отслеживать и выделять важные тенденции данных с помощью новых средств анализа и визуализации. Мини-графики - это миниатюрные графики, которые можно разместить внутри ячеек, чтобы одновременно просматривать данные и диаграмму на одной и той же таблице. При правильном использовании мини-графиков анализ данных становится более быстрым и точным. Они также обеспечивают простой просмотр информации, избегая переполненных листов с множеством занятых диаграмм.

Aspose.Cells предоставляет API для обработки мини-графиков в электронных таблицах.

### **Мини-графики в Microsoft Excel**

Для вставки мини-графиков в Microsoft Excel 2010:

1. Выберите ячейки, где вы хотите разместить мини-графики. Чтобы упростить их просмотр, выберите ячейки сбоку от данных.
1. Нажмите **Вставка** на ленте и затем выберите **столбец** в группе **Мини-графики**.

![todo:image_alt_text](chart-formatting_13.png)

1. Выберите или введите диапазон ячеек на листе, который содержит исходные данные.
   Графики появляются.

Спарклайны помогают увидеть тенденции, например, или результаты побед и поражений в лиге софтбола. Спарклайны даже могут подытожить всю сезонную статистику каждой команды в лиге.

![todo:image_alt_text](chart-formatting_14.png)

### **Мини-графики с использованием Aspose.Cells**

Разработчики могут создавать, удалять или считывать спарклайны (в файле шаблона), используя API, предоставленный Aspose.Cells. Добавляя пользовательскую графику для указанного диапазона данных, разработчики имеют возможность добавлять разные типы маленьких графиков в выбранные ячейки.

Приведенный ниже пример демонстрирует функцию мини-графиков. Пример показывает, как:

1. Открыть простой файл шаблона.
1. Прочитать информацию о мини-графиках для листа.
1. Добавьте новые искры для определенного диапазона данных в область ячейки.
1. Сохраняет файл Excel на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Применение 3D-формата к графику**

Возможно, вам понадобятся стили 3D-графики, чтобы получить именно те результаты, которые вам нужны. API Aspose.Cells предоставляет соответствующий API для применения форматирования 3D, используемого в Microsoft Excel 2007, как показано в данной статье.

### **Установка 3D-формата графику**

Ниже приведен полный пример, показывающий, как создать график и применить форматирование 3D Microsoft Excel 2007. После выполнения приведенного выше примера кода на рабочий лист будет добавлен столбчатый график (с эффектами 3D) как показано ниже.

**Столбчатый график с 3D-форматированием**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Для полного списка поддерживаемых 2D и 3D графиков см. [Поддерживаемые типы графиков для визуализации](/cells/ru/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Продвинутые темы**
- [Установите изображение в качестве фона в диаграмме](/cells/ru/java/set-picture-as-background-fill-in-the-chart/)
