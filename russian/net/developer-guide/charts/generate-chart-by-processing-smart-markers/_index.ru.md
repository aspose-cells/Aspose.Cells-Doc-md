---
title: Создайте диаграмму путем обработки смарт-маркеров
description: Узнайте, как создавать диаграммы с помощью интеллектуальных маркеров, используя номер Aspose.Cells for .NET. Наше руководство покажет вам, как обрабатывать интеллектуальные маркеры и их свойства, чтобы улучшить внешний вид и удобство использования ваших диаграмм.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /ru/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API предоставляют[**Дизайнер рабочих книг**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) класс для работы со смарт-маркерами, где форматирование и формулы помещаются в электронные таблицы дизайнера, а затем обрабатываются с помощью[**Дизайнер рабочих книг**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)класс для заполнения данных в соответствии с указанными смарт-маркерами. Также можно создавать диаграммы Excel путем обработки смарт-маркеров, для чего потребуются следующие шаги.

- Создание дизайнерской таблицы
- Обработка электронной таблицы дизайнера по указанному источнику данных
- Создание диаграммы на основе заполненных данных

{{% /alert %}}

##  Создание таблицы дизайнера

Электронная таблица дизайнера — это простой файл Excel, созданный с помощью приложения Excel Microsoft или API Aspose.Cells, содержащий визуальное форматирование, формулы и интеллектуальные маркеры, содержимое которых можно заполнить во время выполнения.

Для простоты мы создадим электронную таблицу дизайнера, используя Aspose.Cells for .NET API, а затем обработаем ее с помощью динамически создаваемого источника данных в демонстрационных целях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

##  Таблица дизайнера обработки

Для обработки электронной таблицы дизайнера необходимо иметь источник данных, соответствующий смарт-маркерам, используемым в электронной таблице дизайнера. Например, мы создали запись Smart Marker как &=Sales.Year, которая представляет столбец Year в DataTable Sales. Если соответствующий столбец недоступен в источнике данных, API Aspose.Cells пропустят обработку для этого конкретного смарт-маркера, и в результате данные для конкретного смарт-маркера не будут заполнены.

Чтобы продемонстрировать этот вариант использования, мы создадим источник данных с нуля и обработаем его с помощью электронной таблицы дизайнера, созданной на предыдущем шаге. Однако в сценарии реального времени данные уже могут быть доступны для дальнейшей обработки, поэтому вы можете пропустить создание источника данных, если данные уже доступны.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Обработка смарт-маркеров довольно проста, как показано в следующем фрагменте кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Приведенный выше фрагмент кода использует существующий экземпляр[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, созданный на первом шаге. Если у вас уже есть файл электронной таблицы дизайнера на диске или в памяти, вы можете создать экземпляр[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, загрузив существующую электронную таблицу дизайнера.

{{% /alert %}}

##  Создание диаграммы

 Как только данные будут готовы, все, что нам нужно сделать, — это создать диаграмму на основе источника данных. Для простоты примера мы будем использовать[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)метод, чтобы нам не приходилось настраивать диаграмму дальше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
