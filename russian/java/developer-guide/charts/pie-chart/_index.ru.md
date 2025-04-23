---
title: Создание круговой диаграммы с линиями проводниками
linktitle: Круговая диаграмма
type: docs
weight: 170
url: /ru/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Эта статья объясняет, как создать круговую диаграмму с ведущими линиями с нуля, используя API Aspose.Cells for Java. В Excel опция 'Показывать ведущие линии' установлена по умолчанию, поэтому при создании круговой диаграммы в Excel ведущие линии отображаются. Однако при создании аналогичной диаграммы с помощью API Aspose.Cells необходимо явно установить свойство [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines).

{{% /alert %}}

## **Создание круговой диаграммы с линиями**

Чтобы продемонстрировать использование API Aspose.Cells for Java для создания круговой диаграммы с ведущими линиями, сначала мы создадим новый [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) и введем некоторые данные, которые будут служить источником данных для серии. Как только данные будут на месте, мы добавим [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) типа [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) в коллекцию диаграмм и установим различные его аспекты для получения желаемого вида диаграммы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Результативная круговая диаграмма**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Связанные статьи

- [Создание и настройка диаграмм](/cells/ru/java/creating-and-customizing-charts/)
- [Форматирование диаграмм](/cells/ru/java/chart-formatting/)
{{< app/cells/assistant language="java" >}}
