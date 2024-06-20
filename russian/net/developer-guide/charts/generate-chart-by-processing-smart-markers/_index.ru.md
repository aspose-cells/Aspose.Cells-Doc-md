---
title: Генерация диаграммы путем обработки умных маркеров
description: Узнайте, как создавать диаграммы с использованием умных маркеров с помощью Aspose.Cells for .NET. Наш руководство покажет вам, как обрабатывать умные маркеры и их свойства для улучшения внешнего вида и удобства использования ваших диаграмм.
keywords: Aspose.Cells for .NET, создание диаграмм, умные маркеры, внешний вид, удобство использования, обработка.
type: docs
weight: 2100
url: /ru/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

API Aspose.Cells предоставляет класс [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) для работы с умными маркерами, где форматирование и формулы помещены в дизайнерские электронные таблицы, а затем обрабатываются с помощью класса [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) для заполнения данных в соответствии с указанными умными маркерами. Также возможно создать диаграммы Excel путем обработки умных маркеров, для чего потребуются следующие шаги.

- Создание таблиц дизайнера
- Обработка дизайнерской электронной таблицы в соответствии с указанным источником данных
- Создание диаграммы на основе заполненных данных

{{% /alert %}}

## Создание дизайнерской электронной таблицы

Дизайнерская электронная таблица - это простой файл Excel, созданный с помощью приложения Microsoft Excel или API Aspose.Cells, содержащий визуальное форматирование, формулы и умные маркеры, куда содержимое может быть заполняемо во время выполнения.

Для простоты мы создадим дизайнерскую электронную таблицу с использованием API Aspose.Cells for .NET, а затем обработаем ее с использованием динамически созданного источника данных в демонстрационных целях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Обработка дизайнерской электронной таблицы

Чтобы обработать дизайнерскую электронную таблицу, необходимо иметь источник данных, соответствующий использованным умным маркерам в дизайнерской электронной таблице. Например, мы создали запись умного маркера как &=Sales.Year, отображающую столбец Year в DataTable Sales. В случае отсутствия соответствующего столбца в источнике данных, API Aspose.Cells пропустит обработку этого конкретного умного маркера, и в результате данные для этого конкретного умного маркера не будут заполняться.

Для демонстрации данного случая мы создадим источник данных с нуля и обработаем его с использованием созданной на предыдущем шаге дизайнерской электронной таблицы. Однако в реальном сценарии данные могут уже быть доступны для дальнейшей обработки, поэтому вы можете пропустить создание источника данных, если данные уже доступны.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Обработка умных маркеров довольно проста, как показано в следующем фрагменте кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

В приведенном выше фрагменте кода используется существующий экземпляр класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), созданный на первом шаге. Если у вас уже есть файл дизайнерской электронной таблицы на диске или в памяти, вы можете создать экземпляр класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), загрузив существующую дизайнерскую электронную таблицу.

{{% /alert %}}

## Создание диаграммы

Как только данные на месте, все, что нам нужно сделать, это создать диаграмму на основе источника данных. Чтобы сделать пример более простым, мы используем метод [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange), чтобы нам не нужно было дополнительно настраивать диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
