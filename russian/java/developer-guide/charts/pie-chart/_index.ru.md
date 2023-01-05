---
title: Создание круговой диаграммы с линиями выноски
linktitle: Круговая диаграмма
type: docs
weight: 170
url: /ru/java/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 В этой статье объясняется, как создать круговую диаграмму с линиями выноски с нуля при использовании Aspose.Cells for Java API. В Excel параметр «Показать линии выноски» установлен по умолчанию, поэтому при создании круговой диаграммы в Excel отображаются линии выноски. Однако при создании аналогичной диаграммы с API Aspose.Cells необходимо явно указать[**Серия.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines) имущество.

{{% /alert %}}

## **Создание круговой диаграммы с линиями выноски**

 Чтобы продемонстрировать использование Aspose.Cells for Java API для создания круговой диаграммы с линиями выноски, мы сначала создадим новый[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) и введите некоторые данные, которые будут служить источником данных серии. Как только данные будут на месте, мы добавим[**Диаграмма**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) типа[**пирог**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE)к набору диаграмм и установите его различные аспекты, чтобы получить желаемое представление диаграммы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Результирующая круговая диаграмма**

![дело:изображение_альтернативный_текст](creating-pie-chart-with-leader-lines_1.png)

## Статьи по Теме

- [Создание и настройка диаграмм](/cells/ru/java/creating-and-customizing-charts/)
- [Форматирование диаграммы](/cells/ru/java/chart-formatting/)
