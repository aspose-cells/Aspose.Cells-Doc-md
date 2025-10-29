---
title: Создание круговой диаграммы с линиями проводниками
description: Узнайте, как создать круговую диаграмму с выносными линиями в Microsoft Excel с помощью Aspose.Cells для Python via .NET. Наше руководство покажет, как добавлять выносные линии, соединяющие точки данных с легендой и улучшая общую ясность вашего графика.
keywords: Aspose.Cells для Python via .NET, Круговая диаграмма, Выносные линии, Microsoft Excel, Визуализация данных, Настройка графика.
linktitle: Круговая диаграмма
type: docs
weight: 45
url: /ru/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

 Эта статья объясняет, как создать круговую диаграмму с выносными линиями с нуля, используя API Aspose.Cells для Python via .NET. В Excel опция 'Показать выносные линии' установлена по умолчанию, поэтому при создании круговой диаграммы линии отображаются. Однако при создании аналогичной диаграммы с помощью API Aspose.Cells для Python via .NET необходимо явно установить свойство [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines).

{{% /alert %}}

Чтобы продемонстрировать использование API Aspose.Cells для Python via .NET для создания круговой диаграммы с выносными линиями, сначала создадим новый [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) и введем некоторые данные, которые будут служить источником данных для серии. После установки данных добавим [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) типа [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) в коллекцию графиков и настроим его параметры для получения желаемого вида графика.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

До сих пор мы создали круговую диаграмму и установили различные ее аспекты. Теперь мы собираемся включить линии-проводники для диаграммы. Обратите внимание, чтобы показать линии-проводники, нужно немного переместить метки данных.

Следующий кусок кода включает линии-проводники, обновляет диаграмму, а затем рассчитывает позиции меток данных для их соответствующего перемещения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Наконец, следующий код сохраняет диаграмму в формате изображения и книгу в формате XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Результирующая круговая диаграмма**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Продвинутые темы**
- [Пользовательские цвета секторов в круговой диаграмме](/cells/ru/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме](/cells/ru/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Связанные статьи

- [Создание диаграмм](/cells/ru/python-net/creating-charts/)
- [Настраивание диаграмм](/cells/ru/python-net/customizing-charts/)
- [Форматирование данных в диаграммах](/cells/ru/python-net/data-formatting-in-charts/)
- [Настройка внешнего вида диаграммы](/cells/ru/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
