---
title: Создание круговой диаграммы с линиями выноски
description: Узнайте, как использовать Aspose.Cells for .NET для создания круговой диаграммы с выносными линиями в Microsoft Excel. Наше руководство покажет, как добавить линии-выноски, которые соединяют точки данных с легендой и повышают общую четкость вашей диаграммы.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Круговая диаграмма
type: docs
weight: 45
url: /ru/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

В этой статье объясняется, как создать круговую диаграмму с линиями выноски с нуля, используя Aspose.Cells for .NET API. В Excel параметр «Показать линии выноски» установлен по умолчанию, поэтому при создании круговой диаграммы в Excel отображаются линии выноски. Однако при создании аналогичной диаграммы с API Aspose.Cells вам необходимо явно указать[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) свойство.

{{% /alert %}}

 Чтобы продемонстрировать использование Aspose.Cells for .NET API для создания круговой диаграммы с линиями выноски, мы сначала создадим новый[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) и введите некоторые данные, которые будут служить источником данных серии. Как только данные будут готовы, мы добавим[**Диаграмма**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) типа[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)к коллекции диаграмм и настройте ее различные аспекты, чтобы получить желаемый вид диаграммы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

На данный момент мы создали круговую диаграмму и установили ее различные аспекты. Теперь мы собираемся включить линии-выноски для диаграммы. Обратите внимание: чтобы отобразить линии-выноски, нам придется немного сдвинуть метки данных.

Следующий фрагмент кода включает линии-выноски, обновляет диаграмму, а затем вычисляет положения меток данных для их соответствующего перемещения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Наконец, следующий код сохраняет диаграмму в формате изображения, а книгу — в формате XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Результирующая круговая диаграмма**|
| :- |
|![задача: image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **Предварительные темы**
- [Пользовательские цвета срезов или секторов в круговой диаграмме](/cells/ru/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Определите, находятся ли точки данных во второй круговой диаграмме или полосе круговой диаграммы.](/cells/ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  Статьи по Теме

- [Создание диаграмм](/cells/ru/net/creating-charts/)
- [Настройка диаграмм](/cells/ru/net/customizing-charts/)
- [Форматирование данных в диаграммах](/cells/ru/net/data-formatting-in-charts/)
- [Настройка внешнего вида диаграммы](/cells/ru/net/setting-chart-appearance/)

