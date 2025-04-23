---
title: Создание круговой диаграммы с линиями проводниками
description: Узнайте, как использовать Aspose.Cells for .NET для создания круговой диаграммы с линиями проводниками в Microsoft Excel. Наш руководство продемонстрирует, как добавить линии проводники, соединяющие точки данных с легендой, и повысить общую ясность вашей диаграммы.
keywords: Aspose.Cells for .NET, Круговая диаграмма, Линии проводники, Microsoft Excel, Визуализация данных, Настройка диаграммы.
linktitle: Круговая диаграмма
type: docs
weight: 45
url: /ru/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

В данной статье объясняется, как создать круговую диаграмму с линиями-проводниками с нуля при использовании Aspose.Cells for .NET API. В Excel опция 'Показывать линии-проводники' установлена по умолчанию, поэтому при создании круговой диаграммы в Excel линии-проводники отображаются. Однако, при создании аналогичной диаграммы с API Aspose.Cells, вы должны явно установить свойство [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines).

{{% /alert %}}

Для демонстрации использования Aspose.Cells for .NET API для создания круговой диаграммы с линиями-проводниками мы сначала создадим новый [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) и введем некоторые данные, которые послужат источником данных для рядов. После размещения данных мы добавим [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) типа [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) в коллекцию диаграмм и установим различные аспекты, чтобы получить нужный вид диаграммы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

До сих пор мы создали круговую диаграмму и установили различные ее аспекты. Теперь мы собираемся включить линии-проводники для диаграммы. Обратите внимание, чтобы показать линии-проводники, нужно немного переместить метки данных.

Следующий кусок кода включает линии-проводники, обновляет диаграмму, а затем рассчитывает позиции меток данных для их соответствующего перемещения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Наконец, следующий код сохраняет диаграмму в формате изображения и книгу в формате XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Результирующая круговая диаграмма**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Продвинутые темы**
- [Пользовательские цвета секторов в круговой диаграмме](/cells/ru/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме](/cells/ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Связанные статьи

- [Создание диаграмм](/cells/ru/net/creating-charts/)
- [Настраивание диаграмм](/cells/ru/net/customizing-charts/)
- [Форматирование данных в диаграммах](/cells/ru/net/data-formatting-in-charts/)
- [Настройка внешнего вида диаграммы](/cells/ru/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
