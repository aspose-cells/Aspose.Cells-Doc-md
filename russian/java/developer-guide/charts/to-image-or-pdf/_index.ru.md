---
title: Отображение диаграммы
linktitle: В изображение или PDF
type: docs
weight: 40
url: /ru/java/chart-rendering/
---
## **Создание диаграмм**

 Aspose.Cells API-интерфейсы поддерживают создание различных диаграмм Excel, как описано в разделе[Создание и настройка диаграмм Excel](/cells/ru/java/creating-and-customizing-charts/)Чтобы продемонстрировать использование API-интерфейсов Aspose.Cells для отображения диаграмм в формате изображения и PDF, мы создадим диаграмму типа «Столбец» в соответствии со следующим фрагментом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Отображение диаграмм**

 Aspose.Cells API-интерфейсы поддерживают преобразование диаграмм Excel в изображения и форматы PDF без каких-либо дополнительных инструментов или приложений. Чтобы обеспечить поддержку рендеринга,[**Диаграмма**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)класс выставил[**изображать**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**вPDF**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) методы с множеством перегрузок для наилучшего соответствия требованиям приложения.

### **Преобразование диаграмм в изображения**

[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) имеет множество перегрузок для поддержки как простого, так и расширенного рендеринга. Если требование приложения состоит в том, чтобы отображать диаграмму в размерах по умолчанию, мы предлагаем вам использовать[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) следующим образом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Также возможно преобразовать диаграммы в изображения с расширенными настройками. Aspose.Cells API-интерфейсы предоставили перегруженную версию[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) метод, который может принимать экземпляр[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)при этом позволяя указывать такие параметры, как разрешение, подсказки рендеринга, формат изображения и так далее.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Преобразование диаграммы в PDF**

 Чтобы преобразовать диаграмму в формат PDF, API-интерфейсы Aspose.Cells предоставили[**Диаграмма.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) метод с возможностью сохранения результирующего PDF-файла на пути к диску или в экземпляре OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Поддерживаемые типы диаграмм для визуализации**

 Есть несколько типов диаграмм, которые в настоящее время не поддерживаются для визуализации. Такие типы диаграмм содержат** Н** в**Поддерживаемый** столбец таблицы ниже.

|**Тип диаграммы**|**Подтип диаграммы**|**Поддерживается**|
|:- |:- |:- |
|**Столбец**|Столбец|**Д**|
||КолонкаС накоплением|**Д**|
||Столбец100PercentStacked|**Д**|
||Column3DClustered|**Д**|
||Столбец3DStacked|**Д**|
||Столбец3D100PercentStacked|**Д**|
||Колонка3D|**Д**|
|**Бар**|Бар|**Д**|
||БарСложенный|**Д**|
||Bar100PercentStacked|**Д**|
||Bar3DCкластеризованный|**Д**|
||Bar3DStacked|**Д**|
||Bar3D100PercentStacked|**Д**|
|**Линия**|Линия|**Д**|
||LineStacked|**Д**|
||Line100PercentStacked|**Д**|
||LineWithDataMarkers|**Д**|
||LineStackedWithDataMarkers|**Д**|
||Line100PercentStackedWithDataMarkers|**Д**|
||Линия3D|**Д**|
|**пирог**|пирог|**Д**|
||Пирог3D|**Д**|
||пирог пирог|**Д**|
||ПирогВзорван|**Д**|
||Pie3DВзорван|**Д**|
||Пиг-Бар|**Д**|
|**Разброс**|Разброс|**Д**|
||ScatterConnectedByCurvesWithDataMarker|**Д**|
||ScatterConnectedByCurvesWithoutDataMarker|**Д**|
||ScatterConnectedByLinesWithDataMarker|**Д**|
||ScatterConnectedByLinesWithoutDataMarker|**Д**|
|**Область**|Область|**Д**|
||ПлощадьСложенный|**Д**|
||Area100PercentStacked|**Д**|
||Площадь3D|**Д**|
||Площадь3DС накоплением|**Д**|
||Area3D100PercentStacked|**Д**|
|**Пончик**|Пончик|**Д**|
||ПончикВзорван|**Д**|
|**Радар**|Радар|**Д**|
||Радарвисдатамаркерс|**Д**|
||Радар заполнен|**Д**|
|**Поверхность**|Поверхность3D|Н|
||ПоверхностьКаркас3D|Н|
||ПоверхностьКонтур|Н|
||ПоверхностьКонтурКаркас|Н|
|**Пузырь**|Пузырь|**Д**|
||Пузырь3D|Н|
|**Запас**|ЗапасВысокийНизкийЗакрыть|**Д**|
||ЗапасОткрытыйВысокийНизкийЗакрыть|**Д**|
||StockVolumeHighLowClose|**Д**|
||StockVolumeOpenHighLowClose|**Д**|
|**Цилиндр**|Цилиндр|**Д**|
||ЦилиндрСложенный|**Д**|
||Цилиндр100PercentStacked|**Д**|
||ЦилиндрическийБар|**Д**|
||ЦилиндрическийБарС накоплением|**Д**|
||ЦилиндрическийBar100PercentStacked|**Д**|
||ЦилиндрическаяКолонка3D|**Д**|
|**Конус**|Конус|**Д**|
||КонусСложенный|**Д**|
||конус100процентов|**Д**|
||КоническийБар|**Д**|
||КоническийБарС накоплением|**Д**|
||ConicalBar100PercentStacked|**Д**|
||КоническаяКолонна3D|**Д**|
|**Пирамида**|Пирамида|**Д**|
||ПирамидаСложенный|**Д**|
||Пирамида100PercentStacked|**Д**|
||ПирамидаБар|**Д**|
||ПирамидаБарС накоплением|**Д**|
||PyramidBar100PercentStacked|**Д**|
||ПирамидаКолонка3D|**Д**|
|**КоробкаУискер**|КоробкаУискер|Д|
|**Воронка**|Воронка|**Д**|
|**ПаретоЛиния**|ПаретоЛиния|**Д**|
|**солнечные лучи**|солнечные лучи|**Д**|
|**Древовидная карта**|Древовидная карта|**Д**|
|**Водопад**|Водопад|**Д**|
|**Гистограмма**|Гистограмма|Д|
|**карта**|карта|**Н**|

{{% alert color="primary" %}}

Если вы попытаетесь преобразовать неподдерживаемые типы диаграмм в изображение или PDF, вы можете получить изображения нулевого размера или пустой PDF.

{{% /alert %}}


## **Предварительные темы**
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/java/converting-chart-to-image-in-svg-format/)
- [Создайте PDF-файл диаграммы с желаемым размером страницы](/cells/ru/java/create-chart-pdf-with-desired-page-size/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/java/export-chart-to-svg-with-viewbox-attribute/)
