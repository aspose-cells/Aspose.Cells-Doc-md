---
title: Отображение диаграммы
linktitle: В изображение или PDF
type: docs
weight: 45
url: /ru/net/chart-rendering/
---
## **Отображение диаграмм**

 API-интерфейсы Aspose.Cells поддерживают преобразование диаграмм Excel в изображения и форматы PDF без каких-либо дополнительных инструментов или приложений. Чтобы обеспечить поддержку рендеринга,[**Диаграмма**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) класс выставил[**Изображать**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**Топдф**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)методы с множеством перегрузок для наилучшего соответствия требованиям приложения.

### **Преобразование диаграмм в изображения**

[**Диаграмма.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**Топдф**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) Метод имеет множество перегрузок для поддержки как простого, так и расширенного рендеринга. Если требование приложения состоит в том, чтобы отображать диаграмму в размерах по умолчанию, мы предлагаем вам использовать[**Диаграмма.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)следующим образом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Также возможно преобразовать диаграммы в изображения с расширенными настройками. Aspose.Cells API-интерфейсы предоставили перегруженную версию[**Диаграмма.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) метод, который может принимать экземпляр[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), при этом позволяя указать такие параметры, как разрешение, режим сглаживания, формат изображения и так далее.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **График рендеринга на PDF**

 Чтобы отобразить диаграмму в формате PDF, API-интерфейсы Aspose.Cells предоставили[**Диаграмма.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)метод с возможностью сохранения результирующего PDF на пути к диску или в потоке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Поддерживаемые типы диаграмм для визуализации**

 Есть несколько типов диаграмм, которые в настоящее время не поддерживаются для визуализации. Такие типы диаграмм содержат** Н** в**Поддерживаемый** столбец в таблице ниже.

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
|**Площадь**|Площадь|**Д**|
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
|**Акции**|ЗапасВысокийНизкийЗакрыть|**Д**|
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

Если вы попытаетесь преобразовать неподдерживаемые типы диаграмм в изображение или PDF, вы можете получить изображения нулевого размера или пустое PDF.

{{% /alert %}}

## **Предварительные темы**
- [Преобразование диаграммы в PDF с желаемым размером страницы](/cells/ru/net/chart-to-pdf/)
