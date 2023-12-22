---
title: Рендеринг диаграмм
type: docs
weight: 30
url: /ru/cpp/chart-rendering/
---
##  **Создание диаграмм**

Aspose.Cells Поддержка API для создания достоверных диаграмм Excel, как подробно описано в этой теме.[Создание и настройка диаграмм Excel](/cells/ru/cpp/creating-and-customizing-charts/). Чтобы продемонстрировать использование API Aspose.Cells для отображения диаграмм в формате изображения и PDF, мы создадим диаграмму типа Столбец, как показано в следующем фрагменте.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **Рендеринг диаграмм**

API-интерфейсы Aspose.Cells поддерживают преобразование диаграмм Excel в изображения и форматы PDF без необходимости использования каких-либо дополнительных инструментов или приложений. Чтобы обеспечить поддержку рендеринга, класс Chart предоставил методы ToImage и ToPdf с множеством перегрузок, которые наилучшим образом соответствуют требованиям приложения.

###  **Рендеринг диаграмм в изображения**

Метод Chart.toImage имеет множество перегрузок для поддержки как простого, так и расширенного рендеринга. Если требованием приложения является отображение диаграммы в размерах по умолчанию, мы предлагаем вам использовать метод Chart.toImage следующим образом.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **Диаграмма рендеринга на номер PDF**

Чтобы отобразить диаграмму в формате PDF, API Aspose.Cells предоставили метод Chart.ToPdf с возможностью сохранения результирующего PDF на пути к диску или в потоке.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **Поддерживаемые типы диаграмм для рендеринга**

Существует несколько типов диаграмм, которые в настоящее время не поддерживаются для рендеринга. Такие типы диаграмм содержат**N** в списке **Поддерживаемых**столбец таблицы ниже.

|**Тип диаграммы**|**Подтип диаграммы**|**Поддерживается**|
| :- | :- | :- |
|**Столбец**|Столбец|*ДА**|
| |СтолбецСложенный|*ДА**|
| |Столбец100Процент|*ДА**|
| |Столбец3DКластерный|*ДА**|
| |Столбец3DСложенный|*ДА**|
| |Столбец3D100PercentStacked|*ДА**|
| |Колонка3D|*ДА**|
|**Бар**|Бар|*ДА**|
| |БарСтекированный|*ДА**|
| |Бар100ПроцентСложенный|*ДА**|
| |Бар3DКластерный|*ДА**|
| |Бар3DСложенный|*ДА**|
| |Бар3D100ПроцентСложенный|*ДА**|
|**Линия**|Линия|*ДА**|
| |Линия с накоплением|*ДА**|
| |Линия100Процент|*ДА**|
| |LineWithDataMarkers|*ДА**|
| |LineStackedWithDataMarkers|*ДА**|
| |Line100PercentStackedWithDataMarkers|*ДА**|
| |Линия3D|*ДА**|
|**Пирог**|Пирог|*ДА**|
| |Пирог3D|*ДА**|
| |ПирогПирог|*ДА**|
| |ПирогВзорвался|*ДА**|
| |Пирог3DВзорванный|*ДА**|
| |пироговый бар|*ДА**|
|**Разброс**|Разброс|*ДА**|
| |ScatterConnectedByCurvesWithDataMarker|*ДА**|
| |ScatterConnectedByCurvesWithoutDataMarker|*ДА**|
| |ScatterConnectedByLinesWithDataMarker|*ДА**|
| |ScatterConnectedByLinesWithoutDataMarker|*ДА**|
|**Область**|Область|*ДА**|
| |ПлощадьСложенный|*ДА**|
| |Площадь100ПроцентовСложены|*ДА**|
| |Площадь3D|*ДА**|
| |Площадь3DСложенный|*ДА**|
| |Площадь3D100ПроцентСложенный|*ДА**|
|**Пончик**|Пончик|*ДА**|
| |ПончикВзорванный|*ДА**|
|**Радар**|Радар|*ДА**|
| |РадарСДаннымиМаркерами|*ДА**|
| |РадарЗаполнен|*ДА**|
|**Поверхность**|Поверхность3D|N|
| |ПоверхностьКаркас3D|N|
| |ПоверхностьКонтур|N|
| |ПоверхностьКонтурКаркас|N|
|**Пузырь**|Пузырь|*ДА**|
| |Пузырь3D|N|
|Запас|ФондовыйВысокийНизкийЗакрыть|*ДА**|
| |ФондовыйОткрытыйВысокийНизкийЗакрыть|*ДА**|
| |ФондовыйОбъемВысокийНизкийЗакрыть|*ДА**|
| |ФондовыйОбъемОткрытьВысокийНизкийЗакрыть|*ДА**|
|**Цилиндр**|Цилиндр|*ДА**|
| |ЦилиндрСложенный|*ДА**|
| |Цилиндр100Процентов|*ДА**|
| |ЦилиндрическийБар|*ДА**|
| |ЦилиндрическийБарСложенный|*ДА**|
| |ЦилиндрическийБар100%С накоплением|*ДА**|
| |ЦилиндрическаяКолонна3D|*ДА**|
|**Конус**|Конус|*ДА**|
| |КонусСложенный|*ДА**|
| |Конус100ПроцентовСложены|*ДА**|
| |КоническийБар|*ДА**|
| |КоническийБарСложенный|*ДА**|
| |КоническийБар100ПроцентСложенный|*ДА**|
| |КоническаяКолонна3D|*ДА**|
|**Пирамида**|Пирамида|*ДА**|
| |ПирамидаСложены|*ДА**|
| |Пирамида100Процентов|*ДА**|
| |ПирамидаБар|*ДА**|
| |ПирамидаБарСложены|*ДА**|
| |ПирамидаБар100ПроцентСложенный|*ДА**|
| |ПирамидаКолонна3D|*ДА**|
|**КоробкаУсы**|КоробкаУсы|Y|
|**Воронка**|Воронка|*ДА**|
|**Линия Парето**|Линия Парето|*ДА**|
|**Санберст**|Санберст|*ДА**|
|**Древовидная карта**|Древовидная карта|*ДА**|
|**Водопад**|Водопад|*ДА**|
|**Гистограмма**|Гистограмма|Y|
|**карта**|карта|*Н**|

{{% alert color="primary" %}}

Если вы попытаетесь преобразовать неподдерживаемые типы диаграмм в изображение или PDF, вы можете получить изображения с нулевым размером или пустое значение PDF.

{{% /alert %}}
