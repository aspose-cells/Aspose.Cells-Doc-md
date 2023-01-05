---
title: Сгенерируйте диаграмму, обработав интеллектуальные маркеры
type: docs
weight: 2100
url: /ru/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API предоставляют[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)класс для работы со смарт-маркерами, где форматирование и формулы помещаются в электронные таблицы конструктора, а затем обрабатываются с помощью[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)класс для заполнения данных в соответствии с указанными смарт-маркерами. Также можно создавать диаграммы Excel, обрабатывая смарт-маркеры, для чего потребуются следующие шаги.

- Создание дизайнерской таблицы
- Электронная таблица конструктора обработки для указанного источника данных
- Создание диаграммы на основе заполненных данных

{{% /alert %}}

## Создание электронной таблицы конструктора

Электронная таблица дизайнера — это простой файл Excel, созданный с помощью приложения Excel Microsoft или API-интерфейсов Aspose.Cells, содержащий визуальное форматирование, формулы и интеллектуальные маркеры, содержимое которых может быть заполнено во время выполнения.

Для простоты мы создадим электронную таблицу дизайнера, используя Aspose.Cells for .NET API, а затем обработаем ее с помощью динамически созданного источника данных в демонстрационных целях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Электронная таблица дизайнера обработки

Для обработки электронной таблицы дизайнера необходимо иметь источник данных, соответствующий смарт-маркерам, используемым в электронной таблице дизайнера. Например, мы создали запись Smart Marker как &=Sales.Year, которая представляет столбец Year в DataTable Sales. Если соответствующий столбец недоступен в источнике данных, API-интерфейсы Aspose.Cells пропустят обработку для этого конкретного смарт-маркера, и в результате данные для конкретного смарт-маркера не будут заполнены.

Чтобы продемонстрировать этот вариант использования, мы создадим источник данных с нуля и обработаем его с помощью электронной таблицы дизайнера, созданной на предыдущем шаге. Однако в сценарии реального времени данные могут уже быть доступны для дальнейшей обработки, поэтому вы можете пропустить создание источника данных, если данные уже доступны.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Обработка интеллектуальных маркеров довольно проста, как показано в следующем фрагменте кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Приведенный выше фрагмент кода использует существующий экземпляр класса[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, созданный на первом этапе. Если у вас уже есть файл электронной таблицы конструктора на диске или в памяти, вы можете создать экземпляр[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class, загрузив существующую электронную таблицу конструктора.

{{% /alert %}}

## Создание диаграммы

 Как только данные будут на месте, все, что нам нужно сделать, это создать диаграмму на основе источника данных. Чтобы не усложнять пример, мы будем использовать[**Диаграмма.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)метод, чтобы нам не пришлось дополнительно настраивать диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
