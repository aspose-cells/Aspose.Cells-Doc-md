---
title: Отображение диаграммы
type: docs
weight: 30
url: /ru/cpp/chart-rendering/
---
## **Создание диаграмм**

Aspose.Cells API-интерфейсы поддерживают создание различных диаграмм Excel, как описано в разделе[Создание и настройка диаграмм Excel](/cells/ru/cpp/creating-and-customizing-charts/). Чтобы продемонстрировать использование API-интерфейсов Aspose.Cells для отображения диаграмм в формате изображения и PDF, мы создадим диаграмму типа «Столбец» в соответствии со следующим фрагментом кода.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Отображение диаграмм**

Aspose.Cells API-интерфейсы поддерживают преобразование диаграмм Excel в изображения и форматы PDF без каких-либо дополнительных инструментов или приложений. Чтобы обеспечить поддержку рендеринга, класс Chart предоставляет методы ToImage и ToPdf с множеством перегрузок, которые наилучшим образом соответствуют требованиям приложения.

### **Преобразование диаграмм в изображения**

Метод Chart.toImage имеет множество перегрузок для поддержки как простого, так и расширенного рендеринга. Если требование приложения состоит в том, чтобы отображать диаграмму в размерах по умолчанию, мы предлагаем вам использовать метод Chart.toImage следующим образом.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Преобразование диаграммы в PDF**

Чтобы преобразовать диаграмму в формат PDF, API-интерфейсы Aspose.Cells предоставили метод Chart.ToPdf с возможностью сохранения результирующего PDF-файла на пути к диску или в потоке.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Поддерживаемые типы диаграмм для визуализации**

Есть несколько типов диаграмм, которые в настоящее время не поддерживаются для визуализации. Такие типы диаграмм содержат**Н** в**Поддерживаемый** столбец таблицы ниже.

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
|Запас|ЗапасВысокийНизкийЗакрыть|**Д**|
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
